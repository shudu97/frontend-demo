---
name: riskmind-video-style
description: "How the user wants RiskMind videos built and checked — visual style, design dislikes, language, verification habits, .render tools and pitfalls"
metadata:
  node_type: memory
  type: feedback
  originSessionId: cf1063c6-174a-4cab-b254-fa4bdc1d0640
  modified: 2026-11-15T00:00:00.000Z
---

**Style:** on-screen text English; big text Title Case with no full stops, small text sentence case; DM Sans (DM Mono for code; in SVG set mono as a style or tspan, not an attribute); blue palette only (no green/purple/teal; deck colours get converted). One exception: horizontal = RBC yellow #FCF5DA/#DDBB4C (text #8A6D12), vertical/RiskMind = blue #DFEBFC/#1C5BB5 (accent #1A73E8), the same in every session. Diagrams in Anthropic "Building Effective Agents" style; one icon per component; precise alignment and symmetry (the user spots misalignment); no idle holds. Reply in Chinese; talk tracks in English.

**Design preferences (learned 2026-10 from many rejections):**
- Every screen change carries an element over; avoid hard cuts. A plain fade is acceptable only as a placeholder when the user says so (e.g. Session 2's course page → first scene, 2026-11-12).
- Not PowerPoint-like: no big title + bullet lines, no filled boxes, no tables, no title bars before a scene. The user dislikes bullets (prefers a short paragraph) and centred multi-line text blocks (left-align them).
- Minimal on-screen text: anything said aloud stays off the slide.
- "分清主次": the content sentence beats its label; don't stack a header over new content — move it to a corner.
- Real/source imagery (the user's own slide images, logos) beats self-drawn sketches or emoji icons.
- Use the user's original wording on screen; show the real mechanism rather than an abstract list.
- Carry-overs: the box forms in place and the label slides in, then both move together; hide the source label the moment its copy appears; a box is never narrower than its word; when a word swaps, keep the first whole until halfway.

**Why:** the user presents live and iterates frame by frame; they called out non-smooth transitions, misalignment and "too PPT" pages repeatedly.

**How to apply:**
- Back up before every edit (`.render/before-*.html`, Session 2 `s2-before-*`); after edits, check stills AND live playback with real key presses; say what was and wasn't verified; tell the user to Cmd+R the open page (a stale page once looked like a stop-skipping bug, 2026-11-10).
- Tools in `.render/`: `stills.mjs <abs html> <new outdir> <t…>` (needs `window.renderAt`), `livekeys.mjs`, `tval.mjs`, `alltext.mjs`, `errs.mjs`. Playwright must use `executablePath: ~/Library/Caches/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-mac-arm64/chrome-headless-shell` (the default 1248 build isn't installed). Convert stills with `sips -s format jpeg -z 720 1280` (no PIL). Use Python instead of long grep/ugrep regexes ("exceeds complexity limits").
- Write each still batch into a new folder: a command containing `rm -f $DIR/*` is blocked by the safety check and the whole command (edits included) doesn't run.
- Never append a `// comment` via string replace without a newline after it — it swallowed the next statement more than once.
- Hide a scene container with `display:none`, not `visibility:hidden`; every element a later segment adds to a shared container must be hidden before that segment starts; test navigating backwards (→ then Home/←), not just forward.
- "renderAt is not a function" in a stills run means the page threw on load — usually a const used before its definition, or a duplicate `const` name (Session 2 already has `LOGO_RM`).
- Arrow keys and held keys: → / ← always land on a stop and stop; `e.repeat` acts once (fixed in both sessions 2026-11-09).
