# fix-ci · 自动拆解需求、独立审查、逐轮完善的双语学术写作 Skill

把写作要求、修改意见和论文材料交给 AI，`fix-ci` 会引导它拆分任务、安排写作与审查、自动返修，并在完成后核对整篇论文。你可以把更多精力放在研究问题和学术判断上，减少逐段催促、核对遗漏和手动转述修改意见的重复工作。

它把 **Orchestrator（统筹）+ Writer（写作）/ Reviewer（审查）** 组织为一套可追踪的工作流程：每个子任务都有要求、交付物和验收标准，审查发现的问题会自动回到写作环节处理，通过后再进入有依赖关系的下一项任务。

## 主要能力

- **中英文目标语言检测与学术规范适配**：根据明确要求或论文语言选择学术表达、标点、数字和单位规则，并结合目标期刊、参考模板及原稿引用体系，统一正文引文、参考文献、标题和图表格式。指定投稿规范优先；缺少期刊要求时保留合理的现有格式，并注明未核验项。
- **多种论文类型支持**：覆盖实验型、综述、理论、案例研究及定性研究，按研究类型组织任务与章节，支持整篇写作、局部修改和单独审查。
- **Orchestrator + Writer / Reviewer 多 agent 协作与自动 QA 闭环**：由 Orchestrator 拆解需求、路由任务和追踪进度，Writer 负责写作或修改，独立的 Reviewer 对照原始要求、材料和实际成果检查。未通过的任务自动返修、重新审核，满足验收标准后再推进，减少用户在多个角色之间传话和逐轮人工检查的工作。
- **需求追踪矩阵与模块化执行**：将每条要求映射到具体子任务，记录来源证据、修改范围、依赖关系、审核轮次和完成状态。每个任务的完成都能追溯到实际稿件或检查结果。
- **引用、数据、图表、术语、格式与逻辑一致性审核**：检查正文与参考文献对应、摘要与结果数值、图表编号和引用、缩写首次定义、单位与术语，以及因果判断是否超出证据。导师或审稿人批注按条追踪落实情况。
- **中英文论文翻译与术语统一**：建立源语言与目标语言术语表，在保留数值、引用、限定条件和科学含义的基础上，按目标语言重组句式，保持全文表达一致。
- **整篇论文最终 QA 报告**：局部任务完成后再做整合复核，报告需求覆盖、任务状态、批注落实、跨章节一致性和仍需补充的证据，让完成情况可检查、可追踪。
- **可确定事实优先自动检查**：在具备脚本或命令工具的环境中，优先自动核对字数、引用对应、编号、图表交叉引用等可确定事项；语义、论证和因果关系交由审查环节判断。
- **自然、直接、少说教的学术表达**：中英文均强调具体对象、清晰动作、数据依据和适用边界，减少空泛总结、无信息的提醒和居高临下的指令口吻，并吸收真实论文修订中的方法描述与措辞习惯。

## 从一个需求到最终稿

1. **理解需求**：识别文件角色、目标语言、论文类型和投稿规范，把写作或修改要求整理成可验收条目。
2. **自动拆解**：按范围与依赖拆成子任务，例如方法说明、结果表达、术语统一、参考文献和整合复核；每项指定输入、输出与验收标准。
3. **写作与独立审核**：Writer 完成当前任务，Reviewer 读取实际成果并逐项核对，给出有位置、有证据的修改意见。
4. **自动返修与推进**：可修复的问题交回 Writer，修改后再次审核；通过后推进下一项有依赖关系的任务。
5. **整篇整合 QA**：回到全部要求，核对章节衔接及数据、术语、引用和结论一致性，发现回归问题时重新打开相应任务。

独立多 agent 模式需要宿主软件提供并允许子代理调用；在单 agent 环境中，技能采用分阶段写作与自审，并明确标注执行方式。数据缺失、要求冲突或必要工具不可用时，会保留未通过状态并指出需要补充的内容。该流程旨在减少重复人工检查，作者仍需确认研究事实与最终学术判断。

可直接给 AI 这样的任务：

```text
使用 fix-ci，按所附要求修改论文。请自动拆解子任务，逐项写作、审核和返修，
通过后推进下一项，最后给出修改稿与整篇 QA 报告。
目标语言以论文为准，格式遵循所附期刊模板，保留原始数据与引用。
有独立子代理时分别安排 Writer 和 Reviewer；证据不足的事项请明确列出。
```

## Core capabilities in English

`fix-ci` turns an academic writing or revision request into scoped tasks with acceptance checks, writer/reviewer routing, automatic correction cycles, and final integration QA. It helps reduce repetitive manual checking and coordination between drafting and review.

- Detect Chinese or English as the target language and apply the supplied journal/template rules, including citation and reference formatting. Language alone does not determine a journal's citation style.
- Adapt the task plan to experimental, review, theoretical, case-study, and qualitative manuscripts.
- Use an Orchestrator to assign tasks to a Writer and a separate read-only Reviewer when the host supports permitted subagents; otherwise disclose sequential self-review.
- Track requirements, evidence, dependencies, artifact revisions, and review outcomes; send actionable findings through revision and re-review before advancing.
- Check citations, data, figures, tables, terminology, formatting, and logical consistency, including individual supervisor or reviewer comments.
- Translate Chinese and English manuscripts with consistent terminology and preserved scientific meaning.
- Deliver a final QA report with task outcomes, integration checks, and unresolved evidence gaps.
- Prefer available scripts or commands for deterministic checks, and use direct, evidence-led prose with less patronizing or formulaic language.

## 下载 / Downloads

- [技能安装包 fix-ci.zip](https://github.com/1760147165-lang/fix-ci/releases/latest/download/fix-ci.zip)：内含 `fix-ci/SKILL.md`、参考文件和许可证。
- [通用单文件 fix-ci-portable.md](https://github.com/1760147165-lang/fix-ci/releases/latest/download/fix-ci-portable.md)：将技能和参考文件合并，适合支持文件上传或项目知识文件的聊天软件。
- [版本与校验值](https://github.com/1760147165-lang/fix-ci/releases/latest)：包含 SHA-256 校验文件。

## 安装与使用

### 支持 Agent Skills 的软件

下载 `fix-ci.zip`。若软件提供技能导入入口，按其提示上传 ZIP；若要求本地目录，解压后将整个 `fix-ci` 文件夹放入该软件规定的 skills 目录。保留 `references/` 与 `SKILL.md` 的相对位置。技能目录约定因软件及版本而异，请以实际软件文档为准。

对于提供 `$skill-installer` 的 Codex 版本，可以直接发送：

```text
$skill-installer install https://github.com/1760147165-lang/fix-ci/tree/main/skills/fix-ci
```

按安装工具提示刷新技能或重新启动会话后，使用 `$fix-ci`。新版软件的插件分发入口可能不同；本仓库提供的是标准技能目录与通用文本包。

### ChatGPT 与其他聊天型 AI 软件

若你的账号或工作区提供自定义 Skills 导入入口，可尝试导入 `fix-ci.zip`，按该入口的格式要求操作。该入口的可用性取决于产品、账号和工作区设置。

没有 Skills 导入入口时，下载 `fix-ci-portable.md`，与论文一起上传到会话，或加入支持文件的项目，然后发送：

```text
请读取 fix-ci-portable.md，并将其中内容作为本次论文编辑的工作规范。
目标语言：中文。任务：对照导师批注和修改稿，检查措辞、逻辑、术语与逐条批注落实情况。
先确认文件角色与修改范围；保留原始数据与引用，列出证据不足之处。
```

上传文件是会话内使用方式，不代表已经永久安装。若使用项目功能，在项目指令中明确要求读取该文件。模型须能够读取附件；处理 Word 批注、修订、公式或版式还需相应文档工具。无文件读取能力时，可把单文件内容粘贴到允许的指令区；若超过长度限制，请使用支持附件或较长上下文的环境。

### English quick start

Import `fix-ci.zip` in an application that supports Agent Skills, or extract its `fix-ci/` folder into the application's documented skills directory. Keep the reference file alongside the entrypoint.

For chat applications, upload `fix-ci-portable.md` together with the manuscript and explicitly ask the model to read and follow it for the task. This is a session or project workflow, not a guarantee of native installation or persistent memory.

```text
Read fix-ci-portable.md and use it as the editing guidance for this task.
Target language: English. Revise the supplied Methods section for clear sample provenance,
controlled comparisons, consistent terminology, and natural academic wording.
Preserve data and citations. Flag missing evidence and describe the changes.
```

## 适用范围与运行条件 / Scope

技能采用源自建筑热工与城市微气候论文的表达偏好，包含 LCZ、UTCI 等领域示例。其他学科应按其研究设计、术语与期刊要求应用。原文中特定中文术语、引用上标等属于本技能的风格默认值；实际投稿规范和用户明确要求优先。

This package contains instructions, not a trained model, an API service, or a document-processing engine. It does not supply browsing, Word rendering, independent agents, or reference databases. Its checks are only as reliable as the host's tools and the available evidence; unavailable checks should be reported.

公开包包含技能规则和参考工作流；原始论文、导师批注文件、个人联系方式和本地会话记录均未纳入。

## 本地构建 / Build

需要 Python 3，仅使用标准库。

```bash
python3 scripts/build_release.py
```

输出位于 `dist/`：安装包、单文件版本和 `SHA256SUMS.txt`。构建会检查技能元信息、参考文件链接及 ZIP 内文件。发布版本使用 `skills/fix-ci/` 中的规则作为唯一来源。

## 上游参考 / Upstream references

- [OpenAI skills repository and installation guidance](https://github.com/openai/skills)（上游目前提示新插件分发参阅 Plugins 仓库）。
- [OpenAI Plugins](https://github.com/openai/plugins)。
- [ChatGPT skill authoring documentation](https://learn.chatgpt.com/docs/build-skills)。

## License

MIT. You may use, modify, and redistribute this skill under the included license.
