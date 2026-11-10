# RiskMind Session 2 — Video Script

Nov 7, 2026 · 初稿，由视频反推，talk track 待确认

## Overview

一支无旁白的动画视频，你在浏览器里现场边放边讲。动画本身约 154 秒，共 27 段（26 个停顿点）。覆盖 Session 2 的内容：一个 agent 由哪几层组成（Augmented LLM、Agent Harness、RiskMind Customization、Business Plugin），每一层是什么、谁提供；然后用一次真实的定时 run 把这几层串起来；最后回答"为什么要自己做 RiskMind"。

- **文件**：`RiskMind Session 2.html`，和这份讲稿放在同一个文件夹里。用浏览器打开即可播放。
- **观众**：Local Risk Managers 和 Senior Managers，懂业务，不一定懂 AI 术语。听过 Session 1。
- **主线**：把一个 agent 拆成四层，再看 RiskMind 的价值在哪一层。内圈两层（Augmented LLM、Agent Harness）是通用的、横向的，今天由 Claude Agent SDK 提供；外圈两层（RiskMind Customization、Business Plugin）是我们自己的、纵向的：风险管理的服务和风险知识。
- **两个问题**：
  - **Q1，为什么要做 RiskMind**：在结尾用圆圈上色回答：横向的部分可以换，纵向的部分不受影响（decouple）。
  - **Q2，为什么是 Agent + Plugin**：只口头讲，不上屏。在 Augmented LLM 那里提出来，在 run 里回答：第 1 轮说明 skill 只在用到时才加载，第 2 轮说明数据只以文件位置的形式进入 context。
- **不提**：屏幕上和讲稿里都不说 "Claude Code"；不说 "Progressive Disclosure"（那是 Session 3 的内容）；不把 RBC Assist 将来的 agent 放上屏幕（还只是计划）。

### 操作方式

- **空格**：从当前断点播到下一个断点，然后自动暂停。播放中途按空格也能手动暂停。
- **← / →**：跳到上一个或下一个断点。**Home**：回到开头。
- **F 或双击画面**：进入或退出全屏。

### 怎么读下面的表

每一行是一段。"断点"后面的时间是这一段**开始播放**的时刻（也就是上一个停顿点）；"画面"是按空格后、播到下一个断点之前出现的内容；"On-screen text"是这段画面里出现的文字（全部英文）；"Talk track"是你在这一段要讲的英文稿子。

## Augmented LLM

先只看最里面一层：一个能调用工具的 LLM。用 MCP 的例子说明两件事：LLM 本身不记事，每次调用都要把全部 context 重新发一遍；工具定义也要占 context。

| 断点 | 画面 | On-screen text | Talk track |
| --- | --- | --- | --- |
| 1 · 0.0s | 画面左侧出现一个圆：Augmented LLM。右边一张卡片：上面是 Anthropic 的定义，"enhanced with augmentations" 高亮；下面一行写我们用的模型 Claude Sonnet，通过 Lumina Gateway 连接 Model API | "Augmented LLM" · "The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory." · "Anthropic · Building Effective Agents" · "Claude Sonnet" · "Model API, connected through Lumina Gateway" | Last time we saw where RiskMind sits. Today we open it up and look at what an agent is actually made of. We start from the inside: the augmented LLM. In Anthropic's words, it's the basic building block of agentic systems, an LLM enhanced with retrieval, tools and memory. In RiskMind that's Claude Sonnet. We don't host any model ourselves; we call the Model API through Lumina Gateway. |
| 2 · 3.0s | 圆缩进画面底部的进度条（四站：Augmented LLM、Agent Harness、RiskMind Customization、Business Plugin，第一站亮起）。画面中间：User 发出 Prompt，LLM 回一段 Text | "Augmented LLM" · "Agent Harness" · "RiskMind Customization" · "Business Plugin" · "User" · "Prompt" · "LLM" · "Text" · "Here is a summary of …" | We'll go through four layers, and the bar at the bottom keeps track of where we are. At its simplest, an LLM takes a prompt and returns text. That's it. |
| 3 · 8.0s | LLM 上方出现 Context 框（The LLM's Memory）：System Prompt 和 Tool Definitions，里面是六个工具的定义；右边出现 MCP 框，两个 server：FX Option 和 Muni，各三个工具 | "Context · The LLM's Memory" · "System Prompt · instructions" · "Tool Definitions" · "fxo_portfolio · description + input schema" · … · "MCP" · "FX Option" · "Muni" · "fxo_portfolio (date)" · "fxo_drill_down (date, by)" · "fxo_adhoc (question)" · "muni_portfolio" · "muni_drill_down" · "muni_adhoc" | Everything the LLM knows in a call sits in its context: the system prompt with its instructions, and the definitions of the tools it may call. Here the tools come from MCP: two servers, FX Option and Muni, three tools each. Every one of those six definitions takes up room in the context, whether it's used or not. Keep two questions in mind for later: how do we keep the context small, and how much effort does it take to add a new analysis? |
| 4 · 10.6s | Muni 关掉，只剩 FX Option 的工具定义；跑一次 fxo_drill_down：Prompt 进入 context，LLM 发出 Tool Call Request，MCP 返回 Tool Result（一个 HTML 文件位置），LLM 给用户回一段 Text。LLM 下方写着 "Keeps nothing between calls"，context 旁边写 "Sent in full, every call" | "Prompt · from the user" · "Tool Call Request · fxo_drill_down · input" · "Tool Result · HTML location" · "Text · to the user" · "{ "tool": "fxo_drill_down", "input": {…} }" · "Result" · "LLM · Keeps nothing between calls" · "Sent in full, every call" | Switch Muni off, and its tools leave the context. Now one turn: the user asks, the LLM decides to call fxo_drill_down, MCP runs it and returns a result, and the LLM answers. Notice two things. The LLM keeps nothing between calls: every call sends the whole context again. And the context only grows: the prompt, the tool call, the result, all stay in. |

## Agent Harness

第二层：把 LLM 变成 agent 的那一圈。先给定义和它提供的机制，再用电脑做类比（OS / CPU / RAM），最后看 agent loop 怎么跑。

| 断点 | 画面 | On-screen text | Talk track |
| --- | --- | --- | --- |
| 5 · 17.7s | Augmented LLM 外面长出第二圈 Agent Harness（Claude Agent SDK），进度条走到第二站。右边卡片：Anthropic 的定义，"act as an agent" 高亮；下面两组机制：Ready to Use（蓝）：Agent Loop、Core Tools、Memory、Context Management、Permissions；Claude Agent SDK Provides the Mechanism（灰）：System Prompt、Hooks、Skill Loading、MCP Client、Subagents | "Agent Harness" · "Claude Agent SDK" · "An agent harness (or scaffold) is the system that enables a model to act as an agent: it processes inputs, orchestrates tool calls, and returns results." · "Anthropic · Demystifying Evals for AI Agents" · "Ready to Use" · "Agent Loop" · "Core Tools" · "Memory" · "Context Management" · "Permissions" · "Claude Agent SDK Provides the Mechanism" · "System Prompt" · "Hooks" · "Skill Loading" · "MCP Client" · "Subagents" | The second layer is the agent harness: everything around the LLM that turns it into an agent. In RiskMind, the harness is the Claude Agent SDK. Some of what it provides is ready to use as it ships: the agent loop, the core tools, memory, context management and permissions. The rest is mechanism only. The SDK gives us the slot, a system prompt, hooks, skill loading, an MCP client, subagents, but what goes into each slot is up to us. |
| 6 · 24.3s | 切到电脑类比：一个扇形的两层台面，中间写 Agent Harness · OS；上层（蓝）是 Core Tools、Memory、Agent Loop、Context Management、Permissions；下层（灰）是 System Prompt、Hooks、Subagents、MCP Client；台面下方是一块芯片 LLM · CPU 和一条内存 Context Window · RAM | "Agent Harness · OS" · "Core Tools" · "Memory" · "Agent Loop" · "Context Management" · "Permissions" · "System Prompt" · "Hooks" · "Subagents" · "MCP Client" · "LLM · CPU" · "Context Window · RAM" | If this sounds abstract, think of a computer. The LLM is the CPU: it does the thinking. The context window is the RAM: what the CPU can see right now. The harness is the operating system. It runs the loop, manages memory, gives you basic tools, and controls permissions. Same CPU, different operating system, different computer. |
| 7 · 28.1s | 离开类比：CPU、RAM 和 Core Tools 各变成一个方框，带着字飞进 Harness 的详细图：LLM、Context、Tools（Skill、Bash、Read、Edit、Write）。Agent loop 跑三圈：Read、Write、Edit；Edit 那一圈经过 Permissions 检查。Context 里一条条加上 Tool Call Request 和 Tool Result，标题下写着 "Saved as session.jsonl · one file per conversation" | "Context · The LLM's Memory" · "Saved as session.jsonl · one file per conversation" · "System Prompt · first, on every call" · "Tool Definitions · Skill · Bash · Read · Edit · Write" · "Tool Call Request 1 · Read" · "Tool Result 1" · … · "Final Answer · to the user" · "Tools · Core Tools" · "Agent Loop · until no more tool calls" · "Permissions ✓" · "Sent in full, every call" | Here's the harness at work. The LLM decides the next step and asks for a tool: read a file. The harness runs it and appends the result to the context. Then the LLM decides again: write, then edit, and before the edit the harness checks permissions. It keeps looping until the LLM stops asking for tools and gives the final answer. The core tools come from the SDK: Skill, Bash, Read, Edit and Write. RiskMind adds no custom tools of its own. And each conversation is saved as one file, so the agent can pick it up again. |

## RiskMind Customization

第三层：RiskMind 往 harness 的空位里填了什么，以及所有 plugin 共用的平台服务。左边的机制（黄）是 SDK 提供的，右边填进去的东西（蓝）是 RiskMind 做的。

| 断点 | 画面 | On-screen text | Talk track |
| --- | --- | --- | --- |
| 8 · 41.9s | 外面长出第三圈 RiskMind Customization，进度条走到第三站。右边卡片：标题 "What RiskMind customizes, once for every business plugin."；第一组 "Claude Agent SDK Provides the Mechanism（黄）· Filled by RiskMind（蓝）"：System Prompt → CLAUDE.md、Hooks → Bash approval、Skill Loading → render-html、MCP Client → emit_turn_output，Subagents → Data Analyzer · Data Visualization（虚线，PoC 里没上线）；第二组 Platform Services：Workspace、MCP Gateway、Customized Interface、Scheduled Service；第三组 Plugin Lifecycle Management：Evaluation、Monitoring、Version Control、Shared Library，以及虚线的 AutoSkill · AutoEvolution | "RiskMind Customization" · "What RiskMind customizes, once for every business plugin." · "Claude Agent SDK Provides the Mechanism · Filled by RiskMind" · "CLAUDE.md · RiskMind's system prompt" · "Bash approval · Asks the user before every Bash call" · "render-html · Built-in skill for building the HTML report" · "emit_turn_output · Built-in MCP for showing the report in the chat panel" · "Data Analyzer · Data Visualization · Not rolled out in the PoC" · "Platform Services" · "Workspace" · "MCP Gateway" · "Customized Interface" · "Scheduled Service" · "Plugin Lifecycle Management" · "Evaluation" · "Monitoring" · "Version Control" · "Shared Library" · "AutoSkill · AutoEvolution" | The third layer is what we add: RiskMind customization. It's built once and shared by every business plugin. On the left, in yellow, the slots the SDK provides; on the right, in blue, what we put in them. Our system prompt is CLAUDE.md. Our hook asks the user before every Bash call: an approval that must always happen can't be left to the model, so it's done in code. render-html is a skill almost every plugin needs, so it lives here, not in any one plugin. And emit_turn_output shows the report in the chat panel. Subagents are dashed: we haven't rolled them out. Around that sit the platform services, the workspace, the MCP gateway, our interface and the scheduler, and everything we need to manage plugins over time: evaluation, monitoring, version control and a shared library. AutoSkill and AutoEvolution are still to come. |

## Business Plugin

第四层：业务知识。一个 plugin 就是一个文件夹，SDK 把它当作一个整体加载。

| 断点 | 画面 | On-screen text | Talk track |
| --- | --- | --- | --- |
| 9 · 50.1s | 最外面长出第四圈 Business Plugin，进度条走到第四站。右边卡片：Anthropic 的 plugin 定义，"loads as one unit" 高亮；下面 "Claude Agent SDK Provides the Mechanism（黄）· Filled by a Plugin（蓝）"：Hooks、Skill Loading、MCP Client、Subagents 分别对应一个虚线框 One Plugin 里的四样东西：hooks/hooks.json、skills/<name>/SKILL.md、.mcp.json、agents/<name>.md | "Business Plugin" · "A plugin is a directory of hooks, skills, MCP servers, and subagents that the Claude Agent SDK loads as one unit." · "Anthropic · Claude Agent SDK Docs" · "Claude Agent SDK Provides the Mechanism · Filled by a Plugin" · "One Plugin" · "Hooks · hooks/hooks.json" · "Skills · skills/<name>/SKILL.md" · "MCP Servers · .mcp.json" · "Agents · agents/<name>.md" | The outer layer is the business plugin: this is where the risk knowledge lives. A plugin is just a folder of skills, MCP servers, hooks and agents, and the SDK loads it as one unit. We have one plugin per product. The same slots again, but this time filled by the plugin, not by RiskMind. For a Risk Manager, this is the only layer you need to know: adding a new analysis means writing a skill, a SKILL.md and a Python script, inside the plugin. |

## The Run

用一次真实的定时 run（FXO Stress PnL）把四层串起来。先把电脑类比再放一次，这次上面多了一个应用：RiskMind = Customization + Plugin。然后类比里的每个方块带着字飞进 run 的画面。顶部的步骤条一轮一停，Bash 的那几轮会出现 "Approval Hook" 标签。

| 断点 | 画面 | On-screen text | Talk track |
| --- | --- | --- | --- |
| 10 · 55.5s | 电脑类比再出现一次，这次台面上方多了一个窗口 "RiskMind · Application"，里面两块：Customization 和 Plugin，用一根线连到 OS | "Customization" · "Plugin" · "RiskMind · Application" · "Agent Harness · OS" · "LLM · CPU" · "Context Window · RAM" | Back to the computer. If the harness is the operating system, RiskMind is the application running on it: our customization plus the business plugins. Let's watch it run. |
| 11 · 59.4s | 打开 run 的画面：CPU 变成 LLM，RAM 变成左边的 Context 云，Core Tools 变成 Tool Call(s)，Customization 变成右边 Files on Disk 里的 "RiskMind · Built In"（CLAUDE.md、render-html、emit_turn_output），Plugin 变成 "Plugins · One per Product"（FX Option、Muni、IG Canada）。中间是 The Agent · An LLM Running in a Loop。Context 里依次放进 CLAUDE.md、Tool Definitions（Core Tools + MCP）、Skill names and descriptions，最后是定时任务生成的 Prompt | "Context · The LLM's Memory" · "CLAUDE.md · system prompt" · "Tool Definitions · Core Tools + MCP" · "Skill names and descriptions · plugins + render-html" · "Prompt · generated by the schedule" · "/fxo-stress-pnl 2026-08-11 2026-08-10 GLOBALFINANCIALCRISISABS" · "The Agent · An LLM Running in a Loop" · "Agent Loop" · "Tool Call(s)" · "Final Answer" · "Files on Disk" · "RiskMind · Built In" · "Plugins · One per Product" · "Workspace · Files This Run Creates" | This is a scheduled run of the FXO stress P&L analysis. Before the first turn, the context gets our system prompt, the tool definitions, and the names and descriptions of the skills. Only names and descriptions, not the skills themselves. Then the scheduler sends the prompt. A scheduled run is the same as a chat; the only difference is that the prompt is generated in the background instead of typed by a user. |
| 12 · 69.5s | 第 1 轮 · Skill：LLM 决定 "Load the fxo-stress-pnl skill"，调用 Skill 工具；右边 FX Option 的 plugin 打开，露出 SKILL.md 和两个脚本；context 里加一条 "T1 · Skill steps and rules" | "T1 · Skill steps and rules · fxo-stress-pnl" · "Load the fxo-stress-pnl skill" · "skill · SKILL.md" · "portfolio_analysis.py" · "generate_portfolio_figures.py" | Turn one. The LLM sees the prompt, matches it to the fxo-stress-pnl skill, and loads it. Only now do the skill's steps and rules enter the context. That's our answer to the first question: the agent knows every skill by name, but only loads the one it needs. |
| 13 · 75.3s | 第 2 轮 · MCP：取数据；Workspace 里出现 8 个 CSV 文件（fetched by MCP），context 里只加一条 "T2 · Data file locations → 8 CSV paths" | "T2 · Data file locations · → 8 CSV paths" · "8 CSV files · fetched by MCP" | Turn two: fetch the data through MCP. The data lands as eight CSV files in the workspace, and what comes back into the context is only where they are, not the data itself. So the context stays small no matter how big the portfolio is. |
| 14 · 81.1s | 第 3 轮 · Bash（出现 Approval Hook 标签）：运行 portfolio_analysis.py；Workspace 里出现分析结果 .md 和 .json；context 里加 "T3 · Analysis file locations → .md + .json" | "T3 · Analysis file locations · → .md + .json" · "portfolio_analysis _….md" · "portfolio_analysis _….json" · "analysis script" · "Approval Hook" | Turn three runs the analysis script with Bash, and the approval hook asks first. The numbers are calculated by the script, not by the LLM, and written to two files. |
| 15 · 86.9s | 第 4 轮 · Read：读分析结果的 markdown；context 里加 "T4 · Analysis markdown · 9 data checks passed" | "T4 · Analysis markdown · 9 data checks passed · …" | Turn four: the LLM reads the analysis summary, including the data checks. All nine passed. |
| 16 · 92.7s | 第 5 轮 · Bash（Approval Hook）：uuidgen 生成一个 UUID；context 里加 "T5 · UUID" | "T5 · UUID · 9e97706c-ec23-4cdb-bc75-cb2c7121c7a3" | Turn five generates an ID for this report, so all its files belong together. |
| 17 · 98.5s | 第 6 轮 · Write：LLM 写评论和图表标题，存成 _text.json；context 里加 "T6 · Commentary + figure titles · written by the LLM" | "T6 · Commentary + figure titles · written by the LLM" · "9e97706c… _text.json" | Turn six is the only place the LLM writes content: the commentary and the figure titles, based on the numbers it just read. |
| 18 · 104.3s | 第 7 轮 · Bash（Approval Hook）：运行 generate_portfolio_figures.py，生成 _figures.json；context 里只加位置，标着 "not read" | "T7 · Figures location · → _figures.json · not read" · "9e97706c… _figures.json" · "figures script" | Turn seven builds the figures with another script. The LLM doesn't even read them; it only needs to know where they are. |
| 19 · 110.1s | 第 8 轮 · Skill：加载 RiskMind 自带的 render-html skill；context 里加 "T8 · render-html instructions" | "T8 · render-html instructions · render-html" | Turn eight loads a second skill, render-html, which is built into RiskMind. A business skill calling a shared one: that's why render-html sits in our customization layer. |
| 20 · 115.9s | 第 9 轮 · Bash（Approval Hook）：运行 render.py，生成 dashboard 的 .html 和 .json；context 里加 "T9 · Dashboard locations → .html + .json" | "T9 · Dashboard locations · → .html + .json" · "9e97706c….html" · "render script" · "9e97706c….json" | Turn nine renders the dashboard: comments and figures combined into one HTML report. |
| 21 · 121.7s | 第 10 轮 · MCP：emit_turn_output 把 dashboard 显示在聊天面板里；context 里加 "T10 · Dashboard shown"，文件旁标 "Shown as the dashboard" | "T10 · Dashboard shown · emit_turn_output" · "Shown as the dashboard" | Turn ten uses our built-in MCP tool to show the dashboard in the chat panel. |
| 22 · 127.5s | 第 11 轮 · Answer：LLM 判断不再需要调用工具（Done），给出 Final Answer；context 里加 "T11 · Final reply · summary + dashboard" | "Done" · "T11 · Final reply · summary + dashboard" · "Final Answer" | And with no more tools to call, the LLM gives its final answer: a short summary and a link to the dashboard. Eleven turns. The agent decided each step, but the order came from the skill, and every number came from a script. |

## Dashboard

| 断点 | 画面 | On-screen text | Talk track |
| --- | --- | --- | --- |
| 23 · 133.1s | 切到 RiskMind 的界面：左边是这次 run 的聊天记录，列出每一步（Skill、MCP、Bash、Read、Write、render-html、emit_turn_output）和最后的回复；右边是生成的 dashboard "FXO Stress PnL — Global Financial Crisis Absolute"，自动往下滚。底部进度条回来，停在 Business Plugin | "RiskMind · chat" · "/fxo-stress-pnl 2026-08-11 2026-08-10 GLOBALFINANCIALCRISISABS" · "generated by the schedule" · "Global Financial Crisis Absolute: $12.8MM stress profit, up $0.5MM. One flag: BAU and Murex differ by $26.0MM on Rising Rates Risk Off." · "FXO Stress PnL dashboard is ready." · "↗ Open the dashboard" · "FXO Stress PnL — Global Financial Crisis Absolute, 2026-08-11 vs 2026-08-10" · "Summary" · "Stress PnL Estimation by Currency Pair" · "Stress PnL Change by Currency Pair" | And this is what the Risk Manager sees: the run in the chat on the left, and the dashboard on the right. The summary at the top, the figures built by the scripts, and the commentary written by the LLM. Including the flag the data checks raised: BAU and Murex differ on one scenario. |

## Why RiskMind

回答 Q1。四个圈再出现，按横向和纵向上色：内圈两层（黄）是标准化的 agent，今天是 Claude Agent SDK，RiskMind 只是配置它；外圈两层（蓝）是 RiskMind 自己的：风险管理的服务和风险知识。最后演示 decouple：内圈换模型、换 SDK，外圈不变。

| 断点 | 画面 | On-screen text | Talk track |
| --- | --- | --- | --- |
| 24 · 143.1s | 一个球从进度条的 Business Plugin 站点升起，展开成四个圈；最里面的 Augmented LLM 变黄，旁边出现标签 "RBC Assist Pro · Today" | "Augmented LLM" · "Agent Harness" · "RiskMind Customization" · "Business Plugin" · "RBC Assist Pro" · "Today" | So why did we build RiskMind? Back to the four layers. Remember from last time: RBC Assist Pro today is an augmented LLM, the inner circle. |
| 25 · 145.7s | 标签收回，四个圈移到中间；第二圈 Agent Harness 也变黄；下方出现图例 "Standardized Agent · Horizontal" | "Standardized Agent" · "Horizontal" | Add the harness, and you have a standardized agent. That part is horizontal: it's not specific to risk, and today we take it as it is from the Claude Agent SDK. We only configure it. |
| 26 · 147.7s | 外面两圈 RiskMind Customization 和 Business Plugin 变蓝；图例加上 "RiskMind · Vertical" | "RiskMind" · "Vertical" | The two outer layers are ours, and they're vertical: the services risk management needs, and the risk knowledge in the plugins. That's where RiskMind's value is. |
| 27 · 149.1s | Decouple：Augmented LLM 和 Agent Harness 名字下面的小字轮换：模型 Claude Sonnet 4.6 → Claude Sonnet 5.5 → GPT-6.1 Sol，harness Claude Agent SDK → OpenAI Codex SDK → Pi；外面两圈不动。最后小字淡出，名字回到正中，停在这里 | "Claude Sonnet 4.6" · "Claude Sonnet 5.5" · "GPT-6.1 Sol" · "Claude Agent SDK" · "OpenAI Codex SDK" · "Pi" | And because the layers are decoupled, the horizontal part can change underneath without touching what we built. A newer model, another model, another SDK, or one day an internal horizontal agent: the customization and the plugins stay the same. That's why we build RiskMind as Agent plus Plugin. Next session, we open up the plugin. |

## Production notes

- **视觉风格**：和 Session 1 一致：细线、方框和胶囊形节点、灰色箭头、大量留白；只用蓝色系，唯一例外是 Horizontal 用 RBC 黄；字体 DM Sans，代码用等宽字体。
- **颜色规则**：黄色表示 SDK 提供的（横向），蓝色表示 RiskMind 或 plugin 做的（纵向）。只在需要对比的页面用黄蓝（Customization、Business Plugin 两页和结尾）；Agent Harness 页保持蓝/灰。
- **实线和虚线**：实线是已经有的，虚线是还没有的（Subagents、AutoSkill · AutoEvolution）。
- **衔接**：类比里的方块带着字飞进下一屏（CPU → LLM、RAM → Context、Core Tools → Tool Call(s)、Customization → RiskMind · Built In、Plugin → Plugins）。
- **用词**：第四圈叫 Business Plugin；类比方块、Run 里的 Plugins、Plugin Lifecycle Management 等功能性说法保留 Plugin。屏幕上不出现 "Claude Code"。

## 待做

- [ ] Talk track 是按视频和最初的 Outline 反推写的初稿，需要逐段确认措辞，尤其是第 8 段（Customization，比较长）和第 24–27 段（结尾的 Q1）。
- [ ] 讲之前确认 "GPT-6.1 Sol" 仍是 OpenAI Sonnet 级别模型的名字（第 27 段）。
- [ ] Q2（为什么是 Agent + Plugin）只在第 3、12、13 段口头讲；最初 Outline 里的对比表（Workflow / Agent + Tools / Agent + Plugin）没有进视频，要不要在讲稿里补一段口头说明，待定。
- [ ] Session 2 还没有和 Session 1 一样的 Outline 定稿和提词器；`RiskMind Session 2 Outline.html` 是做视频之前的规划（4 张 slide），和现在的视频差别很大。
- [ ] 开场要不要加和 Session 1 一样的封面和课程页（Session 2 · Agent 亮起）。
