# RiskMind 培训材料 — 交接文档 v5（Session 1 / 2 / 3）

写于 2026-11-17，取代 v4。v1–v4 留作历史，内容有冲突时以本文为准。
给接手的 Claude session 看。**对话用中文；文件内容（屏幕文字、talk track、outline）用英文。**

项目文件夹：`~/Downloads/RiskMind Video/`（以下简称"文件夹"）。

**v4 → v5 改了什么**：
- Session 2 的 MCP 事实改正了：`get_query_data` 返回下载链接，不是 MCP 把 CSV 存进 workspace。视频和讲稿都已同步。
- Session 3 Outline 按"为什么是 Agent + Plugin"这条主线重写成 9 张卡片。
- §2 里 v4 写的 MCP 细节（"每个 query 是一个 tool"）是错的，已改。

---

## 0. 先看这几点（最容易踩的坑）

1. **只用本地文件。** 线上的讲稿 Doc 和各个 outline 页面（claude.ai artifact）**不再维护，不要同步或重新发布**（用户 2026-11-10 决定）。
2. **用户改的是 md。** 各节的 `… — Video Script.md` 是用户自己编辑的源文件。Session 1 的流程：用户改完说一声 → Claude 把 talk track 同步到 Outline 的 Caption 栏 → 重新生成提词器 → 通读一遍，只**列出**语法/笔误问题，不擅自改用户写的内容。
3. **用户在编辑器里开着 md 时，不要往 md 里写东西。** 编辑器不会自动刷新，用户一保存就会把 Claude 的改动覆盖掉。拿不准就先问；用户明确说"你可以改"时再写。
4. **用户说某处"有 bug"时，先让用户刷新页面。** 浏览器里改完 HTML 要 Cmd+R。
5. **改任何东西之前先 `ls`，别信旧路径。** 每次改 HTML / md / Outline 前先备份到 `.render/`。
6. **不要用带 shell 变量或通配符的 `rm`**，会被安全检查拦下；需要清理时用明确的完整路径，或者留给用户。
7. **屏幕上和讲稿里永远不出现 "Claude Code"。** 同事的名字（照片里 git blame 的作者）也不能上屏。

---

## 1. 文件夹结构（2026-11-17）

- 根目录：`Handoff Notes/`（HANDOFF v1–v5）、`README.md`、`build_prompter.py`、`assets/`、`.render/`（备份和检查脚本）、`Session 1/`、`Session 2/`、`Session 3/`
- `Session 1/`
  - `RiskMind Session 1.html`：视频（单文件 HTML/SVG 动画，现场边放边讲）
  - `RiskMind Session 1 — Video Script.md`：讲稿（中文画面描述 + 英文 On-screen text + 英文 talk track），**用户编辑这一份**
  - `RiskMind Session1 Outline.html`：outline（英文画面描述 + On-screen + Caption + Reference + 每场截图），约 1.36 MB，文件名里 `Session1` 无空格
  - `RiskMind Session 1 Prompter.html`：提词器，由 `build_prompter.py` 从 Outline 生成，不要手改 beats 部分
  - `Product Positioning Speech.md`：Scene 2（beat 6–15）的单独副本，给 Jun 讲
- `Session 2/`
  - `RiskMind Session 2.html`：视频（DOM 动画，170.5 s，34 个停顿点）
  - `RiskMind Session 2 — Video Script.md`：讲稿，**Session 2 唯一的 talk track 来源**
  - `RiskMind Session 2 Outline.html`：做视频之前的规划（4 张 slide），已过时，不要拿它当 talk track。新格式 Outline 和提词器等 talk track 定稿后从 md 生成
- `Session 3/`：只有 `RiskMind Session 3 Outline.html`（2026-11-17 重写），**还没有视频、讲稿、提词器**

---

## 2. 项目是什么

RiskMind = Agent（基于 Claude Agent SDK）+ Plugin（Skills + MCP），用于 Market Risk。培训分三节：

| Session | 主题 | 日期 |
|---|---|---|
| Session 1 | RiskMind | November 12 |
| Session 2 | Agent | November 23 |
| Session 3 | Plugin | November 30 |

课程系列名：**GRM AI Learning Series**。观众：Senior Managers、Local Risk Managers，以及 Local Market Risk 以外的人；懂业务，不一定懂 AI。

**谁讲什么（Session 1）**：封面、课程页、beat 1–15 由 **Jun** 讲（"Jun's Speech"）。用户从 **beat 16** 开始讲，第一句 "Thanks, Jun."。

**产品事实（讲稿里用到的）**
- 封面：标题 **Vertical AI: RiskMind**；副标题 "Collaboration among Market Risk, COO AI Center of Excellence (AiXel) and Risk IT"。
- 时间线：2026 年 4 月启动，9 月完成 PoC；计划 **2027 年 4 月进入 production、开放给所有用户**。第三级是 Expansion（虚线）。
- PoC：一个用例 stress P&L explain，三个 portfolio（FX Option、Muni、IG Canada），每个 portfolio 一个 plugin、各一个 Stress P&L skill；数据连接 ATOM。
- Production：和各团队的 AI champions 一起，**从 3 个 skill 扩到 10+**；plugin 的建设逐步交给 Local Market Risk；Market Risk AI × AiXel 维护平台并提供 support。
- 数据连接：ATOM（PoC）；GRIP、RiskLedger 已接好；Other Data Sources 虚线。
- 平台功能（计划中）：AutoEval、AutoSkill、AutoEvolution。
- Pipeline：Get Data 由 **MCP**；Analyze、Build Dashboard 由 **Script**；Write Comments / Write Answer 由 **LLM**。原则 "Numbers from Scripts, Words from the LLM"。
- 定位页（Jun 讲）：RBC Assist Pro = augmented LLM（horizontal，黄），DocuMind = workflow，RiskMind = agent（vertical，蓝）。

**MCP 和 skill 的真实情况（2026-11-15 至 11-17 用户确认，看过三个真实 skill 和 query YAML 的照片）**
- **MCP 是"给 agent 提供 tool 的标准方式"，不是"data connection"。** 用户认为大家对 MCP 误解很大，Session 3 要全面讲。Session 1 里叫它 data connection，是因为当时只讲用途。
- RiskMind 里有两个 MCP server：
  - **backend 内置**的 MCP server：提供 `emit_turn_output`（把报告显示在聊天面板），跟 backend 绑在一起、默认可用，只是通过 MCP 暴露给 agent。不来自 plugin。
  - **ATOM MCP server**（AiXel 建）：只有两个 tool，`get_query_data(query_name, date)` 和 `list_queries`。skill 只用 `get_query_data`。
- Agent → **MCP Gateway**（查用户的 AD 组，下载时再查一次）→ ATOM MCP server → ATOM。plugin 的 `.mcp.json` 只放 gateway 地址。
- `get_query_data` 返回**下载链接**（`file_download_link`）+ row_count、pending_dates、message。**数据不进 context，MCP 也不往 workspace 存文件**；分析 script 按链接自己下载，在本地筛选（query 返回整张表）。不同 flow 之间复用同一个链接（"do not re-fetch"）。
- **Query catalog**：ATOM MCP 的 repo 里有个 `query` 文件夹，下面是 `fxo.yaml`、`gsp.yaml`，大体按 product 分组、有些会合并。每条：名字（= skill 里的 query_name）、description、group_name、fabric、analytic_id、dim_filters（category / scenario / where）、selects（带别名，比如 `pnl.pnl As pnlValue`，script 靠这些列名）、nodes（desk）、hierarchy、split_by。**条目里没有日期**，日期跟着每次调用传。用 git 管理，commit 关联 ticket。**以后由 Risk Manager 自己加条目。** 不要露出作者名、repo 名。
- `group_name` 和"按 skill 过滤 query"都没上线，不讲。
- **三个真实 skill**：`fxo-plugin/skills/fxo-stress-pnl`、`gsp-muni-plugin/skills/gsp-muni-stress-pnl`、`gsp-ig-ca-plugin/skills/gsp-ig-ca-stress-pnl`。
  - SKILL.md 结构相同：description → Business Background → Wording → 5 个 Analysis Steps（取数、分析 script、LLM 写评论、figures script、render）→ 几个 flow。
  - Flow 名字：**Portfolio Analysis / Detail Analysis / Ad-hoc**（FXO 的 BAU Investigation 属于 Ad-hoc，用户 2026-11-17 确认）。
  - 每个 flow 写明 slash command、query、script 命令、.md 的段落、评论 JSON 模板。
  - 三个 skill 都没有 references 文件夹，知识全写在 SKILL.md 里。
- **Shared Library**：三个 skill 的共同部分（步骤 3–5、raw/display 名字规则、日期规则、评论写法等）会抽出来。它是一个 uv package，同时放共享知识和共享代码；放在 plugins 的 parent dir，但不是直接引用，而是 uv install 进 backend 环境，skill 从那里用。skill 用 SKILL.md 里的 `!cat` 把共享知识插进来（加载时插入，不多一轮 Read）。**具体内容和路径还在等团队。**
- 三个 repo：agent runtime 在 backend；frontend 单独一个；plugins 单独一个。

---

## 3. 固定规则

**合作方式**
- 改 talk track 时：**一次一个 beat**，中文解释问题 + 给英文建议版本，**用户同意后才写进文件**。现在用户多数时候自己改 md，Claude 负责同步和挑错。
- 用户解释意图的话是给 Claude 的指导，**不是要写进稿子的文字**。
- 每次改文件先备份到 `.render/`；改视频后截图检查，说明检查了什么、没检查什么。
- 视频画面变了，同步改 md 的画面描述 / On-screen（有 Outline 的话也改 Outline 和截图）。
- 改动记录写进记忆（见 §7）。

**讲稿用词和口语化**
- 像现场讲话：短句、少用冒号和分号、不用 First/Second/Third 串讲（Key Takeaways 例外）。
- **少用 "you"**，不要 "You all know this process"。
- 避免"烫嘴"的组合："What changes is how it gets done"、"gives you back"、"happens on every run"、"tested it"、"Skill sets"、"walk you through"、"sum it up"、"word of mouth"。
- 同一段不重复同一个意思。
- "product" 指产品；"tool" **只**用来指 LLM 的 tools。
- 不说 RiskMind "replaces" 任何东西；RiskMind 不做 Official Risk Report。
- 用词：Judgement、Scripts（不是 code）、AiXel、What-if Analysis（不是 Sensitivities）、Dashboard、Center（美式拼法）。
- Session 1–2 不说 "Progressive Disclosure"，这个名字留给 Session 3。

**视频风格**
- 屏幕文字英文；大字每词首字母大写、无句号；字体 DM Sans。
- 只用蓝色系；唯一例外 Horizontal 用 RBC 黄（底 #FCF5DA、边 #DDBB4C、字 #8A6D12）。
- 换屏要带一个元素过去，不硬切；不要像 PPT；屏幕文字尽量少。

---

## 4. 文件关系和维护流程（Session 1）

```
RiskMind Session 1.html（视频，画面以它为准）
RiskMind Session 1 — Video Script.md（用户编辑；talk track 以它为准）
   ↓ Claude 用 Python 按标签逐行同步 talk track → Outline 的 Caption 栏
RiskMind Session1 Outline.html
   ↓ cd ~/Downloads/"RiskMind Video" && python3 -I build_prompter.py
RiskMind Session 1 Prompter.html
```

- md 表格每行：`| 标签 | 画面 | On-screen | Talk track |`；按 `|` 切开时 talk track 是 index 4。
- Outline 每行 `<tr><td>标签</td><td>Visual</td><td>On-screen</td><td>Caption</td><td>Reference</td></tr>`；写 Caption 时 HTML 转义，保留 `<br>`。
- 生成提词器应输出：`12 scenes, 46 beats (Cover, Course, 1 … 44)`。
- 结论是**保留 md**（Outline 有大量内嵌截图，不适合手改）。
- 提词器同步：视频 HTML 末尾的 `// ---------- prompter sync ----------` 段**不要删**；BroadcastChannel `rm-s1`。Session 2 以后要做提词器时，频道名和本地存储键要换成自己的。
- 视频操作（S1、S2 相同）：Space 播放/暂停，播到下一个停顿点自动停；→ / ← 落在停顿点；Home 回开头；F 全屏。

**检查工具**（`.render/`）
- Playwright 脚本：`stills.mjs`（视频截图）、`errs.mjs`（页面报错）、`tval.mjs`（在页面里求一个表达式，带 `?export=1`）、`livekeys.mjs`、`alltext.mjs`，以及 2026-11-17 新加的 `s3shot.mjs`（把 Session 3 Outline 的每张卡片单独截图）。
- 浏览器要用 `executablePath: ~/Library/Caches/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-mac-arm64/chrome-headless-shell`。
- 截图：`node .render/stills.mjs "<绝对路径 html>" <输出文件夹> t1 t2 …`。没有 PIL；裁图、转 JPEG 用 `sips`。
- 长正则用 grep/ugrep 会报 "exceeds complexity limits"，改用 `python3 -I`。

---

## 5. 当前状态

### Session 1 — 定稿
- 视频、讲稿、提词器 2026-11-10 定稿。
- **待修的小问题**（不急，做之前问用户）：
  1. Outline beat 23 Reference 栏错字 "or a answer in chat in chat"。
  2. `README.md` 输出示例应为 46 / 44 beats。
  3. md Overview 过时（时长、"代码算"→"脚本算"、待做里的段号）。
  4. 时间标签偏移（v3 遗留），不影响提词器。
  5. Outline 部分截图和 beat 39–43 的 Visual 没逐帧核对。
- **待办**：Demo 视频接进 beat 26 的占位框（时钟停住、不加进时间轴）；deck outline 去掉 "replaces the existing risk report"。

### Session 2（Agent）— 视频接近定稿，talk track 待逐句重审
- 视频 170.5 s、34 个停顿点：封面、课程页 → 四层（Augmented LLM、Agent Harness、RiskMind Customization、Business Plugin）→ 一次真实定时 run（FXO Stress PnL，11 轮）→ Dashboard → 四个圈回答 Q1（为什么做 RiskMind：横向可换、纵向是我们的价值）→ 三条 Takeaways → 下节预告 → 结束页。
- **2026-11-16/17 按 MCP 事实改了视频**（备份 `.render/s2-before-getquerydata-2026-11-16.html`、`s2-before-t3links-2026-11-17.html`）：
  - MCP Tools 里的 chip 从 `run_query` 改成 `get_query_data`（两个 MCP chip 都改成 11px，才能排在一行）。
  - T2 只返回 "→ 8 links"，Workspace 里不再出现 "8 CSV files"（用户决定不加回）。
  - T3 的调用写成 `portfolio_analysis.py --portfolio-url … --scenario …`。T3 运行时，Context 里 T2 那块会亮起（`ctxIn:2`），表示链接交给了 script。`--portfolio-url` 这个参数名借用的是 Muni 的，FXO 的真名没看到。
  - Takeaway 2 改成 "…data comes in only as download links"，pill 改成 "→ 8 links"。
  - 调用框里的选项名不再从中间断开，T7 的长文件名放得进一行。
- **讲稿 md 2026-11-17 同步改了**（备份 `.render/s2-script-before-talkfix-2026-11-17.md`、`s2-script-before-tooldef-2026-11-17.md`）：
  - Overview 的 Q2：Session 2 只答 context 这一半，另一半留给 Session 3。
  - 第 3 段：补了 tool 的定义（"A tool is something the LLM can ask for but can't do itself…"）。
  - 第 4 段："Switch Muni off by hand"。
  - 第 7 段：删掉 "RiskMind adds no custom tools of its own"（跟 `emit_turn_output` 冲突）。
  - 第 9 段：加了 "and a query if it needs new data"。
  - 第 11、13、14、30 段：改成 `get_query_data`、下载链接、script 自己下载。
  - 第 27 段：改成 "That's **one** reason we build RiskMind as Agent plus Plugin."，重复的预告句删了。
  - 第 32 段：预告改成回到第 3 段的第二个问题 "how much effort does it take to add a new analysis?"。
- **还要做**：用户说之后要**逐字逐句**重审整份 talk track（一次一个 beat）；确认 takeaway 文字；讲之前确认 "GPT-6.1 Sol" 仍是 OpenAI Sonnet 级别模型的名字；定稿后再决定新格式 Outline 和提词器。
- 措辞和视觉规则见记忆 `riskmind-session2-decisions.md`。

### Session 3（Plugin）— Outline 重写完，等用户逐张 review
- `Session 3/RiskMind Session 3 Outline.html` 2026-11-17 重写（备份 `.render/s3-before-outline-2026-11-17.html`、`s3-before-tooltable-2026-11-17.html`）。**时间先不管**：用户要先把能想到的内容都放进去，再慢慢删。
- **主线：为什么是 Agent + Plugin？** Session 1、2 留下的问题，Session 3 开场提出、结尾回答。两个答案，每张卡片都标了标签：
  - **Expansion**：加一个新分析 = 写 SKILL.md + 命令行 script + 一条 query，不需要懂 agent、tool 注册、MCP 开发和托管。Agent（AI runtime）和 Plugin（业务知识）分开；RBC Assist Pro 也分开，但是靠 MCP、没有 skill。
  - **Context**：下载链接让数据不进 context（Assist Pro 没有这个机制，数据全进 context）；skill 按需加载，不用像 Assist Pro 那样手动关 MCP server（Session 2 第 4 段）；progressive disclosure 就是为 context 设计的。
- **9 张卡片**：
  1. Why Agent + Plugin?（开场，接 Session 2 的四个圈和第 3 段的两个问题）
  2. Plugin Introduction（真实 plugin 名字；Risk Manager 写的三样东西和各自的位置）
  3. SKILL.md（五个部分；用一张表把 SKILL.md 对到 Session 2 的 T1–T10，原来的 Walk Through 并进来了）
  4. Scripts（新：改造前的 constants 写法 vs 改造后的命令行写法，用 Muni 的真实命令；9 条条件；3 个必须对上的约定；Bash + 命令行替代 tool 注册）
  5. What MCP Is（新：先回顾 tool 的定义；一张表列出 tool 从哪里来，并说明 skill、script 都不是 tool；5 行误解表；两个 MCP server；对照"把分析包成 tool"的做法）。引用换成了 MCP 官方文档讲 tools 的原话，2026-11-17 核对过；删掉了 Anthropic 发布文里 "systems where data lives" 那句。
  6. MCP Gateway, Tools and the Query Catalog（用 `GSP_MUNI_POSITIONS_STRESS` 走一遍完整路径；分层表；重画的 YAML；"The tool is how, the catalog is what"；治理五条 + git 历史）
  7. Writing a Skill（新：8 条清单配真实例子，是 Claude 归纳的，待用户 review）
  8. Shared Library（等团队细节）
  9. Takeaways（之后再做；Expansion、Context 两张对比表已放进去）
- **review 时要留意的推断**：YAML 的 `fabric` 写成 `…`（GSP 用 IRMPositionDim 还是 PositionDim 没记清）；Takeaways 表里 Assist Pro "LLM 在返回的数据上算"是推断；Writing a Skill 的 8 条是 Claude 归纳的。
- 封面、课程页、结束页之后再做，照 Session 1、2 的样子。

---

## 6. 下一步（建议顺序）

1. **Session 3**：用户逐张 review Outline；拿到 Shared Library 的具体内容和路径后补那一页；内容定了再删减时间、写讲稿、做视频。
2. **Session 2**：talk track 逐句重审（一次一个 beat）；定稿后做新格式 Outline 和提词器（如果要）。
3. **Session 1**：上面的待修小问题（问用户）；Demo 录好后接进 beat 26。

**需要用户拍板的问题**
- Shared Library 的具体内容和 `!cat` 的路径（等团队）。
- FXO 分析 script 的真实参数名（Session 2 T3 现在借用 Muni 的 `--portfolio-url`）。
- Session 2 要不要提词器；Demo 视频播放时 Space 怎么用。

---

## 7. 链接和记忆

线上页面停在旧版本，**不要更新**，只供查旧内容：
- Session 1 outline：https://claude.ai/artifact/FZYXQf3QTiHxwkbDAnWumF
- 视频讲稿 Doc：https://claude.ai/artifact/64pG6b9JRMpeXa4JwrZEtD
- Session 2 outline（旧格式）：https://claude.ai/artifact/LkLWhxi1SCE4WTVqAYG1Wz
- Session 3 outline（旧格式）：https://claude.ai/artifact/7t6EW7JbvMi1MWbWcHT1SL

记忆文件：
- `~/.claude/projects/-Users-shuangdu/memory/`：`riskmind-session1-video.md`、`riskmind-session2-video.md`、`riskmind-session2-decisions.md`、`riskmind-session3.md`（Session 3 的事实和状态，最详细）、`riskmind-video-style.md`
- `~/.claude/projects/-Users-shuangdu-Downloads-RiskMind-Video/memory/`：`talk-track-review-feedback.md`（review talk track 的方式）
