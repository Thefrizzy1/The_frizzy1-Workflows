# How to write a script for the Story Creator

The Story Creator turns a script into one long video: one line = one scene. Every scene gets a picture (Qwen Image,
always the same main character), the picture moves and speaks (MiniMax H3), a narrator reads the story lines in one
voice, music runs under it, and the scenes are joined.

**Let a big chatbot write it.** Paste the prompt at the bottom into ChatGPT, Claude or Gemini with your idea. The
workflow still has a small built-in writer (*Write the scenes for me*, the 8B Qwen text encoder), but it ships switched
off: in the tests it wrote short, vague lines and dropped how side characters look, so a rabbit turned into a second fox.
A detailed script from a big model got 10 of 12 scene pictures right on the first try.

## The format
```
WORLD: <one line: the look of the whole story - place, season, light, style>
[camera] <what we see> || <what the narrator says>
[camera] <what we see> || Name: <what the character says>
[continue] [camera] <what we see> || <what we hear>
```
Think of the tags as little embeddings the workflow reads:

| Tag | What the workflow does with it |
|---|---|
| `WORLD:` (first line, optional) | The look of the whole story, put in front of every scene. Not a scene. Without it the 8B writer makes one from your scenes. |
| `[camera]` | Goes into the picture and the video prompt: `[wide, tracking shot]`, `[close-up, slow push-in]`, `[low angle]`, `[the camera follows the wing]`. |
| `what we see` | The scene picture and the motion. This is what makes or breaks the video (rules below). |
| `\|\| plain text` | The **narrator** reads it, off screen, one voice for the whole story; the scene is made without voices. |
| `\|\| Name: words` | That **character says it on screen** (mouth moves). |
| nothing after `\|\|` | A silent scene with just its own sound. |
| `[continue]` | Transition instead of a cut: this scene's clip ends on the next scene's picture. Only where the action really flows on (walking out of the forest onto the lake). Cuts are the default. |

Scene length follows the line: every scene gets as long as its words need (3-9 s).

## The rules that make the picture match the words
1. **Name every character with their full look, in every line they're in** - "Clover, a small white rabbit in a green
   knitted hat", not just "Clover". Only the main character has a picture; everyone else exists only in your words.
2. **Say the important things exactly**: "the path ends in a clear fork: two separate paths, one curving left and one
   curving right, a crooked wooden signpost with two arrows" - not "the path splits".
3. **Write the action from start to end**: "Pip holds the compass out at arm's length, the needle swings and settles on
   the left path, he points left" - movement, not a pose. "Pip looks at the sky" gives a still picture.
4. **Say where they are, every line** ("at the edge of the frozen lake", "behind the big grey rock by the river") so the
   places connect.
5. **Faces**: worried, laughing, wide-eyed - H3 animates what you name.
6. **Keep what is said short**: up to about 12 words narrator, about 10 words dialogue.
7. **More talking, less narrator**: about two thirds dialogue feels like a film; the narrator for jumps in time or place.
8. **Avoid over-the-shoulder shots and characters cut off at the frame edge**: in the tests the main character appeared
   twice, or two characters melted into one.

## Before / after (the same scene)
- Before: `In the snowy pine forest, the path splits in two, Pip and Clover stop and look at both ways || Soon the path split in two.`
- After: `[wide shot from behind] In the snowy pine forest the path ends in a clear fork: two separate paths, one curving away to the left and one curving away to the right, a crooked wooden signpost with two arrows in the middle; Pip, the small orange fox in the blue scarf, and Clover, the small white rabbit in the green hat, stop in front of it || Clover: Oh no. Two paths! Which one?`

## Prompt for any chatbot (copy, fill in, paste)
```
Write a script for an AI story video as a scene list, one scene per line, nothing else.
Main character: <who, exactly what they look like>
Other characters: <name: exact look, for each>
Story idea: <one or two sentences>
Number of scenes: <about 12 per minute>
Format:
- First line: WORLD: <the look of the whole story: place, season, light, style>
- Every other line: [camera] what we see || what we hear
- [camera]: the shot and its movement, e.g. [wide, tracking shot], [close-up, slow push-in], [low angle].
  No over-the-shoulder shots, no characters cut off at the edge of the frame.
- "what we see": where we are, every character in the shot with their FULL look written out, the important objects
  exactly (how many, where), and the action from start to end with clear movement and faces. 40-70 words.
- "what we hear": either the narrator's sentence (max 12 words) or  Name: what they say  (max 10 words).
  About two thirds of the lines are characters talking.
- Add [continue] in front of a line only when that scene flows straight into the next one without a cut.
- A beginning, a problem and a happy ending. No numbering, no titles, no blank lines.
```

A full 58-line example (about 5 minutes) is in [samples/example_script_5min.txt](samples/example_script_5min.txt).
