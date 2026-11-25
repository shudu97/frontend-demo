# RiskMind 培训材料 — 交接文档 v6（Session 1 / 2 / 3）

写于 2026-11-24，取代 v5。v1–v5 留作历史，内容有冲突时以本文为准。
给接手的 Claude session 看。**对话用中文；文件内容（屏幕文字、talk track、outline）用英文。**

项目文件夹：`~/Downloads/RiskMind Video/`（以下简称"文件夹"）。

**v5 → v6 改了什么**：
- **Session 3 开始做视频了**：`Session 3/RiskMind Session 3.html`，已做到 Scripts 的一半（67.55 s，32 个停顿点）。§5 有逐段说明。
- 工作方式变了：**先一段一段做 HTML 动画，outline 最后按 HTML 重写**。v5 里那份 9 张卡片的 Outline 已经过时，只当素材库用。
- Session 3 的主线改了：不再有 "Why Agent + Plugin?" 开场卡片，主线就是 `fxo-plugin` 这个文件夹本身（见 §5）。
- **Session 2 已定稿**（2026-11-21 在公司电脑上定稿）。
- 补了很多 Session 3 的真实事实（FXO 的真实命令、scripts 文件夹内容、三个 flow 的结构等），见 §2。

---

## 0. 先看这几点（最容易踩的坑）

1. **只用本地文件。** 线上的讲稿 Doc 和各个 outline 页面（claude.ai artifact）**不再维护，不要同步或重新发布**。
2. **用户在编辑器里开着 md 时，不要往 md 里写东西**（编辑器不会自动刷新，用户一保存就覆盖）。拿不准先问。
3. **用户说某处"有 bug"时，先让用户刷新页面**（Cmd+R）。每次改完 HTML，用 built-in 浏览器重新打开 `file:///Users/shuangdu/Downloads/RiskMind%20Video/Session%203/RiskMind%20Session%203.html`。
4. **改任何东西之前先备份到 `.render/`**（命名习惯：`s3v-before-<改了什么>-<日期>.html`）。
5. **不要用带 shell 变量或通配符的 `rm`**，会被拦；清理用完整路径，或者留给用户。
6. **屏幕上和讲稿里永远不出现 "Claude Code"。** `CLAUDE.md`（Session 2 讲过）和 `${CLAUDE_SKILL_DIR}`（真实命令里的变量）可以出现；官方定义原文里的 "Claude"（不是 "Claude Code"）可以。
7. **同事的名字（照片里 git blame 的作者）、repo 名不能上屏，也不要写进记忆。**
8. **不要露出真实的 gateway URL。**
9. **`ccar-ims-plugin` 永远不出现**（早期测试用的，会删）；plugins 那一排只画三个。
10. **"product" 指产品，"tool" 只指 LLM 的 tools。**
11. **Session 3 HTML 里 `OP` 的时间名不能重名。** 已经踩过两次：`OP.f0`（plugin 文件夹 vs 正文折叠）、`OP.sn0`（Skill navigator vs Scripts）。加新名字前先 `grep -o "OP\.<名字>=" | wc -l` 确认是 0。全局 `const` 也一样（`FR` 撞过一次）。
12. **隐藏的 SVG 文字量出来宽度是 0。** 测量宽度时要临时把 `style.display=''`，或者只用 opacity 渐隐不用 display:none（`op()` 在透明度为 0 时会设 display:none）。

---

## 1. 文件夹结构（2026-11-24）

- 根目录：`Handoff Notes/`（HANDOFF v1–v6）、`README.md`、`build_prompter.py`、`assets/`、`.render/`（备份和检查脚本）、`Session 1/`、`Session 2/`、`Session 3/`
- `Session 1/`：视频、讲稿 md（用户编辑这份）、Outline、提词器、`Product Positioning Speech.md`。见 v5 §1，没变。
- `Session 2/`：视频、讲稿 md、旧 Outline。**已定稿。**
- `Session 3/`
  - `RiskMind Session 3.html`：**视频，正在做**（单文件 SVG 动画，引擎和 Session 2 一样）
  - `RiskMind Session 3 Outline.html`：2026-11-17 的 9 张卡片版，**已过时**，只当素材（官方定义原文、MCP 细节、清单等）。视频做完后按 HTML 重写。
- 真实 SKILL.md 和文件夹的照片原来在 Claude 的临时 scratchpad 里（重启会丢），**关键内容都已经写进 §2 和记忆**。缺什么就请用户重新拍。

---

## 2. 项目是什么，以及真实事实

RiskMind = Agent（基于 Claude Agent SDK）+ Plugin（Skills + MCP），用于 Market Risk。

| Session | 主题 | 日期 |
|---|---|---|
| Session 1 | RiskMind | November 12 |
| Session 2 | Agent | November 23 |
| Session 3 | Plugin | November 30 |

课程系列名 **GRM AI Learning Series**；观众懂业务、不一定懂 AI。Session 3 大约 25 分钟。产品事实（封面、时间线、PoC、Production、pipeline 等）见 v5 §2，没变。

**MCP 的真实情况**（v5 已有，仍然成立）
- MCP 是"给 agent 提供 tool 的标准方式"，**不是** "data connection"。Session 1 叫它 data connection 是因为当时只讲用途；Session 3 要正面纠正。
- 两个 MCP server：backend 内置的（`emit_turn_output`）和 ATOM MCP server（只有 `get_query_data(query_name, date)`、`list_queries` 两个 tool，skill 只用前者）。
- Agent → MCP Gateway → ATOM MCP server → ATOM。`get_query_data` 返回**下载链接**（`file_download_link` + row_count、pending_dates、message），数据不进 context，分析 script 自己按链接下载。
- Query catalog 在 ATOM MCP 的 repo 里（`fxo.yaml`、`gsp.yaml`…），以后由 Risk Manager 自己加条目。细节见 v5 §2。
- **`.mcp.json` 的真实情况**：现在 MCP 是在 backend 里配置的，不在 plugin 里（以前 plugins 放在 backend 外面，SDK 不从项目目录外的 plugin 加载 MCP；而且只有一个 MCP server）。Shared Library 的改动会把 plugins 挪进 backend，之后 MCP 会改成走 plugin。**培训材料里就当 `.mcp.json` 在 plugin 里**（保留三部分的间隔页）。

**真实的 fxo-plugin**
- `fxo-plugin/.claude-plugin/plugin.json`：`{"name": "fxo-plugin", "version": "0.0.1", "description": "Streamline FXO workflows. Generate reports, visualizations, and perform data analysis."}`
- `fxo-plugin/skills/fxo-stress-pnl/` 下：`SKILL.md`、`scripts/`，以及不画的 `IMPLEMENTATION.md`、`README.md`。
- **`scripts/` 里画出来的**：`analysis/`、`templates/` 两个文件夹，`bau_analysis.py`、`constants.py`、`detail_analysis.py`、`generate_bau_figures.py`、`generate_detail_figures.py`、`generate_portfolio_figures.py`、`portfolio_analysis.py`。
  - **不画**：`__pycache__`、`.ruff_cache`、`fetch_bau_data.py`（BAU 自己的取数 script）、`queries.py`（老的 script 取数方式，文件还在，只是不展示）、`stress_pnl_attribution.py`（独立脚本，SKILL.md 里没调用）。
  - `templates/` 不是 agent 用的 resource，是代码的一部分；画出来，但不做 chip、不变灰。
- `.market-risk-base`（repo 根目录）= Shared Library，**还没定稿**，那一节挂起。

**真实的 SKILL.md（约 432 行）结构**
- YAML metadata：`name: fxo-stress-pnl`；description = "做什么"（FXO stress PnL analysis — …）+ "什么时候用"（Use this skill whenever the user asks about FXO stress, …）。
- `# FXO Stress PnL` 正文，五个 `##`：
  1. **Business Background**（`### Scenario Names (Display Vs Raw)`、`### BAU, Murex And The Estimate`、`### Wording` 等）
  2. **Analysis Steps**：一段导语 + 5 个 `###`：Step 1: Fetch The Data / Step 2: Run The Analysis / Step 3: Write The Commentary As Text JSON / Step 4: Build The Figures / Step 5: Render。Steps 1–2 每个 flow 不同，Steps 3–5 共用。
  3. **Slash Command `/fxo-stress-pnl` — Portfolio Analysis**（第 101 行起）：说明、Usage（`/fxo-stress-pnl <date> <prev-date> [scenario]`）、两条参数说明、`### Step 1: Fetch Data via MCP`（8 个 `get_query_data`）、`### Step 2: Analysis`（13 行真实命令，见下）、`### Steps 3–5: Comment, Build, Render`。
  4. **Detail Analysis — Single Currency Pair**（第 208 行起）：Step 1 第 220 行、Step 2 第 237 行、Steps 3–5 第 312 行。
  5. **BAU Investigation — The Reported Numbers**（第 340 行起）：Step 1: Fetch Data 第 353 行、Step 2: Analysis 第 363 行、Steps 3–5 第 407 行。
- **三个 flow 的 Steps 3–5 写法完全一样**："Follow the shared **Step 3–5** (see **Analysis Steps**), with the … specifics below:"，然后 `**Step 3**: text JSON.`（keys：Portfolio 是 checks/total/estimation/change；Detail 是 attribution/change/books/books_change/new_trades；BAU 是 total/pairs/books/activity）、`**Step 4**: Figures.`（各自的 `generate_*_figures.py`）、`**Step 5**: Render. As in the analysis steps.`
- **Portfolio 的真实命令**（SKILL.md 第 131–144 行）：
  ```
  uv run ${CLAUDE_SKILL_DIR}/scripts/portfolio_analysis.py \
      --bau-url "<FXO_STRESS_PNL link, date>" \
      --prev-bau-url "<FXO_STRESS_PNL link, prev-date>" \
      --murex-url "<FXO_STRESS_PNL_TRADE_LEVEL link, date>" \
      --prev-murex-url "<FXO_STRESS_PNL_TRADE_LEVEL link, prev-date>" \
      --portfolio-url "<FXO_PORTFOLIO_STRESS link, date>" \
      --riskmod-url "<FXO_TRADE link, date>" \
      --grid-url "<FXO_SPOT_VOL_GRID link, date>" \
      --prev-grid-url "<FXO_SPOT_VOL_GRID link, prev-date>" \
      --scenario <raw scenario> \
      --output "${TEMP_OUTPUT_DIR}/portfolio_analysis_<date>_<prev-date>.md" \
      --json-output "${TEMP_OUTPUT_DIR}/portfolio_analysis_<date>_<prev-date>.json"
  ```
  `--portfolio-url` 是 FXO 的真名（v5 以为是借 Muni 的，错了；Session 2 的 T3 是对的）。输出的 .md 有四段：Data Checks、Portfolio Stress PnL by Scenario、Estimated Stress PnL by Currency Pair、Change in Estimated Stress PnL。
- Flow 名字：Portfolio Analysis / Detail Analysis / Ad-hoc（FXO 的 BAU Investigation 属于 Ad-hoc）。

---

## 3. 固定规则

**合作方式**
- 用户喜欢**先讨论场景和顺序再动手**（"你先别动手，先想想……"）。用户说"你先试试"时就直接做一版。
- **一次一个 beat**；中文解释；用户解释意图的话**不是**要写进稿子的文字。
- 一节内容可以占好几拍（展示一拍、滚动一拍都可以）。
- 改完要截图检查（`stills.mjs`、`sheet.mjs` 拼图、`livekeys.mjs` 走一遍停顿点、`errs.mjs` 看报错），说清楚检查了什么。
- 每次决定都更新记忆 `riskmind-session3.md`（更新当前状态，不写长改动记录）。

**讲稿用词**（v5 §3，没变）：短句、少冒号、少 "you"、不说 "replaces"、What-if Analysis、Scripts（不是 code）……Session 1–2 不说 "Progressive Disclosure"，留给 Session 3。

**Session 3 的视觉规则**（这些都是用户在 2026-11-22/23 定的）
- 风格沿用 Session 2：白底、蓝色系、DM Sans（屏幕大字）、DM Mono（文件路径、代码、markdown 原文）；卡片 `rx 18`、浅灰边。
- **SKILL.md 用"编辑器里的原始 markdown"样式显示**：`##`/`###` 灰色、标题用 DM Sans 加粗；`**` 和反引号灰色，粗体字 600，代码字蓝色 `#1C5BB5`；代码块浅灰底 `#F1F4F8`。
- **折叠的标题只显示箭头和一个小的 "⋯"，永远不显示行数**（用户：行数没有意义）。
- 不要旗标/吊牌之类的旁注（试过，删了），靠高亮和旁白讲。
- 高亮用浅蓝底 `#DFEBFC`（像荧光笔），只高亮要点。
- 三栏场景里**不要横向连线**（用户：丑，观众看得懂）。
- 转场要**一步一步来，不要一堆东西同时飞**；换屏要带一个元素过去。
- 用户不喜欢"before/after 对比"做主线（Scripts 那一节明确否掉了）。

---

## 4. Session 3 视频的技术说明

**引擎**（和 Session 2 一样）
- `render(t)` 只根据时间画每一帧，没有 CSS transition、没有 timer。现在是 `render(t){renderOpening(t);renderMD(t);renderFlow(t);renderScripts(t);}`，**后面的函数会覆盖前面函数设的属性**（比如 renderFlow 在三栏场景里把 mdG 隐藏、renderScripts 重新定 file 的位置和缩放）。
- 时间点都在 `OP` 对象里；停顿点在 `STOPS`；章节名在 `window.CHAPTERS`；`TOTAL` 是总时长。
- 操作：Space 播放/暂停（到停顿点自动停）、← / → 落在停顿点、Home 回开头、F 全屏。导出：`?export=1`，然后 `window.renderAt(t)`。
- 舞台 1920×1080。常用 helper：`pr`（进度）、`eo`/`eio`（缓动）、`lerp`、`mixc`（颜色插值）、`op`（透明度，0 时 display:none）、`sv`/`G`（建元素）、`icon`（Lucide 图标表 `LUCIDE`）、`tileAt0`（图标块）。
- 字体加载后要重新测量：`layoutDef();layoutSkDef();pjWrap();mdMeasure();mdTags();flagWrap();flMeasure();` 在初始化和 `document.fonts.ready` 时各跑一次。

**SKILL.md 文件卡片**
- `MD={x1:560,x2:1860,...,fs:21,lh:33}`；`mdG`（整张卡片）→ `mdClip` → `mdView`（滚动就是平移它）。`mdWidth(x2)`、`mdHeight(h)` 改卡片尺寸。
- 正文各节用 `mkRows(SRC)` → `mkY(rows,y0)` → `mkEls(rows,Y,group)` 生成；SRC 的行类型：`{runs,hang,tailBar}`、`{h3,fold}`、`{code,fence}`、`{bar}`、`{}`（空行）。runs 的样式码：`''` 正文、`m` 灰色标记、`b` 粗体、`c` 代码、`i` 斜体。
- 五个 `##` 折叠行是 `mdFoldRows`，位置 `foldY(k)`；展开某节时，后面各节靠 transform 往下推（`BB_PUSH`、`AS_PUSH`、`PF_PUSH`、`S2_PUSH`…），收起靠 `LEAD_H`、`DESC_H`。
- 宽版文件（Business Background 收起那一拍起）：左边缘 560→60、上下各多 28px，Analysis Steps 和 Portfolio 按 135 列排版（`MD_WCOLS`）。

**navigator**
- `NAV_P`（Plugin 节）、`NAV_S`（Skill 节）、`NYS_S`（各行的 y）；`navWraps` 是给 navigator 各块套的外层 `<g>`，用来整体平移/滑出而不碰它们自己的 transform。Scripts 节用 `NYS_C` 重新排版，scripts 的子项在 `navCh`。

**三栏场景**（`renderFlow`）
- `FL` 是布局常量；左框 `FLL`、右框 `FLR`、中间 `flMid`（Agent 虚线框 + 五个 pill）、标题副本在 `flHeads`（右栏在 `flRight`，带裁切）。手风琴高度由 `flState(k)` / `flLayout(t)` 算。

**检查工具**（`.render/`，Playwright）
- `node .render/stills.mjs "<html 绝对路径>" <输出文件夹> t1 t2 …`：截图。
- `node .render/sheet.mjs "<截图文件夹绝对路径>" "<输出 png>" 0 9 3`：拼成一张对比图。
- `node .render/livekeys.mjs "<html>" <输出 png> ArrowRight ArrowRight …`：模拟按键，输出页面报错（`none` 表示没有）。
- `node .render/errs.mjs "<html>"`：页面报错。`tval.mjs` / `tval2.mjs`（后者等字体加载完）：在页面里求表达式，比如 `"[OP.mdAS,STOPS.length]"`。
- Chromium 路径写在脚本里；没有 PIL（拼图用 sheet.mjs，裁图用 `sips`）；长正则用 `python3` 而不是 grep。

---

## 5. 当前状态

### Session 1 — 定稿
没变，见 v5 §5（几个待修的小问题、Demo 接进 beat 26）。

### Session 2（Agent）— 定稿
2026-11-21 定稿。Session 3 引用 Session 2 的内容时，以定稿版为准。

### Session 3（Plugin）— 视频做到 Scripts 一半（67.55 s，32 个停顿点）

**主线**（用户 2026-11-22 定）：主线就是 `fxo-plugin` 文件夹。开场 logo → 四个圈 → 一条线到三个 plugin 文件夹 → 点 fxo-plugin，它的三部分（`.claude-plugin`、`skills`、`.mcp.json`）就是**间隔页**；Plugin、Skill、MCP 三节都从这个间隔页点进去；Shared Library 从 plugins 那一排开始。例子固定用 FXO，flow 例子用 Portfolio。

**已经做好的停顿点**（时间 · 章节）

| 时间 | 内容 |
|---|---|
| 0 | RiskMind logo |
| 6.80 | 点 logo → 四个圈（只亮最外圈 Business Plugin）→ 圈左移，一条线到卡片，卡片上是 Agent SDK 的 plugin 定义（"Plugins let you extend Agent with custom functionality … A plugin can include:" + 四条列表），"local directories"、"add capabilities" 高亮 |
| 8.50 | 卡片下面长出虚线，标签 `plugins`，三个 plugin 文件夹 |
| 11.90 | 点 fxo-plugin → 它变成标签，三部分进来（间隔页，圈留着） |
| 14.10 | 列表里的 Skills、MCP servers 字变蓝 → 飞下来变成 chip，落在 `skills`、`.mcp.json` 上 |
| 18.35 | 点 `.claude-plugin` → 变成左边的 navigator；右边 `<plugin folder>/.claude-plugin/plugin.json` 卡片，三个字段先显示官方说明 |
| 19.75 | 换成真实值，标题变成 `fxo-plugin/.claude-plugin/plugin.json` |
| 22.60 | navigator 原路回到间隔页，只高亮定义里的 Skills 那一行 |
| 25.75 | 点 skills → Skill 间隔页：定义换成 Agent Skills（"…organized folders of instructions, scripts, and resources that agents can discover and load dynamically…"），"discover and load dynamically" 高亮；`skills/fxo-stress-pnl` 下面是 SKILL.md 和 scripts |
| 27.85 | "instructions"、"scripts" 变蓝，飞下来变成 chip，落在 SKILL.md、scripts 上 |
| 29.90 | 变成 Skill 的 navigator |
| 31.70 | SKILL.md 文件卡片打开（YAML + 正文开头） |
| 32.80 | YAML 部分保持清楚，正文变淡变模糊 |
| 33.80 / 34.80 / 35.80 | 依次高亮 name、description 的"做什么"、"什么时候用" |
| 37.80 | 正文全部清楚，滚到 `# FXO Stress PnL`，折叠成五个 `##` |
| 39.70 | 展开 Business Background（用户定的摘录，灰色占位条表示还有内容） |
| 42.70 | Business Background 收起的同时，文件变宽变高、把 navigator 推出去；Analysis Steps 和 Slash Command（Portfolio）**一起展开**，一屏放得下 |
| 45.90 | 三栏：两节先收成只剩标题 → Portfolio 整块先往右、再往上移到旁边 → 框从中间裂开，各行对齐中间 Session 1 的 pipeline（Agent 虚线框，五个等宽 pill：Get Data / Analyze / Write Comments / Build Dashboard / Dashboard） |
| 47.30–52.90 | 手风琴，一步一停：左边 Analysis Steps、右边 Portfolio 的同一步一起展开，中间 pill 亮；打开的行按内容定高，其他行让开、标题始终对齐自己的 pill |
| 55.30 | 关上 Step 5；右框像同一个文件那样：Portfolio 收进标题 → Detail、BAU 标题升上来 → 滚动 → Detail 展开（三个 step + Steps 3–5 下的 `**Step 3/4/5**` 三行） |
| 57.10 | 同样换到 BAU |
| 61.35 | 回去：BAU 收起 → 滚回三个折叠大标题 → 中间 Agent 淡出、两框合拢 → 三个标题接回 Analysis Steps 下面 → 文件缩回、navigator 回来。最后：Analysis Steps 五个 step + 三个折叠的 flow 标题 |
| 63.15 | Scripts 场景 0：scripts 直接展开（不点击），上面几行往上推，列出真实子项（§2） |
| 65.15 | Scripts 场景 2：Analysis Steps 收起，Slash Command 展开、只打开 Step 2（真实命令），滚到 Slash 在最上 |
| 65.85 | navigator 里 `portfolio_analysis.py` 亮起，同时 SKILL.md 里 `uv run …/portfolio_analysis.py \` 那一行高亮 |
| 67.55 | navigator 滑出；SKILL.md（左，82%）和脚本卡片 `fxo-stress-pnl/scripts/portfolio_analysis.py`（右，同样缩放）并排。**脚本卡片现在是灰色占位条** |

**三栏里显示的内容**（用户审过一轮，之后还要再审）
- 左框（Analysis Steps 每步展开）：Step 1 = 导语 + `row_count: 0`、`pending_dates` 两条 bullet；Step 2 = "Run the flow's analysis script…"；Step 3 = 用户改写的那段 + 两条 bullet（keys 要对上、用 display names）；Step 4 = figures 命令；Step 5 = "Follow "With Script Generated Components" step 4 in `CLAUDE.md`…"。
- 右框（Portfolio）：Step 1 = 8 行 `get_query_data` + "You need 8 `file_download_link` URLs…"；Step 2 = "Pass the MCP download URLs directly…" + 13 行命令 + 四段 .md 名字；Steps 3–5 = `**Step 3**: text JSON.`（说明 + 截短的 json 模板）、`**Step 4**: Figures.`、`**Step 5**: Render.`。

**备份**：`.render/s3v-before-*.html`、`s3v-flowscene-v1/v2-*.html` 等（75 个左右），最新的是 `s3v-before-uvhl-2026-11-23.html`。

---

## 6. 下一步（建议顺序）

1. **Scripts 收尾**：等用户给 `portfolio_analysis.py` 的内容，替换右边的占位条，然后加拍子展示两点：
   - 所有输入都是命令行参数（脚本里的参数定义对上左边命令里的参数）；
   - 它是触发点，调用 `analysis/` 文件夹里的代码（navigator 已经滑出去了，打算用脚本里的 import 行来表现；要不要临时把 navigator 拉回来点亮 `analysis/`，看到内容再定）；
   - 然后展示输出（.md 给 LLM 读、.json 给 figures 脚本）。
   - 用户说重点是 Step 2 和 **Step 4**，所以 Step 4 的 `generate_portfolio_figures.py` 可能还要一段。
2. **MCP 节**：从间隔页点 `.mcp.json` 进入。要讲 MCP 是什么（回扣 Session 1 的 "Data Connection" 并纠正）、Gateway、ATOM MCP server 的两个 tool、query catalog（单独设计；"三个约定"大概率挪到这里）。旧 Outline 卡片 5、6 有素材（MCP 官方原文已核对）。
3. **Shared Library**：等团队定稿 `.market-risk-base`。
4. **框架页**：封面、课程页、结束页、takeaways，照 Session 1、2 的样子。
5. **回头 review**：三栏里 Analysis Steps 和 Portfolio 的显示内容（用户说等后面做完再一步一步看）。
6. **两个待定**：要不要在画面上点出 "Progressive Disclosure" 这个名字（现在靠旁白；原来写"所有 skill 都先读 metadata、选中才读正文"的旗标已经删了）；"怎么写一个 skill"的指导放旁白还是 takeaways。
7. 最后：按 HTML 重写 outline，再写讲稿（中文一拍一拍过）。

---

## 7. 链接和记忆

线上页面停在旧版本，**不要更新**（链接见 v5 §7）。

记忆文件：
- `~/.claude/projects/-Users-shuangdu/memory/`：`riskmind-session3.md`（**Session 3 的事实和每一段的决定，最详细**）、`riskmind-session1-video.md`、`riskmind-session2-video.md`、`riskmind-session2-decisions.md`、`riskmind-video-style.md`
- `~/.claude/projects/-Users-shuangdu-Downloads-RiskMind-Video/memory/`：`riskmind-memory-location.md`（指向上面那个文件夹和最新 HANDOFF）、`talk-track-review-feedback.md`（review talk track 的方式）
