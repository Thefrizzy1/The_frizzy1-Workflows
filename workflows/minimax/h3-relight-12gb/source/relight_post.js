  // re-run the group layout with the final node sizes (nested subgraph nodes grow after the first layout and overlapped)
function relayout(g, MAXH) {
for (const n of g._nodes) { const c = n.computeSize ? n.computeSize() : n.size; n.size = [Math.max(n.size[0], c[0]), Math.max(n.size[1], c[1])]; }
  const groups = [...g._groups];
  const member = new Map(groups.map(G => [G, []]));
  for (const n of g._nodes) {
    const G = groups.find(G => n.pos[0] >= G.pos[0] && n.pos[0] < G.pos[0] + G.size[0] && n.pos[1] >= G.pos[1] && n.pos[1] < G.pos[1] + G.size[1]);
    if (G) member.get(G).push(n);
  }
  const rows = [];
  for (const G of [...groups].sort((p, q) => p.pos[1] - q.pos[1] || p.pos[0] - q.pos[0])) {
    const r = rows.find(r => r.y === G.pos[1]); if (r) r.gs.push(G); else rows.push({ y: G.pos[1], gs: [G] });
  }
  const PAD = 30, GAP = 70, HEAD = 60;
  let y = 0, maxX = 0;
  for (const row of rows) {
    let x = 0, rowH = 0;
    for (const G of row.gs.sort((p, q) => p.pos[0] - q.pos[0])) {
      const nodes = member.get(G).sort((p, q) => p.pos[0] - q.pos[0] || p.pos[1] - q.pos[1]);
      let cx = x + PAD, cy = y + HEAD, colW = 0, maxY = cy;
      for (const n of nodes) {
        const h = n.size[1] + 34;
        if (cy > y + HEAD && cy + h > y + HEAD + MAXH) { cx += colW + 40; cy = y + HEAD; colW = 0; }
        n.pos = [cx, cy]; cy += h + 10; colW = Math.max(colW, n.size[0]); maxY = Math.max(maxY, cy);
      }
      const w = Math.max(cx + colW + PAD - x, 340), h = Math.max(maxY - y + 10, 160);
      G.pos = [x, y]; G.size = [w, h];
      x += w + GAP; rowH = Math.max(rowH, h); maxX = Math.max(maxX, x);
    }
    y += rowH + GAP;
  }
  if (g.outputNode) g.outputNode.pos = [maxX + 40, 0];
}

// After buildUltimate("The_frizzy1_h3-relight-12gb_v1.0.0"): readable labels for the sockets the builder could not name
// (the light text comes from a text node outside, not a Load node), then save again.
async function relightPost(NAME) {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const top = app.graph, MN = top._nodes.find(n => n.subgraph), MS = MN.subgraph, log = [];
  const ren = (sg, name, label) => { const si = sg.inputs.find(i => i.name === name); if (si) { sg.renameInput(si, label); log.push(`${sg.name}: ${name} -> ${label}`); } };
  ren(MS, 'string_b', 'Light text (master prompt)');
  await sleep(100);
  for (const w of MN.widgets) { const i = MN.inputs.find(i => i.name === w.name); if (i && i.label) w.label = i.label; }
  for (const n of MS._nodes) {
    if (!n.subgraph) continue;
    const sg = n.subgraph;
    for (const si of sg.inputs) {
      // name each nested input after the node it comes from in the main subgraph
      const inp = n.inputs.find(i => i.name === si.name);
      const l = inp && inp.link != null && (MS.links.get ? MS.links.get(inp.link) : MS.links[inp.link]);
      let src = l && (l.origin_id === -10 ? null : MS.getNodeById(l.origin_id));
      let label = src ? (src.title || src.type) : (l ? (MS.inputs[l.origin_slot]?.label || MS.inputs[l.origin_slot]?.name) : null);
      if (label && label !== si.name) { sg.renameInput(si, label); inp.label = label; }
    }
    log.push(`${sg.name}: ${sg.inputs.map(i => i.label || i.name).join(' | ')}`);
  }
  relayout(MS, 1100);
  for (const n of MS._nodes) if (n.subgraph) relayout(n.subgraph, n.subgraph.name.startsWith('Long') ? 1300 : 1100);
  // top level: the three inputs stacked in one column on the left, the main node, the Result on the right
  const byT = t => top._nodes.find(n => n.title === t);
  const [vid, sph, txt] = ['Your video (24 fps)', 'Light sphere (from the preset)', "Light: the preset's master prompt"].map(byT);
  vid.size = [420, 470]; sph.size = [420, 470]; txt.size = [880, 230];
  vid.pos = [0, 0]; sph.pos = [460, 0]; txt.pos = [0, 540];
  MN.pos = [960, 0];
  const save = byT('Result'); save.pos = [960 + MN.size[0] + 90, 0];
  const li = MN.inputs.find(i => i.name === 'string_b');
  if (li) li.label = 'Light text (master prompt)';
  top.setDirtyCanvas(true, true);
  const wf = top.serialize();
  wf.extra = Object.assign(wf.extra || {}, { ds: { scale: 1, offset: [60, 60] } });
  log.push('top: ' + top._nodes.map(n => `${n.title} @${n.pos.map(Math.round)} ${n.size.map(Math.round)}`).join(' | '));
  const res = await fetch(`/api/userdata/${encodeURIComponent('workflows/' + NAME + '.json')}?overwrite=true`, { method: 'POST', body: JSON.stringify(wf, null, 1) });
  return { status: res.status, widgets: MN.widgets.map(w => w.label || w.name), log };
}

// Second pass on the SAVED file: node sizes as ComfyUI computes them on load (autogrow inputs, nested node labels), then the
// group layout again, so nothing overlaps for the user. Keeps the first-load view.
async function relightRelayout(NAME) {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const wf0 = await (await fetch(`/api/userdata/${encodeURIComponent('workflows/' + NAME + '.json')}?t=${Date.now()}`)).json();
  await app.loadGraphData(wf0, true, true, NAME + '.json');
  await sleep(2500);
  const MS = app.graph._nodes.find(n => n.subgraph).subgraph;
  relayout(MS, 1100);
  for (const n of MS._nodes) if (n.subgraph) relayout(n.subgraph, n.subgraph.name.startsWith('Long') ? 1300 : 1100);
  const wf = app.graph.serialize();
  wf.extra = Object.assign(wf.extra || {}, { ds: wf0.extra.ds });
  const res = await fetch(`/api/userdata/${encodeURIComponent('workflows/' + NAME + '.json')}?overwrite=true`, { method: 'POST', body: JSON.stringify(wf, null, 1) });
  return res.status;
}
