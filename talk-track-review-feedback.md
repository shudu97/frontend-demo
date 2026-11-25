---
name: talk-track-review-feedback
description: "How the user wants talk-track reviews done (one beat at a time, Chinese, no translating their explanations into the script)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: f0292f1c-48c6-4dd8-aad2-91944a885ab1
  modified: 2026-11-15T20:20:18.333Z
---

When reviewing RiskMind talk tracks: go one beat at a time, explain in Chinese, give the suggested English version, and write to the md only after the user approves that beat.

What the user writes to explain their intent (e.g. "the key word is automatic", "one round should mean the LLM thinks once") is guidance for me, not text to put into the talk track. Use it to shape the wording; don't translate it in.

Style they want: spoken, smooth, short sentences, few colons (colons feel too written), non-technical for risk managers, matching what's on screen. Use "product" for products and keep "tool" only for the LLM's tools. Phrases they find awkward to say: "walk you through", "sum it up" (they prefer "walk through", "summarize it"). They also dislike addressing the audience as "you" a lot; the audience is broader than Local Market Risk, so avoid "you all know…".

Since 2026-11-10 the user often edits the md themself: then I give suggested sentences in chat instead of writing the file (an editor left open would overwrite my changes), and when they say it's done I sync once and only list grammar slips. Tongue-twisters to avoid: clauses like "what changes is how it gets done", "gives you back", "happens on every run", "tested it", "Skill sets" (heard as skillset); repeated "and", and saying the same point several times.

**Why:** they corrected me twice on 2026-11-07/08 for copying their explanations into the script, and said reviewing everything at once was too much.
**How to apply:** for each beat: visual summary → numbered issues → suggested version → wait for OK → edit md (back up to .render/ first). See [[riskmind-memory-location]].
