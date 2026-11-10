# RiskMind 培训材料 — 合并交接文档(Session 1 / 2 / 3)

写于 2026-11-07(当天稍后更新了文件夹路径和提词器相关说明)。合并了两份交接:
(a) 文件夹里的 `HANDOFF.md`(现在是 `Handoff Notes/HANDOFF v1.md`;只讲 Session 1 的视频、讲稿、outline、提词器怎么维护);
(b) 云端 chat 的交接(讲 outline 的整理过程、规则、Session 2/3 的状态)。
给接手的 Claude session 看。**对话用中文,文件内容(屏幕文字、talk track、outline)用英文。**

项目文件夹:`~/Downloads/RiskMind Video/`(以下简称"文件夹")。用户已给过这个文件夹的访问授权的话可直接读;换了 session 要重新请求访问。

---

## 0. 先看这几点(最容易踩的坑)

1. **文件夹结构变了,旧交接里的路径要对照现状。** 现在是:
   - 根目录:`Handoff Notes/`(HANDOFF v1 = 原文件夹 `HANDOFF.md`,v2 = 云端 chat 的交接,v3 = 本文档)、`README.md`、`build_prompter.py`、`assets/`、`.render/`、`Session 1/`、`Session 2/`、`Session 3/`
   - `Session 1/`:`RiskMind Session 1.html`(视频)、`RiskMind Session 1 — Video Script.md`(讲稿本地副本)、`RiskMind Session 1 Prompter.html`(提词器)、`RiskMind Session1 Outline.html`(outline,文件名里是 `Session1` 无空格、无下划线)
   - `Session 2/`:`RiskMind Session 2.html`(视频,已有)、`RiskMind Session 2 Outline.html`(旧格式)
   - `Session 3/`:只有 `RiskMind Session 3 Outline.html`(旧格式),**没有视频**
   - **2026-11-07 已更新到新结构**:`build_prompter.py` 默认读 `Session 1/RiskMind Session1 Outline.html`,写 `Session 1/RiskMind Session 1 Prompter.html`;`README.md` 和提词器开头的注释也已改好。生成提词器只要:
     ```bash
     cd ~/Downloads/"RiskMind Video"
     python3 -I build_prompter.py
     ```
     (从哪个目录跑都行;两个文件任一不存在会直接报 `outline not found` / `prompter not found`。文件改名或挪走时传两个路径:`python3 -I build_prompter.py "<outline>" "<prompter>"`,只传 outline 不够。)
   - 仍是旧名/旧路径的只有 `Handoff Notes/HANDOFF v1.md`、`v2.md` 里写的 `RiskMind_Session1_Outline.html`、`~/Downloads/RiskMind Session 1 Video/`、`.render/build_prompter.py`,以本文档为准。**改任何东西之前先 `ls` 一遍,别信旧路径。**
2. **云端 chat 里用来生成 Session 1 outline 的 markdown 源文件和脚本都丢了(容器被替换)。** 现在 Session 1 outline 的唯一源头就是文件夹里的 outline HTML(它和线上页面 v92 一致,1,276,979 字节)。**以后直接改 HTML**(用 Python 按 `<tr>` 定位替换),不要再走 md → 生成 HTML 的流程。线上页面 https://claude.ai/artifact/FZYXQf3QTiHxwkbDAnWumF 是同一份内容的副本,改完文件夹里的 HTML 后可再发布同步。
3. **Session 1 outline 现在有格式约束**:`build_prompter.py` 严格按行解析 — 每个断点一行 `<tr>`,标签后面必须正好 4 个 `<td>`(Visual · On-screen text · Caption · Reference);Reference 里每条用 `•` 开头、`<br>` 分行;行数必须 = 停顿点数 + 2(Cover、Course、1–43 共 45 行)。**改 outline 不能破坏这个格式**,改完要重新生成提词器,应输出 `12 scenes, 45 beats (Cover, Course, 1 … 43)`。
   - 标签格式是 `<标签> · <秒数>s`(中间是 ` · `),标签可以是数字或单词。**第一行标签是单词(Cover)就当作封面**:t=0 还没播时的画面;之后每一行对应视频里"上一个停顿点 → 下一个停顿点"的一段,按顺序对应,不看秒数。所以下面"待修的小问题"第 2 项改时间标签不会影响提词器。
   - 行数对不上时,提词器连上视频后顶部会出黄色警告。
4. **Session 2 已经有视频,但没有讲稿、outline(新格式)和提词器;Session 3 连视频都还没有。** 云端 chat 之前以为 Session 2、3 的视频是"之后做",实际 Session 2 视频已经做了(`.render/` 里有大量 `s2-before-*.html` 备份,改过很多轮)。**Session 2 的内容必须以它的视频 HTML 为准**,旧的 outline 要按视频重做。
5. 用户的 Mac 上有记忆文件(`~/.claude/projects/-Users-shuangdu/memory/`):`riskmind-session1-video.md`(Session 1 改动历史)、`riskmind-session2-video.md`(Session 2 改动记录)、`riskmind-video-style.md`、`MEMORY.md`。如果在本机 Claude Code 里继续,先读它们;在云端 chat 里读不到,需要的话让用户把 `riskmind-session2-video.md` 发过来。

---

## 1. 项目是什么

RiskMind = Agent(基于 Claude Agent SDK)+ Plugin(Skills + MCP),用于 Market Risk。培训分三节,每节约 45 分钟,另留 15–20 分钟 Q&A:

| Session | 主题 | 课程页上的日期 |
|---|---|---|
| Session 1 | RiskMind(Introduction) | November 12 |
| Session 2 | Agent | November 20 |
| Session 3 | Plugin | November 27 |

观众:Senior Managers 和 Local Risk Managers,懂业务,不一定懂 AI 术语。

**Session 1 是视频**,用户在浏览器里现场边放边讲:Space 播到下一个断点后自动暂停,用户在断点处讲。提词器(`Session 1/RiskMind Session 1 Prompter.html`)驱动演示窗口,同时显示 talk track 和 Reference。之后可能再做配音版。

产品事实:
- 1 个产品 = 1 个 plugin;1 个指标/分析 = 1 个 skill(**只口头讲,不写在屏幕上**)。
- 共享知识放在 plugins 的上级目录 `plugins/reference/`(Shared Library)。
- Skill Tooling:AutoEval → AutoSkill → AutoEvolution。
- 团队(最新视频):**Local Market Risk**(AI Champions 写 Skills)、**Market Risk AI × AiXel**(搭 Agent 和数据连接,并支持 Local Market Risk)。旧名 "Agent Serving Team (Enterprise AIXel)" ↔ AiXel 的对应关系我提过,**用户没有明确确认**。
- 定位页坐标:Chat / Augmented LLM | 虚线 | Agentic Systems;Prompt Chaining 和 Autonomous Agent 是 pattern(虚线),不是产品;RBC Assist Pro = augmented LLM,DocuMind = workflow,RiskMind = agent。蓝 = Vertical,RBC 黄 = Horizontal。定义和框架来自 Anthropic "Building effective agents",agent loop 引 ReAct(arXiv 2210.03629)。引文和链接保留在 Reference 栏。
- Today vs. With RiskMind:自动化轴(All Manual / Today / With RiskMind / Fully Automatic)+ effort bar(**Design · Execution · Judgement**)。Judgement 始终属于 Risk Manager,不缩;With RiskMind 时 Execution 大幅缩短、Design 变宽(一次性成本)、左侧约半条是 Saved Effort。角色变化:从"每次做分析"到"设计一次、每次判断"。
- Pipeline:Get Data / Analyze / Build Dashboard 由 **Scripts** 跑;Write Comments / Write Answer 由 **LLM** 写。原则:**Numbers from Scripts, Words from the LLM**。
- Session 2 中的 "Business Plugin" 是用户确定的措辞。

---

## 2. 固定规则(两份交接合并;用户反复强调)

**合作方式**
- 一次只做一张 slide / 一个 session,**动手前先问问题**;用户常说"先别动手,先说说"。改动小、意思明确时直接改。
- 用户逐个 session、逐个断点 review;还会对每个 session 的 caption 做细节 review。
- 每次改 HTML **先备份**:`cp "<file>.html" .render/before-<名字>.html`。
- 每次改完**截图给用户看**(SendUserFile),并说明检查了什么、没检查什么(例如"只看了静止帧,没完整播放")。
- 渲染后检查再发布;md/页面/outline/讲稿保持同步。
- 在记忆文件末尾追加一行改动记录(本机 Claude Code 里做)。
- 下载链接/文件**只在用户要时才给**。

**内容规则**
- 官方来源要**逐字引用并带链接**(Harness 页和旧 workflow 页除外)。
- **不提早期尝试和失败案例。**
- **不说 RiskMind "replaces" 任何东西**;RiskMind 不替代 Official Risk Report,Risk Manager 仍要 review 它的产出。
- 用词:Judgement(不是 Verification)、Scripts(不是 code)、Digitize(不是 digitalize)、AiXel(不是 AIXel)、What-if Analysis(不是 Sensitivities)、Dashboard(统一叫法)、Answer in Chat(不是 Direct Answer)、Standard Operating Procedure(不是 Operational Manual)。
- 讲 key person risk 时说"人员变动时知识留在团队里",不直接提离职。
- 秒数以真实 HTML 为准;讲稿和 outline 的时间标签规则:"N · Xs" = 这一段**开始播放**的时刻(即上一个停顿点)。

**视频风格**
- 屏幕文字英文;大字每个单词首字母大写、不加句号;小字只大写句首;字体 DM Sans。
- 只用蓝色系;唯一例外是 Horizontal 用 RBC 黄(底 #FCF5DA、边 #DDBB4C、字 #8A6D12);Vertical 和 RiskMind 用蓝(#1C5BB5,强调词 #1A73E8)。**不用绿色**;deck 里的 teal/紫色搬进视频要改成蓝色系。
- 多行文字左对齐;卡片里的描述居中。
- 换屏要带一个元素过去,不硬切;动作连贯;飞行距离别太远。
- 不要像 PPT:避免大标题加几行字、填色方框、表格。
- 三个转场页(GRM AI Vision、Positioning、Key Takeaways)一行阶段统一:logo 高 108,名字 60.5px,后面那句 50px,中间空 44;RBC 盾牌和文字之间 32。
- 尽量少放屏幕文字,能口头讲的就不放。

---

## 3. 文件之间的关系和维护流程

视频已定稿,进入修改阶段,方向是:

```
视频 HTML(最终以它为准)
   ↓ ① 改完视频
讲稿(claude.ai Doc,中文画面描述 + 英文 talk track)   ② 按视频同步
   ↓ 本地副本 RiskMind Session 1 — Video Script.md
Outline HTML(英文 + Reference + 每场截图)             ③ 按讲稿和视频同步
   ↓ ④ python3 -I build_prompter.py(在 `RiskMind Video/` 下跑)
Prompter HTML(演讲时用,不要手改)
```

**提词器怎么和视频同步**(改视频 HTML 时要知道):
- 视频 HTML `<script>` 的最后有一段 `// ---------- prompter sync ----------`(外加 PageDown/PageUp 两个键)。**改视频时不要删它**;如果整份 HTML 重写或从备份恢复,要确认这段还在(`grep -c "prompter sync"` 应为 1)。加这段之前的备份是 `.render/before-prompter-sync.html`。
- 两个窗口通过 BroadcastChannel `rm-s1` 通信;提词器用 "Open Presentation Window" 打开视频时还会走 postMessage。视频是时钟的主人,提词器只发命令(advance / back / home / toggle / seek)并显示视频报回来的时间。
- 提词器右侧的小预览是 iframe 里的 `RiskMind Session 1.html?export=1&mirror=1`,所以**两个 HTML 必须放在同一个文件夹**(都在 `Session 1/`)。
- `build_prompter.py` 只替换提词器里的 `<script id="beats">` 那一块,其他部分(界面、同步逻辑)要改的话直接改提词器 HTML;界面文字全是英文(用户要求)。

- 讲稿 Doc:https://claude.ai/artifact/64pG6b9JRMpeXa4JwrZEtD ,Doc id `29060cbf-457a-46b9-be58-5e0045838dfe`,根节点 `4c0ec995-28c2`,最新 rev 595(其间可能又有修改,先读最新版)。读写方法见 `Handoff Notes/HANDOFF v1.md` 第 5 节(read 用 ref {"object":"node",...} + container {"kind":"project","id":"29060cbf-457a-46b9-be58-5e0045838dfe"};写用 update + payload.ops;**id 要带 `mvehed4ek7e.` 前缀写全**;整篇输出超限会存成文件,用 jq/Python 解析)。
- 讲稿和 outline 内容基本重复,**每次改动要同步两份**(用户的习惯,不要擅自合并;用户嫌麻烦可建议简化)。
- 历史顺序(用户说明):先和用户确认 outline → 做视频 → 按视频写讲稿 → 回头按讲稿和 HTML 更新 outline。新增内容(例如 Session 2 预告卡)可沿用这个顺序。

**每次改动的标准流程**:备份 → 改 HTML → 检查(报错、截图、`BEATS`/`DURATION`)→ 同步讲稿 Doc → 同步 outline(画面变化明显时重拍截图)→ 重新生成提词器 → 同步本地 `Video Script.md` → 记录。

**视频 HTML 结构**(Session 1):全局时钟 `T`,`window.renderAt(t)` 渲染第 t 秒;按 Space 播到下一个停顿点;`COVER = 3.2`,`INTRO = 12.3`,`DURATION = 133.2`;模块 S0(封面/课程页)、S1(GRM AI Vision)、S2(轴)、定位页、S4(Today/With RiskMind)、S3(Agent + Plugin)、S5(pipeline)、Demo 占位、S6(Why RiskMind)、S8(Expansion → 收拢 → Key Takeaways → 结束页)。详细表在 `Handoff Notes/HANDOFF v1.md` 第 4 节。

**检查工具**:`.render/` 里有 Mac 本机的 Playwright 脚本(`stills.mjs`、`tval.mjs`、`errs.mjs`、`alltext.mjs`、`livekeys.mjs`,浏览器路径写死在 `~/Library/Caches/ms-playwright/…`,文件参数用绝对路径,每次截图用新文件夹)。**在云端 chat 里这些不能直接用**:把 HTML 取到容器后,用 Python Playwright 打开 `file://…html?export=1`,调用 `window.renderAt(t)` 截 1920×1080 再缩成 1280×720 JPEG;字体 DM Sans 要本地路由(npm 装 `@fontsource/dm-sans`)。云端 chat 用过的场景截图时间(末尾取下一个断点前约 0.15 秒):intro 14.65、landscape 56.0、positioning 66.25、today 72.45、with RiskMind 76.55、agent+plugin 84.35、pipeline 96.15、demo 97.55、why 108.95、PoC→production 112.35、expansion 120.55、takeaways 131.05、closing 133.0;cover 在 t=0.1,课程页在 t=2.15。

---

## 4. 当前状态

### Session 1 — 内容定稿,正在逐断点 review
- outline 12 张场景卡(Cover and Course Structure;GRM AI Vision and Strategy;AI Tools Landscape;RiskMind Positioning;Today vs. With RiskMind;What RiskMind Is: Agent + Plugin;How a Pipeline Runs;Demo;Why RiskMind;From Proof of Concept to Production;Expansion;Key Takeaways),共 45 行(Cover、Course、1–43),总长 133.2 秒。
- **用户的 review 计划**:从断点 6(axis 出现,14.8s)开始逐个 review 要讲的内容,前面的封面、课程页、GRM AI Vision 不是用户要讲的稿子。AI Tools Landscape 这一页有 10 个断点(6–15)。**我已把这 10 条 talk track 列给用户,用户还没有给出任何修改意见——从这里接着做**(talk track 在 outline 的 Caption 栏里,也在讲稿 Doc 里)。
- 待修的小问题:
  1. outline 第 23 段 Caption 错字 "or a answer in chat in chat" → "or an answer in chat"(改后要重新生成提词器)。
  2. 时间标签偏移:课程应为 **0.0s**,断点 1 应为 **2.2s**,其后各行依次改成"上一个停顿点"(Doc、outline、md 都要改;注意 outline 里现在的标签是"该段结束/下一个起点"的旧写法)。
  3. 讲稿 Doc 过时处:Overview "约 116 秒"→133 秒并重算讲稿字数和时长,内容列表补上封面/课程/Key Takeaways/结束页;"数字全部由代码算"→由脚本算;4b 引言 "Direct Answer"→"Answer in Chat";Today 节引言 "Operational Manual"→Standard Operating Procedure;Intro 引言去掉 "GRM AI Vision:" 的冒号并补封面和课程两行;"待做"里 "补第 20 段讲稿" 现在是第 26 段(Demo)。
  4. 检查 outline 里的截图是否最新(Key Takeaways、结束页、收拢转场)。云端 chat 已在最新 HTML 上重拍过,但只逐张核对了封面、课程页、结束页和 Take Away 页。
  5. 云端 chat 写的 beat 39–43 的 Visual 描述来自 script,没有逐帧对照视频,review 时核对。
- 待办(内容):Demo 的 caption 为空,Demo 录好后替换第 26 段占位画面并补讲稿,同时确认录屏里的真实报告是否需要脱敏;"Session 2 预告卡"没做,片尾现在是结束页(Market Risk · RiskMind · AiXel),**要不要加,问用户**;deck outline(PPT,不在文件夹里)要去掉 "replaces the existing risk report",Expansion 页按视频版本调整。

### Session 2(Agent) — 视频已有,讲稿/outline/提词器缺
- `Session 2/RiskMind Session 2.html`(约 186 KB)是最新视频;`Session 2 Outline.html` 是旧的四张幻灯片格式(Agent Introduction、Agent Harness、RiskMind Customization on Agent Harness、Why Agent + Plugin Decoupling),**可能已与视频不一致**。
- 需要做:读视频 HTML(提取每个停顿点的画面、On-screen text,可用 `alltext.mjs` 或自己的 Python 脚本)→ 先和用户确定内容 → 写成与 Session 1 同格式的断点表(Beat · Visual · On-screen text · Caption · Reference,Caption/Reference 不丢旧内容信息)→ 用户 review → 再决定是否做讲稿 Doc 和提词器。如果要给 Session 2 做提词器:`build_prompter.py` 的默认路径写死在 Session 1(可以传两个路径参数,或泛化);视频 HTML 要加同样的 prompter sync 段;频道名 `rm-s1` 和 `rm-s1-*` 本地存储键在两个文件里都是写死的,要换成 Session 2 自己的,免得两节同时开着时互相干扰。
- 沿用 Session 1 的做法:每页一张完整场景截图,时间以视频 HTML 为准。
- Session 2 的 outline 里还有 "Sensitivities" 要改成 What-if Analysis。

### Session 3(Plugin) — 只有旧 outline,无视频
- 已起草的 slide:Plugin Introduction、Skill Introduction;Skill Walk Through 和 MCP Introduction **暂停**。
- **两个卡点(需要用户提供信息)**:
  1. **Shared Library 怎么运作**:用户说大约知道了,但还没写给我(共享知识在 `plugins/reference/`)。
  2. **Skill 中具体抽出哪些内容、剩下什么**:用户自己也还没完全搞清楚,等 skill 重构 / 代码核对后再定。Skill Walk Through 和 MCP Introduction 等这一项。
- 旧 outline 里也有 "Sensitivities",要改。
- 约定:先做 Plugin 内容,再回头做 Session 2、3 的视频,最后连起来时加课程结构和 session 之间的过渡(Session 1 的 Cover/Course 两个 beat 已有课程结构,用户之后会再定稿)。

---

## 5. 下一步计划(建议顺序)

**第一阶段 — Session 1 review(用户在场,逐断点)**
1. 从断点 6 开始逐个 review talk track:每个断点用户说意见,Claude 直接改(outline 的 Caption/Reference;讲稿 Doc 同步);用户说"先别动手"的就先讨论。
2. review 完成后一次性处理上面"待修的小问题"第 1–5 项(错字、时间标签、讲稿 Doc 过时处、截图核对),重新生成提词器并检查 `12 scenes, 45 beats` 输出,发布线上页面同步。

**第二阶段 — Session 2(视频已有,补内容)**
3. 读 Session 2 视频 HTML,列出所有停顿点和对应画面/文字,先把"视频里实际有哪些幻灯片和断点"报给用户确认。
4. 与用户确定内容 → 写新格式断点表 → 用户 review → 同步到讲稿 Doc / 提词器(按用户要不要)。
5. 把 Session 2 outline 里的 "Sensitivities" 改成 What-if Analysis。

**第三阶段 — Session 3(Plugin)**
6. 向用户要两个卡点的信息:Shared Library 的实际操作方式;Skill 重构后抽出什么、剩下什么。
7. 完成 Plugin Introduction、Skill Introduction;转成断点表;Skill Walk Through 和 MCP Introduction 等代码核对后再写。
8. 之后再做 Session 3 视频(用户还没开始)。

**第四阶段 — 串起来**
9. 三节视频都有之后:课程结构和 session 之间的过渡;决定是否加"Session 2 预告卡";补 Demo 的 caption 和占位画面;更新 deck outline(PPT)。

**需要用户拍板的问题**
- 先做哪个:Session 1 review,还是先读 Session 2 视频(我建议先 Session 1 review,因为已经在中途)。
- 要不要在 Session 1 片尾加 Session 2 预告卡。
- AiXel 和旧名 "Agent Serving" 是否同一个团队。
- Session 2 要不要也做讲稿 Doc 和提词器,还是只做 outline。
- 讲稿 Doc 和 outline 要不要继续同步两份(HANDOFF 里说这是用户目前的习惯)。

---

## 6. 链接和文件

线上页面(私有,用 Artifact 工具 `url` 原地更新):
- Session 1 outline:https://claude.ai/artifact/FZYXQf3QTiHxwkbDAnWumF(v92)
- Session 2 outline(旧格式):https://claude.ai/artifact/LkLWhxi1SCE4WTVqAYG1Wz
- Session 3 outline(旧格式):https://claude.ai/artifact/7t6EW7JbvMi1MWbWcHT1SL
- 视频讲稿 Doc:https://claude.ai/artifact/64pG6b9JRMpeXa4JwrZEtD

注意:Session 2、3 的线上页面是云端 chat 发布的旧格式页面,**文件夹里的 outline 可能比线上页面新**(文件夹里 Session 2 outline 是 34,554 字节,云端 chat 发布的约 34,006 字节),以文件夹里的为准。

云端 chat 的容器里还留着:`/mnt/user-data/outputs/RiskMind_Session1_Outline.html`(单文件版,与文件夹里的 Session 1 outline 一致)和 `RiskMind_Handoff_Note.md`(较早的交接,已被本文档取代)。
