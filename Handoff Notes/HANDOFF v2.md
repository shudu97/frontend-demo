# RiskMind Training Material — Handoff Note

Written 2026-11-07, from the chat that built the Session 1–3 outlines. Read this first in a new session. The chat is in Chinese, the file content is in English.

---

## 1. What this project is

RiskMind is an Agent + Plugin product for Market Risk. The training material is three sessions, about 45 minutes each, with 15–20 minutes of Q&A:

| Session | Topic | Date on the course page |
|---|---|---|
| Session 1 | RiskMind (Introduction) | November 12 |
| Session 2 | Agent | November 20 |
| Session 3 | Plugin | November 27 |

Audience: Senior Managers and Local Risk Managers. They know the business well but not necessarily AI terms.

**Session 1 is a video.** The user presents it live in a browser, beat by beat: Space plays from one beat to the next and then pauses, and the user talks at each pause. The voice-over version comes later. The video is a single HTML file; the final one is `ed0c760f-RiskMind_Session_1.html` (133.2 s, 43 beats).

After all videos exist, the user will add the course structure and the transitions between sessions. The user will also review every session's captions in detail.

---

## 2. Standing rules (the user set these; keep following them)

- **One slide at a time. Ask questions before writing.** Review one session at a time.
- **File content in English; conversation in Chinese.**
- **Keep the md and the published page in sync.** Render and check before each publish.
- **Cite official sources verbatim, with links** (Anthropic "Building effective agents", the ReAct paper arXiv 2210.03629, etc.). Exceptions: Harness and the old workflow slide don't need citations.
- **Never mention earlier attempts or failures.**
- **Never say RiskMind "replaces" anything.** RiskMind does not replace the Official Risk Report; Risk Managers still verify its output.
- **Give download links only when asked.** The user asked for a self-contained file once; see section 5.
- **If seconds differ between the script and the HTML, the real HTML wins.**
- **Spelling:** AiXel (not AIXel, not "Agent Serving"); "digitizes" (not "digitalizes"); "Judgement".
- "1 Product = 1 Plugin, 1 Metric = 1 Skill" is said only verbally, never written on slides.
- Audience-facing wording: "Dashboard" for outputs; for key-person risk, say "knowledge stays with the team when people change", never mention resignation directly.

---

## 3. Where things stand

### Session 1 — done, now in review

- The outline was restructured per video beat. Each slide has a table with columns **Beat · Visual · On-screen text · Caption · Reference**.
  - **Caption** = what the user says at that beat (taken from the video script; the user is revising it).
  - **Reference** = background for Q&A, not said unless asked. No information from the old outline was lost.
- Each slide has a full-scene screenshot, re-shot from the final HTML.
- The outline now matches the user's kept video script (Docs "RiskMind Session 1 — Video Script", rev 595; local copy `b8cd2004-RiskMind_Session_1___Video_Script.md`) and the final HTML.
- Slide structure (12 slides, 43 beats; times from the final HTML):

| Slide | Beats | Start |
|---|---|---|
| Cover and Course Structure | Cover, Course | 0.0 s |
| GRM AI Vision and Strategy (Why RiskMind Exists) | 1–5 | 5.4 s |
| AI Tools Landscape (Where RiskMind Fits) | 6–15 | 14.8 s |
| RiskMind Positioning | 16 | 56.2 s |
| Today vs. With RiskMind | 17–19 | 66.4 s |
| What RiskMind Is: Agent + Plugin | 20–23 | 76.7 s |
| How a Pipeline Runs | 24–25 | 84.5 s |
| Demo (placeholder) | 26 | 96.3 s |
| Why RiskMind | 27–29 | 97.7 s |
| From Proof of Concept to Production | 30 | 109.1 s |
| Expansion | 31–38 | 112.5 s |
| Key Takeaways (Three Things to Take Away) | 39–43 | 120.7 s |

- **Review plan, as the user stated it:** the user reviews the talk track beat by beat. The opening scenes (cover, course page, GRM AI Vision, up to the moment the axis appears) are **not** content the user speaks, so **the review starts at beat 6** (the axis appears, 14.8 s).
  - The AI Tools Landscape slide has **10 beats (6–15)**. I listed all 10 captions in the last turn, speech only. **The user has not yet given feedback on any of them. Start there.**

### Session 2 (Agent) and Session 3 (Plugin) — drafted in the old slide format, not yet converted

- Both are still in the **old slide-by-slide format**. They have **not** been converted to the beat tables that Session 1 uses.
- They still say **"Sensitivities"**. The video now says **"What-if Analysis"**; update the wording when each session is reviewed.
- Session 2 starts with `# Agent`; Session 3 starts with `# Plugin`.
- Session 3 status:
  - **Plugin Introduction** and **Skill Introduction** are drafted (old format).
  - **Skill Walk Through** and **MCP Introduction** are **on hold**.

**Open blockers for Plugin (the user said these two are the blocking points):**
1. **Shared Library**: the user said they now roughly know how it operates, but has not yet written it down for me. Shared knowledge sits in the plugins' parent folder `plugins/reference/`.
2. **Which parts of a Skill get extracted, and what remains**: the user said this is still not fully clear to them. Skill Walk Through and MCP Introduction wait on this skill restructure and a code check.

The agreed order was: finish the Plugin content first, then go back and build the Session 2 and Session 3 videos, then connect all three with course structure and transitions.

---

## 4. Facts the content depends on

- **RiskMind = Agent (built on the Claude Agent SDK) + Plugin (Skills + MCP).** 1 product = 1 plugin; 1 metric or analysis = 1 skill.
- **Skill Tooling:** AutoEval → AutoSkill → AutoEvolution.
- **Teams (current video):** *Local Market Risk* (AI Champions write Skills) and *Market Risk AI × AiXel* (build the Agent and the data connection, and support Local Market Risk). The old name was "Agent Serving Team (Enterprise AIXel)". The user wrote AiXel; I flagged the old-name mapping but the user has not explicitly confirmed it.
- **Landscape axis (the "AI Tools Landscape" slide):** Chat / Augmented LLM | dashed line | Agentic Systems. Prompt Chaining and Autonomous Agent are *patterns* (dashed), not products. DocuMind = workflow; RiskMind = agent; RBC Assist Pro = augmented LLM. Colours: blue = Vertical, RBC yellow = Horizontal. The framing and definitions come from Anthropic's "Building effective agents"; ReAct supports the agent loop. Quotes with source links are kept in the Reference column.
- **Today vs. With RiskMind:** shown on one automation axis (All Manual / Today / With RiskMind / Fully Automatic) plus an effort bar of three segments: **Design · Execution · Judgement**. Judgement stays with the Risk Manager and does not shrink. With RiskMind, Execution shrinks a lot, Design grows (a one-time cost), and the left part of the bar is "Saved Effort" (about half). The Risk Manager's role shifts from doing the analysis every time to designing it once and verifying it every time.
- **Pipeline:** Get Data, Analyze, Build Dashboard run as **Scripts**; Write Comments / Write Answer are done by the **LLM**. Principle: **Numbers from Scripts, Words from the LLM.**
- **Closing page:** Market Risk · RiskMind · AiXel.

---

## 5. Open items

- **Demo caption (beat 26)** is empty. The Demo frame is a placeholder until the recording exists; check whether the real report in the recording needs masking.
- The script's to-do list mentions a **Session 2 preview card at the end**. It does not appear in the current video or the outline. The user said they will do it when connecting the videos.
- **Course structure** now exists as the first two beats (Cover, Course). The course page lists the three session dates. The user will finalize it later.
- AiXel / "Agent Serving" naming: not yet confirmed (section 4).
- Glossary and time-budget items from earlier planning are not done.
- The script's own summary line says the animation is about 116 s; the real video is 133.2 s. The HTML is authoritative.
- Beats 40–42 visuals and the three new beats' captions were written from the script and checked against screenshots only for the cover, course page, closing page and the Take Away page. Other scene screenshots were re-shot with the same method but not all individually reviewed.

---

## 6. Files and links

**Published pages** (private to the user; the Artifact tool updates them in place via `url`):
- Session 1 outline: https://claude.ai/artifact/FZYXQf3QTiHxwkbDAnWumF (v92, current)
- Session 2 outline (old format): https://claude.ai/artifact/LkLWhxi1SCE4WTVqAYG1Wz
- Session 3 outline (old format): https://claude.ai/artifact/7t6EW7JbvMi1MWbWcHT1SL
- Video script doc (Claude Docs): https://claude.ai/artifact/64pG6b9JRMpeXa4JwrZEtD (project 29060cbf-457a-46b9-be58-5e0045838dfe)

**Files that survive in this container** (the rest of the working directory was lost when the container was replaced):
- `/mnt/user-data/outputs/RiskMind_Session1_Outline.html` — the self-contained Session 1 outline (screenshots embedded), current as of v92. This is the most complete copy of Session 1. The markdown source (`RiskMind_Session1.md`) and the scene screenshots were **not** kept as files.
- Attachments from the user: the final video HTML `ed0c760f-RiskMind_Session_1.html` (earlier versions `cd5fc608`, `e5393959`, `8fdafaed`, `39111125` are superseded), the video script `b8cd2004-RiskMind_Session_1___Video_Script.md` (rev 472 + edits; the newer Docs rev 595 adds the Cover / Course / closing beats and is the latest), and older outline md versions (`521abf38`, `77f25d26`, `252520b5`, `5481f257`).
- **Session 2 and Session 3 markdown sources are gone from disk.** The published pages above are the surviving copies of their content. To continue them, read the artifact (Artifact `read`) and rebuild the md from it.

**How to rebuild the Session 1 md if needed:** the self-contained HTML holds the tables as `<table>` rows. Extract the five columns per beat; images are base64 `scenes/*.jpg`.

**Technical method used (for re-capturing screenshots):** Playwright Chromium; open the video HTML with `?export=1`; call `window.renderAt(t)` and take a screenshot at 1920×1080, then resize to 1280×720 JPEG. DM Sans is routed locally. Screenshot times are "end of the scene" (next beat start minus ~0.15 s). Scene end times used: intro 14.65, landscape 56.0, positioning 66.25, today 72.45, with RiskMind 76.55, agent+plugin 84.35, pipeline 96.15, demo 97.55, why 108.95, PoC→production 112.35, expansion 120.55, takeaways 131.05, closing 133.0; cover at t=0.1, course page at t=2.15.

**Beat start times:** use the "Beat" column in the Session 1 outline as the source of truth (they match the final HTML: Cover 0.0, Course 2.2, beat 1 at 5.4, beat 6 at 14.8, beat 43 at 131.2, end 133.2).

---

## 7. What to do next, in order

1. **Review Session 1, beat by beat, starting at beat 6.** Ask the user for their changes beat by beat; edit the Caption and Reference; keep the page in sync.
2. **Plugin content:** get the user's description of the Shared Library and of what is extracted from a Skill; then finish Plugin Introduction and Skill Introduction, and convert them to beat tables.
3. **Session 2 (Agent):** convert to beat tables, review with the user, change "Sensitivities" to "What-if Analysis".
4. **Session 3 (Plugin):** same, after step 2.
5. **Demo caption** once the recording exists.
6. When all three videos exist: course structure and transitions between sessions.
