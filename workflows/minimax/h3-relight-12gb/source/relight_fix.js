// Frontend 1.58.5: convertToSubgraph re-orders the inputs of autogrow / dynamic nodes but keeps the old slot numbers on
// their links, so links land on the wrong input (seen on MiniMaxH3ReferenceToVideo and Math Expression, 2026-11-11).
// Before the tags are stripped: for every node, move each link to the input the API graph says it belongs to.
window.__beforeStrip = async (top, spec) => {
  const log = [];
  const L = (g, id) => g.links.get ? g.links.get(id) : g.links[id];
  const graphs = [];
  const walk = (g, parent, inst) => { graphs.push({ g, parent, inst }); for (const n of g._nodes) if (n.subgraph) walk(n.subgraph, g, n); };
  walk(top, null, null);
  const info = g => graphs.find(x => x.g === g);
  // origin of a link, followed through subgraph boundaries, as [api key, slot]
  function resolve(g, originId, originSlot, depth = 0) {
    if (depth > 10) return null;
    if (Number(originId) === -10) {
      const { parent, inst } = info(g); if (!parent) return null;
      const name = g.inputs[originSlot]?.name;
      const hi = inst.inputs.find(i => i.name === name);
      if (!hi || hi.link == null) return null;
      const l = L(parent, hi.link); return l ? resolve(parent, l.origin_id, l.origin_slot, depth + 1) : null;
    }
    const n = g.getNodeById(originId); if (!n) return null;
    if (n.subgraph) {
      const so = n.subgraph.outputs[originSlot];
      const lid = so?.linkIds?.[0]; if (lid == null) return null;
      const l = L(n.subgraph, lid); return l ? resolve(n.subgraph, l.origin_id, l.origin_slot, depth + 1) : null;
    }
    const key = n.properties?._key; return key ? [key, originSlot] : null;
  }
  let moved = 0;
  for (const { g } of graphs) {
    for (const n of g._nodes) {
      const key = n.properties?._key; const api = key && spec.api[key]; if (!api || n.subgraph) continue;
      const want = Object.entries(api.inputs).filter(([k, v]) => Array.isArray(v) && v.length === 2 && typeof v[1] === 'number');
      const cur = n.inputs.map((inp, idx) => ({ inp, idx, l: inp.link != null ? L(g, inp.link) : null })).filter(x => x.l);
      const plan = [];
      const used = new Set();
      for (const c of cur) {
        const o = resolve(g, c.l.origin_id, c.l.origin_slot);
        if (!o) { log.push(`fix: ${key} ${n.type}.${c.inp.name} origin unresolved`); continue; }
        const cands = want.filter(([nm, v]) => String(v[0]) === o[0] && v[1] === o[1] && !used.has(nm));
        const pick = cands.find(([nm]) => nm === c.inp.name) || cands[0];
        if (!pick) { log.push(`fix: ${key} ${n.type}.${c.inp.name} <- ${o} not in API`); continue; }
        used.add(pick[0]);
        if (pick[0] !== c.inp.name) plan.push({ c, name: pick[0] });
      }
      if (!plan.length) continue;
      // proper frontend calls, so autogrow / dynamic inputs update themselves
      for (const p of plan) { p.origin = [p.c.l.origin_id, p.c.l.origin_slot]; }
      for (const p of plan) { const idx = n.inputs.findIndex(i => i.name === p.c.inp.name); if (idx >= 0) n.disconnectInput(idx); }
      await new Promise(r => setTimeout(r, 30));
      for (const p of plan) {
        const idx = n.inputs.findIndex(i => i.name === p.name);
        if (idx < 0) { log.push(`fix: ${key} ${n.type} has no input ${p.name}`); continue; }
        if (Number(p.origin[0]) === -10) g.inputNode.slots[p.origin[1]].connect(n.inputs[idx], n);
        else g.getNodeById(p.origin[0]).connect(p.origin[1], n, idx);
        moved++;
        await new Promise(r => setTimeout(r, 30));
      }
      log.push(`fix: ${key} ${n.type} moved ${plan.map(p => p.c.inp.name + '->' + p.name).join(', ')}`);
    }
  }
  log.push(`fix: ${moved} links moved`);
  return log;
};
