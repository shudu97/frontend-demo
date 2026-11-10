# RiskMind Session 1 交接文档

给接手的 Claude session 看。目标：**在一个 session 里同时维护视频、讲稿、Outline 和提词器**，不再分三个 session。

写于 2026-11-07。项目文件夹：`~/Downloads/RiskMind Session 1 Video/`

---

## 1. 和用户合作的方式

- **用中文回复**。屏幕上的文字和 talk track 用英文。
- 用户在现场边放边讲，会逐帧看效果，对对齐、留白、转场是否顺滑都很敏感。改完要截图给用户看（SendUserFile），并说清楚检查了什么、没检查什么（比如"只看了静止帧，没完整播放"）。
- 改动较大或涉及设计时，先出方案再动手。用户经常说"先别动手，先说说"。改动小、意思明确时直接改。
- **每次改 HTML 前都要备份**：`cp "RiskMind Session 1.html" .render/before-<名字>.html`
- 每次改完，在记忆文件 `~/.claude/projects/-Users-shuangdu/memory/riskmind-session1-video.md` 末尾追加一行，写明改了什么、关键数值和备份文件名。

---

## 2. 文件和它们的关系

**历史上的顺序**（用户说明）：先和用户确认 Outline（规划）→ 按 Outline 做视频 → 按做出来的视频写讲稿 → 最后用讲稿和视频回头更新 Outline。视频做的过程中总会和最初的 Outline 有出入，所以 Outline 的最终版是**按讲稿和 HTML 整理出来的定稿**，再拿去生成提词器。

**现在的状态**：视频已经做完，进入修改阶段。所以每次改动的方向是：

```
RiskMind Session 1.html            ← 视频本身（最终以它为准）
        │  ① 改完视频
        ▼
讲稿 (claude.ai Doc，中文画面描述 + 英文 talk track)   ② 按视频同步
        │     └─ RiskMind Session 1 — Video Script.md   ← 讲稿的本地副本
        ▼
RiskMind_Session1_Outline.html     ③ 按讲稿和视频同步（英文 + Reference + 每场截图）
        │
        ▼  ④ python3 -I build_prompter.py
RiskMind Session 1 Prompter.html   ← 提词器（演讲时用）
```

如果用户要**新加一段内容**（比如 Session 2 预告卡），可以沿用历史顺序：先在 Outline 里和用户把这一段的内容定下来，再做视频，然后按做出来的结果写讲稿，最后回头把 Outline 改成和讲稿一致。

| 文件 | 是什么 | 怎么改 |
|---|---|---|
| `RiskMind Session 1.html` | 演示视频，单文件 HTML，约 1.3 MB，图片都嵌成 data URI | 直接改代码（见第 4 节） |
| 讲稿（claude.ai Doc） | https://claude.ai/artifact/64pG6b9JRMpeXa4JwrZEtD ，每个断点一行：断点 · 画面（中文）· On-screen text · Talk track，外加 Overview、各节引言、Production notes、待做 | 用 docs 连接器编辑（见第 5 节） |
| `RiskMind Session 1 — Video Script.md` | 讲稿的本地副本，2026-11-07 时与 Doc 逐字一致 | Doc 改完后重新导出或同步 |
| `RiskMind_Session1_Outline.html` | 英文版：12 张场景卡，每张有截图（共 15 张，data URI）和一张表：Beat · Visual · On-screen text · Caption · Reference | 直接改 HTML（见第 6 节） |
| `build_prompter.py` | 把 Outline 的 Caption 和 Reference 复制进提词器 | `cd` 到项目文件夹后运行 `python3 -I build_prompter.py` |
| `RiskMind Session 1 Prompter.html` | 提词器：打开演示窗口、同步断点、显示讲稿 | 不要手改，用脚本生成 |
| `README.md` | 用户写的提词器使用说明 | 一般不用改 |
| `RiskMind Session 2.html` | Session 2 视频，**这次不用管**。Session 2 只有这个 HTML，没有讲稿、Outline 和提词器；改动记录在记忆文件 `riskmind-session2-video.md` | — |
| `.render/` | 备份（`before-*.html`）、截图输出、检查工具 | — |

**讲稿和 Outline 的分工**：讲稿 Doc 是视频的详细记录，画面描述用中文，最贴近 HTML 的实际效果；Outline 是给用户审阅和生成提词器用的英文定稿，多了 Reference 和截图。两者内容基本重复，所以每次改动都要同步两份。这是用户目前的习惯，不要自作主张合并；如果用户觉得麻烦，可以建议简化。

---

## 3. 每次改动的标准流程

1. 备份 HTML，然后改 HTML。
2. 检查：
   - 用 `node .render/errs.mjs "$PWD/RiskMind Session 1.html"` 看页面有没有报错（没输出就是没报错）。
   - 用 `stills.mjs` 截相关时刻的图，自己看一遍，再发给用户。
   - 如果停顿点变了，用 `tval.mjs` 打印 `BEATS` 和 `DURATION`。
3. **同步讲稿 Doc**：改对应行的画面描述、On-screen text 和 Talk track。如果断点时间变了，所有后续行的时间标签都要改。
4. **同步 Outline**：内容和 Doc 一致（英文）。画面变化明显时，更新那一场的截图。
5. **重新生成提词器**：`python3 -I build_prompter.py`，应该输出 `12 scenes, 45 beats (Cover, Course, 1 … 43)`。断点数变了，这行会跟着变。
6. 同步本地的 `Video Script.md`。
7. 在记忆文件里追加记录。

**断点对齐规则**：视频里每按一次 → 走一段。讲稿和 Outline 每段一行，第一行 `Cover` 是 0 秒时静止显示的封面。现在是 45 行：Cover、Course、1–43；视频有 43 个停顿点（`STOPS`）。行数必须等于停顿点数 + 2，否则提词器会显示黄色警告。

**时间标签规则**：每行的 "N · Xs" = 这一段**开始播放**的时刻，也就是上一个停顿点。提词器不读这个时间，只按行的顺序对齐，但讲稿里要保持正确。

---

## 4. 视频 HTML 的结构

### 时钟和停顿
- 一个全局时钟 `T`。`window.renderAt(t)` 渲染第 t 秒的画面。按 Space 播到下一个停顿点；← → 在停顿点之间跳。
- 最外层：`function render(t){S1.render(t-COVER);S0.render(t);renderMain(t-COVER-INTRO);}`
- `COVER = S0.END = 3.2`，`INTRO = S1.END = 12.3`。
- `BEATS = [...S0.BEATS, ...S1.BEATS+COVER, ...BEATS_MAIN+INTRO+COVER]`，`STOPS = BEATS 排序`。
- 现在 `DURATION = 133.2`，第一个停顿在 2.2（课程页）。

### 各场景模块（都是 IIFE，各自画在一个 `<svg id="sN">` 里）

| 模块 | 内容 | 全局时间 |
|---|---|---|
| `S0`（s0） | 封面（照 deck 标题页重画）→ 课程页（MCCR AI Learning Modules，三站进度条）。封面的三根弧线并成一根、拉直，变成进度条；RBC 盾牌从课程页标题飞到 GRM 那一行 | 0–3.2，停顿点 2.2 |
| `S1`（s1） | GRM AI Vision 和两条 strategy → Horizontal/Vertical 层级图 → Tesla / F1 比喻 | 3.2–15.5 |
| `S2`（s2） | 一根轴（LLM Decides the Next Step）：RBC Assist Pro、Prompt Chaining、Autonomous Agent、DocuMind、RiskMind，黄蓝上色，"complement, not a competitor"。注意 S2 有自己的跳空映射 `GAPS` / `s2global` / `s2local` | 15.5–57.2 |
| 定位页（在 `renderMain` 和 `fx` 图层里） | `[logo] RiskMind is An Agent That …`，Notion 风格的滚动标签 → 两行 + 台阶时间轴 | P0 = 57.2 |
| `S4`（s4） | Today / With RiskMind 卡片、自动化轴、Design / Execution / Judgement 条形、手电筒光、Saved Effort | T0 = 66.4 |
| `S3`（s3） | What RiskMind Is：Agent + Plugin | X0 = 76.7 |
| `S5`（s5） | 4b：一次 pipeline 怎么跑；Script / LLM 标签；"Numbers from Scripts, Words from the LLM" | X1 = 84.5 |
| Demo 占位 | 虚线框 + 播放图块 | D0 = 96.3 |
| `S6`（s6、s7） | Why RiskMind：Improves Efficiency / Ensures Consistency / Digitizes Knowledge，收成一句总结回到台阶时间轴 | W0 = 97.7，X8 = 109.1 |
| `S8`（s8） | Expansion（Plugin 网格、团队、扩展）→ 收拢转场（全部落进 Agent，Agent 变 RiskMind）→ Key Takeaways（三条，每条一个前面画面的缩影）→ 结束页（Market Risk · RiskMind · AiXel） | X9 = 112.5，结束页停顿 131.2 |

- `fx` 图层画的是跨场景移动的元素：RiskMind 的 logo 和名字、Risk Insight、RiskMind 框等。
- S8 的图层用 viewBox 放大了 1.05 倍，收拢转场时会恢复到整页。
- 嵌入的图片常量：`RBC_LOGO`（在 S1 内，S0/S8 通过 `S1.logo.getAttribute('href')` 拿）、`IMG_TESLA`、`IMG_F1`、`IMG_AIXEL`（在 S8 内），以及 `S2.logo` / `S2.logoDM`（RiskMind / DocuMind 的 logo）。素材原件在 `.render/assets/`。

---

## 5. 讲稿 Doc 的编辑方法

- Doc id：`29060cbf-457a-46b9-be58-5e0045838dfe`，根节点 `4c0ec995-28c2`，最新 rev 595。
- 读：`mcp__…__read`，参数 `ref {"object":"node","id":"4c0ec995-28c2"}`，`container {"kind":"project","id":"29060cbf-…"}`，`engine "prose"`。整篇会超过输出上限，会存成文件，用 `jq -r '.[].text'` 取出后再用 Python 解析。只看改动可以加 `payload {"kind":"view","sinceRev":N}`。
- 写：`mcp__…__update`，`engine "prose"`，`payload.ops`：
  - 改字：`{"op":"replace","target":{"kind":"find","text":"原文"},"with":{"as":"text","from":{"kind":"inline","content":"新文"}}}`
  - 加行：`{"op":"insert","target":{"kind":"blocks","ids":["mvehed4ek7e.<行id>"]},"side":"after","source":{"as":"blocks","from":{"kind":"inline","content":[{"type":"row","content":[4 个 cell]}]}}}`
  - **id 必须写全**，带 `mvehed4ek7e.` 前缀，读出来的 `.12345` 是简写。
  - 一次调用可以放很多 op，按顺序执行。
- Doc 会提示"takes suggestions"：用户只说"润色/改得更好"这类话时要用建议模式。明确的修改直接改。

---

## 6. Outline 的编辑方法

- 12 个 `<article class="slide">`，每个是一场；标题在 `<h3>`，副标题在 `<span class="subtitle">`。
- 每行：`<tr><td>{label} · {t}s</td><td>Visual</td><td>On-screen text</td><td>Caption</td><td>Reference</td></tr>`。`build_prompter.py` 严格按这个格式解析：标签后面必须正好 4 个 `<td>`；Reference 里每条用 `•` 开头、`<br>` 分行。
- Caption 就是 talk track，会显示在提词器上。
- 截图是 `<figure class="scene"><img src="data:…">`，画面大改时用 `stills.mjs` 重截、转 base64 替换。
- 文件很大（截图），用 Python 按 `<tr>` 定位替换，不要整体重写。

---

## 7. 检查工具（`.render/`）

都用 Playwright，浏览器路径写死为 `~/Library/Caches/ms-playwright/chromium_headless_shell-1243/…`。文件参数要用**绝对路径**。

| 命令 | 用途 |
|---|---|
| `node .render/stills.mjs "<abs html>" <新文件夹> <t1> <t2> …` | 截指定时刻的图（每次用新文件夹） |
| `node .render/tval.mjs "<abs html>" "<JS 表达式>"` | 在页面里求值，比如 `BEATS`、`DURATION`，或者 `renderAt(t)` 之后量元素位置 |
| `node .render/errs.mjs "<abs html>"` | 打印页面加载时的报错 |
| `node .render/alltext.mjs "<abs html>"` | 在每个停顿点渲染并收集所有文字，用来对照讲稿的 On-screen text |
| `node .render/livekeys.mjs "<html>" <out.png> wait1500 Space …` | 模拟真实播放和按键（先 `wait1500` 等页面加载） |
| `sips -c H W --cropOffset Y X in.png --out out.png` / `sips -Z 800` | 裁图、缩图，方便看细节 |

已知的坑：
- 一条命令里如果有 `rm -f $DIR/*` 会被安全检查拦下，整条命令都不执行。每次截图用新文件夹。
- `stills.mjs` 报 "renderAt is not a function" = 页面加载时出错了，先跑 `errs.mjs`。常见原因是 const 在定义前被使用。
- 往某一行末尾加 `// 注释` 时，后面要换行，否则会吞掉下一行代码。

---

## 8. 风格规则（用户反复强调过）

- 屏幕文字用英文；大字每个单词首字母大写，不加句号；小字只大写句首。字体是 DM Sans。
- 只用蓝色系。唯一例外是 Horizontal 用 RBC 黄（底 #FCF5DA、边 #DDBB4C、字 #8A6D12），Vertical 和 RiskMind 用蓝（#1C5BB5，强调词 #1A73E8）。
- 多行文字左对齐；卡片里的描述居中。
- 换屏要带一个元素过去，不要硬切或单纯淡入淡出。动作要连贯，不能中途停顿（分两段的动画要用同一条时间曲线）。元素飞行距离不要太远。
- 不要像 PPT：避免一行大标题加几行字、填色方框、表格。
- 三个转场页（GRM AI Vision、Positioning、Key Takeaways）的一行阶段统一：logo 高 108，名字 60.5px（84×0.72），后面那句 50px，中间空 44；RBC 盾牌和文字之间留 32。
- 措辞：不说 RiskMind "replaces" 任何东西；用 Judgement（不是 Verification）、Scripts（不是 code）、Digitize（不是 digitalize）、Business Plugin（Session 2）、AiXel（不是 AIXel）。
- 尽量少放屏幕文字，能口头讲的就不放上去。

---

## 9. 当前待办（2026-11-07 核对后）

**讲稿 Doc 里过时的地方**（表格本身和视频吻合，问题都在表格外面）：
1. Overview："动画约 116 秒"改成 133 秒；讲稿字数和时长要重算；内容列表补上封面、课程结构、Key Takeaways 和结束页。
2. 核心信息和 4b 引言："数字全部由代码算"改成由脚本算；4b 引言里的 "Direct Answer" 改成 "Answer in Chat"。
3. Today 那一节的引言："Operational Manual"改成 Standard Operating Procedure。
4. Intro 引言：去掉 "GRM AI Vision:" 的冒号；补一句封面和课程两行。
5. 时间标签："课程 · 2.2s" 应为 0.0s，"1 · 3.2s" 应为 2.2s（按"开始播放时刻"的规则）。Doc、Outline 和 md 都要改。
6. 待做里"补上第 20 段讲稿"现在是第 26 段（Demo）。

**Outline**：
7. 第 23 段的 Caption 有错字："or a answer in chat in chat" 应为 "or an answer in chat"。改完要重新生成提词器。
8. 检查 Outline 里的截图是不是最新的画面（Key Takeaways、结束页、收拢转场都是最近改的）。

**内容上的待办**（来自讲稿的"待做"）：
9. Demo 录好后，替换第 26 段的占位画面并补讲稿；确认录屏里的真实报告是否需要脱敏。
10. Session 2 预告卡：课程结构已做，预告卡没做，现在片尾是结束页（Market Risk · RiskMind · AiXel）。要不要加，问用户。
11. 更新 deck outline（PPT，不在这个文件夹里）：去掉 "replaces the existing risk report"，Expansion 那页按视频的版本调整。

**提醒**：
12. Session 2 没有讲稿、Outline 和提词器。如果用户之后想给 Session 2 也补上，按历史顺序：先定 Outline，再写讲稿，然后生成提词器。

---

## 10. 参考

- 记忆文件（每次改动都在这里有记录，按时间顺序）：
  - `~/.claude/projects/-Users-shuangdu/memory/riskmind-session1-video.md`：Session 1 的全部改动历史和数值
  - `~/.claude/projects/-Users-shuangdu/memory/riskmind-video-style.md`：风格和检查习惯
  - `~/.claude/projects/-Users-shuangdu/memory/MEMORY.md`：索引
- 最近几次改动的备份（`.render/` 里，最新的在前）：`before-endcard-dots.html`、`before-endcard-size.html`、`before-endcard.html`、`before-track-long.html`、`before-cover-smooth.html`、`before-cover-merge.html`、`before-cover-morph.html`、`before-rbc-gap.html`、`before-course.html`、`before-cover.html`
