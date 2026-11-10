# RiskMind 培训材料 — 交接文档 v4（Session 1 / 2 / 3）

写于 2026-11-10，取代 v3。v1–v3 留作历史，内容有冲突时以本文为准。
给接手的 Claude session 看。**对话用中文；文件内容（屏幕文字、talk track、outline）用英文。**

项目文件夹：`~/Downloads/RiskMind Video/`（以下简称"文件夹"）。

---

## 0. 先看这几点（最容易踩的坑）

1. **只用本地文件。** 线上的讲稿 Doc 和 Session 1 outline 页面（claude.ai artifact）**不再维护，不要同步或重新发布**（用户 2026-11-10 决定）。
2. **用户改的是 md。** `Session 1/RiskMind Session 1 — Video Script.md` 是用户自己编辑的源文件。用户改完说一声，Claude 负责：把 talk track 同步到 Outline 的 Caption 栏 → 重新生成提词器 → 通读一遍，只**列出**语法/笔误问题，不擅自改用户写的内容。
3. **用户在编辑器里开着 md 时，不要往 md 里写东西。** 编辑器不会自动刷新，用户一保存就会把 Claude 的改动覆盖掉（2026-11-10 发生过一次误会：用户的编辑器显示的是旧版）。这时只在对话里给建议的英文句子，让用户自己改；用户说"改好了"再一次性同步。每次同步前先确认之前的改动还在（比如 Scene 2 仍是 "Jun's Speech"）。
4. **用户说某处"有 bug"时，先让他刷新页面。** 2026-11-10 "按空格断点被跳过"的问题，最后是视频页面没刷新、还在跑修复前的旧代码。浏览器里改完 HTML 要 Cmd+R。
5. **改任何东西之前先 `ls`，别信旧路径。** 每次改 HTML / md / Outline 前先备份到 `.render/`。

---

## 1. 文件夹结构（2026-11-10）

- 根目录：`Handoff Notes/`（HANDOFF v1–v4）、`README.md`、`build_prompter.py`、`assets/`、`.render/`（备份和检查脚本）、`Session 1/`、`Session 2/`、`Session 3/`
- `Session 1/`
  - `RiskMind Session 1.html`：视频（单文件 HTML/SVG 动画，现场边放边讲）
  - `RiskMind Session 1 — Video Script.md`：讲稿（中文画面描述 + 英文 On-screen text + 英文 talk track），**用户编辑这一份**
  - `RiskMind Session1 Outline.html`：outline（英文画面描述 + On-screen + Caption + Reference + 每场截图），约 1.36 MB，文件名里 `Session1` 无空格
  - `RiskMind Session 1 Prompter.html`：提词器，由 `build_prompter.py` 从 Outline 生成，不要手改 beats 部分
  - `Product Positioning Speech.md`：Scene 2（beat 6–15）的单独副本，给 Jun 讲（见 §4）
- `Session 2/`：`RiskMind Session 2.html`（视频）、`RiskMind Session 2 — Video Script.md`（2026-11-07 由视频反推的初稿，talk track 待确认）、`RiskMind Session 2 Outline.html`（旧格式）
- `Session 3/`：只有 `RiskMind Session 3 Outline.html`（旧格式），**没有视频**

---

## 2. 项目是什么

RiskMind = Agent（基于 Claude Agent SDK）+ Plugin（Skills + MCP），用于 Market Risk。培训分三节，每节约 45 分钟，另留 15–20 分钟 Q&A：

| Session | 主题 | 日期 |
|---|---|---|
| Session 1 | RiskMind | November 12 |
| Session 2 | Agent | November 23 |
| Session 3 | Plugin | November 30 |

课程系列名：**GRM AI Learning Series**。观众：Senior Managers、Local Risk Managers，以及 Local Market Risk 以外的人；懂业务，不一定懂 AI。

**谁讲什么（Session 1）**：封面、课程页、beat 1–15（GRM AI Vision、AI Tools Landscape / Positioning）由 **Jun** 讲，讲稿里写 "Jun's Speech"。用户从 **beat 16** 开始讲，第一句是 "Thanks, Jun."。

**产品事实（讲稿里用到的）**
- 封面：标题 **Vertical AI: RiskMind**；副标题 "Collaboration among Market Risk, COO AI Center of Excellence (AiXel) and Risk IT"。所以 AiXel = COO AI Center of Excellence。
- 时间线：2026 年 4 月启动，9 月完成 Proof of Concept；计划 **2027 年 4 月进入 production、开放给所有用户**，所以下一阶段叫 production。第三级是 Expansion（虚线，未定时间）。
- PoC：一个用例 stress P&L explain，三个 portfolio（FX Option、Muni、IG Canada），每个 portfolio 一个 plugin、各一个 Stress P&L skill；Agent 有 Runtime；数据连接 ATOM。
- Production 阶段：和各团队提名的 AI champions 一起，**从 3 个 skill 扩到 10+**；plugin 的建设逐步交给 Local Market Risk；Market Risk AI × AiXel 维护平台（agent + 数据连接）并提供 support。
- 数据连接：ATOM（PoC）；**GRIP、RiskLedger 已接好**（视频里是实心 badge，但在 beat 38 才出现）；Other Data Sources 虚线。
- 平台功能（计划中）：AutoEval（新 skill 上 production 前必须通过）、AutoSkill（聊天起草 skill 的 agent）、AutoEvolution（从使用对话中找改进点来改 skill）。
- Pipeline：Get Data 由 **MCP**；Analyze、Build Dashboard 由 **Script**；Write Comments / Write Answer 由 **LLM**。原则 "Numbers from Scripts, Words from the LLM"。
- MCP 细节：每个 query 是一个 tool；Local Risk Manager 提供 query catalog，AiXel 建连接和 MCP 本身。**讲稿里不展开**，只说 plugin 是 risk manager 塑造的部分、AiXel 做 data connection。
- Plugin 在 Session 1 用 "product" 计（画面 "Plugin: Product"、"Expand to More Products"），1 product = 1 plugin，1 analysis = 1 skill（只口头讲）。
- 定位页（Jun 讲）：Chat / Augmented LLM | Agentic Systems；Prompt Chaining、Autonomous Agent 是 pattern（虚线），不是产品；RBC Assist Pro = augmented LLM（horizontal，黄），DocuMind = workflow，RiskMind = agent（vertical，蓝）。定义来自 Anthropic "Building effective agents"。
- Today vs. With RiskMind：effort bar = **Design · Execution · Judgement**；With RiskMind 时 Execution 大幅缩短、Design 变宽（一次性）、Judgement 不变，左侧空出 Saved Effort。角色变化：做一次设计、每次 verify。

---

## 3. 固定规则

**合作方式**
- 改 talk track 时：**一次一个 beat**（很短的 beat 可以两三个一起），中文解释问题 + 给英文建议版本，**用户同意后才写进文件**。现在用户多数时候自己改 md，Claude 负责同步和挑错。
- 用户解释意图的话（如 "the key word is automatic"）是给 Claude 的指导，**不是要写进稿子的文字**。
- 每次改文件先备份到 `.render/before-<名字>.<ext>`；改视频后截图检查（必要时发给用户），说明检查了什么、没检查什么。
- 视频画面变了，同步改：md 的画面描述 / On-screen、Outline 的 Visual / On-screen、Outline 里对应场景的截图（1280×720 JPEG）。
- 在 `~/.claude/projects/-Users-shuangdu/memory/riskmind-session1-video.md`（或 session2）末尾追加一行改动记录。

**讲稿用词和口语化（用户 2026-11-07 至 11-10 反复强调）**
- 要像现场讲话，不像念稿：短句、少用冒号和分号、不用 First/Second/Third 串讲（Key Takeaways 例外）。
- **少用 "you"**，尤其不要 "You all know this process"（观众不只 Local Market Risk）。
- 避免读着"烫嘴"的组合：用户读不顺的有 "What changes is how it gets done"、"gives you back"、"happens on every run"、"Now look at who does each step"、"tested it"、"Skill sets"（会听成 skillset）、"walk you through"、"sum it up"、"word of mouth"。改用简单主谓句。
- 不要在同一段里重复同一个意思（如 Beat 25 原来把"LLM 不算数字"说了四遍）。
- "product" 指产品；"tool" **只**用来指 LLM 的 tools。
- 说 **domain expertise**（屏幕上的 Knowledge 不用改）。
- 不提早期尝试和失败案例；不说 RiskMind "replaces" 任何东西；RiskMind 不做 Official Risk Report。
- 用词：Judgement、Scripts（不是 code）、Digitize、AiXel、What-if Analysis、Dashboard、Answer in Chat、Standard Operating Procedure、Center（美式拼法）。
- 讲 key person risk 时说"人员变动时知识留在团队里"。

**视频风格**（不变）
- 屏幕文字英文；大字每词首字母大写、无句号；字体 DM Sans。
- 只用蓝色系；唯一例外 Horizontal 用 RBC 黄（底 #FCF5DA、边 #DDBB4C、字 #8A6D12）。不用绿色。
- 换屏要带一个元素过去，不硬切；不要像 PPT；屏幕文字尽量少。

---

## 4. 文件关系和维护流程

```
RiskMind Session 1.html（视频，画面以它为准）
RiskMind Session 1 — Video Script.md（用户编辑；talk track 以它为准）
   ↓ Claude 用 Python 按标签逐行同步 talk track → Outline 的 Caption 栏
RiskMind Session1 Outline.html
   ↓ cd ~/Downloads/"RiskMind Video" && python3 -I build_prompter.py
RiskMind Session 1 Prompter.html
```

- md 表格每行：`| 标签 | 画面 | On-screen | Talk track |`，段落之间用 `<br><br>`；按 `|` 切开时 talk track 是第 5 段（index 4）。标签 "封面 · 0.0s"、"课程 · 2.2s" 对应 Outline 的 "Cover · 0.0s"、"Course · 2.2s"。
- Outline 每行 `<tr><td>标签</td><td>Visual</td><td>On-screen</td><td>Caption</td><td>Reference</td></tr>`；写 Caption 时 HTML 转义（P&L → `&amp;`），保留 `<br>`。Outline 里还有几行 "Portfolio Analysis / Drill Down / Ad-hoc" 是别的表，不是 beat。
- 生成提词器应输出：`12 scenes, 46 beats (Cover, Course, 1 … 44)`。提词器的 Caption 用 `white-space: pre-line`，`<br>` 会显示成换行。
- 用户问过要不要删掉 md 只改 Outline：结论是**保留 md**。Outline 有大量内嵌截图，不能在浏览器里编辑，用编辑器改很容易坏格式；md 还有中文画面描述、Production notes、待做清单。
- `Product Positioning Speech.md`：Scene 2（beat 6–15）的副本，三列 Beat · On-screen Text · Talk Track，无中文，beat 11 改成 "As I mentioned earlier"，beat 6 的 "Thanks, Jun" 已去掉。**它和 video script 是两份独立文件**，Jun 那边的改动不会自动同步。

**提词器和视频怎么同步**
- 视频 HTML `<script>` 末尾有 `// ---------- prompter sync ----------` 段（外加 PageDown/PageUp），**不要删**。
- BroadcastChannel `rm-s1`（提词器打开视频窗口时还会走 postMessage）。视频是时钟的主人，提词器只发命令；提词器按"T 落在第几个停顿点"决定显示哪个 beat（按顺序，不看秒数）。
- 小预览是 iframe `RiskMind Session 1.html?export=1&mirror=1`，两个 HTML 必须在同一文件夹。

**视频操作（Session 1、Session 2 都已修好）**
- Space：播放 / 暂停，播到下一个停顿点自动停。→ / ←：总是落在一个停顿点并停住（播放中按 → 是播完当前这段，不会跳过一段）。按住不放只算一次（`e.repeat`）。Home 回开头，F 全屏。
- 停顿点 `STOPS` 是排好序的 `BEATS`；`frame()` 推进 T 并夹在下一个停顿点。Session 1：44 个停顿点，`DURATION` 136.6 s。

**Demo（beat 26，96.3 s）**
- 现在是占位画面：虚线框 + 播放图标 + "Demo"（"RiskMind in action" 已删）。talk track "Okay, that's enough from me. Let's meet RiskMind."
- 计划：录好的 demo 视频**放进这个占位框里播**，时钟停在 beat 26 不动 → 提词器不受影响。**不要**把 demo 时长加进时间轴（后面所有时间标签都会错）。待定：视频播放中 Space 的行为（建议：没播完时控制视频暂停/继续，播完再按进入 beat 27，PageDown 同理）；视频文件放在 HTML 旁边用相对路径，不要内嵌；提词器小预览只会显示静态框。录屏里的真实报告是否要脱敏也要确认。

**检查工具**（`.render/`）
- Playwright 脚本（`stills.mjs`、`errs.mjs`、`alltext.mjs`、`livekeys.mjs` 等）。浏览器要用 `executablePath: ~/Library/Caches/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-mac-arm64/chrome-headless-shell`（默认的 1248 版没装）。
- 截图：`node .render/stills.mjs "<绝对路径 html>" <输出文件夹> t1 t2 …`；转 JPEG 用 `sips -s format jpeg -s formatOptions 82 -z 720 1280`（没有 PIL）。
- 长正则用 grep/ugrep 会报 "exceeds complexity limits"，改用 Python。

---

## 5. 当前状态

### Session 1 — talk track 定稿
- Outline 12 张场景卡、46 行（Cover、Course、1–44），视频 136.6 s。
- **2026-11-07 至 11-10 完成**：
  - Beat 16–44 逐个 review 完，之后用户自己通读修改，已全部同步到 Outline 和提词器。Cover–15 = "Jun's Speech"。
  - 视频改动：→/← 和按住键的跳断点问题（S1、S2）；beat 25 的 Get Data 标 MCP；封面副标题和标题（Vertical AI: RiskMind）；课程系列名 GRM AI Learning Series；日期 Nov 23 / Nov 30（含片尾预告卡）；Centre → Center；GRIP、RiskLedger 改实心；删掉 Demo 下的 "RiskMind in action"。对应的 Outline 截图都已重拍（cover、pipeline 96.2 s、demo 97.6 s、expansion 120.6 s）。
  - Session 2 预告卡（片尾 beat 43）早已做好。
- **待修的小问题**（都不急，做之前问一下用户）：
  1. Outline beat 23 的 **Reference** 栏错字："or a answer in chat in chat" → "or an answer in chat"。
  2. `README.md` 里的输出示例还是 "45 beats (Cover, Course, 1 … 43)"，应为 46 / 44。
  3. md Overview 过时："约 116 秒"（现在 136.6 s，讲稿字数也要重算）、"数字全部由代码算"→由脚本算；"待做"里 "补上第 20 段讲稿" → 第 26 段（Demo）。
  4. 时间标签偏移（v3 遗留）：Course 应为 0.0 s、beat 1 应为 2.2 s，之后每行标"该段开始播放的时刻"。不影响提词器（按顺序对应）。
  5. Outline 截图里 Key Takeaways、结束页、收拢转场没有逐张核对过；beat 39–43 的 Visual 描述没逐帧对照视频。
- **待办（内容）**：Demo 视频接入（见 §4）；deck outline（PPT，不在文件夹里）去掉 "replaces the existing risk report"、Expansion 页按视频调整。

### Session 2（Agent）— 视频已有，讲稿初稿已有
- `RiskMind Session 2.html` 是最新视频（27 段、26 个停顿点，约 154 s）。注意：代码里有个变量 `DURATION` 是 123.6，但停顿点到 149.1，这是另一个变量、还没查清楚。
- `RiskMind Session 2 — Video Script.md`：2026-11-07 由视频反推的初稿，**talk track 待用户确认**。
- 旧格式 `Session 2 Outline.html` 可能和视频不一致；里面的 "Sensitivities" 要改成 What-if Analysis。
- 还没有提词器和 prompter sync。如果要做：`build_prompter.py` 默认路径是 Session 1（可传两个路径参数），视频要加 sync 段，频道名 `rm-s1` 和本地存储键要换成 Session 2 自己的。
- 措辞和视觉规则见记忆 `riskmind-session2-decisions.md`。

### Session 3（Plugin）— 只有旧 outline，无视频
- 已起草 Plugin Introduction、Skill Introduction；Skill Walk Through、MCP Introduction 暂停。
- 卡点（要用户提供）：Shared Library（`plugins/reference/`）怎么运作；skill 重构后抽出什么、剩下什么。
- 旧 outline 里的 "Sensitivities" 要改。

---

## 6. 下一步（建议顺序）

1. Session 1 收尾：上面的待修小问题（问用户要不要做）；Demo 录好后接进 beat 26。
2. Session 2：和用户 review `Session 2 — Video Script.md` 的 talk track（同样的方式：一个 beat 一个 beat，或用户自己改），再决定要不要 Outline 新格式和提词器。
3. Session 3：先拿到两个卡点的信息，再写内容，之后做视频。
4. 三节串起来：课程结构、session 之间的过渡，更新 deck outline。

**需要用户拍板的问题**
- Demo 视频播放时 Space 怎么用（见 §4）。
- Session 2 要不要提词器。

---

## 7. 链接（历史，不再维护）

以下线上页面停在旧版本，**不要更新**，只供查旧内容：
- Session 1 outline：https://claude.ai/artifact/FZYXQf3QTiHxwkbDAnWumF
- 视频讲稿 Doc：https://claude.ai/artifact/64pG6b9JRMpeXa4JwrZEtD
- Session 2 outline（旧格式）：https://claude.ai/artifact/LkLWhxi1SCE4WTVqAYG1Wz
- Session 3 outline（旧格式）：https://claude.ai/artifact/7t6EW7JbvMi1MWbWcHT1SL

记忆文件：`~/.claude/projects/-Users-shuangdu/memory/`（`riskmind-session1-video.md` 改动历史、`riskmind-session2-video.md`、`riskmind-session2-decisions.md`、`riskmind-video-style.md`）。
