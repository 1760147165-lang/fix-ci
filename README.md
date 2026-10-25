# fix-ci · 中英双语学术写作与审查

An instruction-based skill for Chinese and English academic writing, revision, translation, and reviewer-comment checks. The name is retained from the original personal skill; this project is about manuscripts, not continuous-integration pipelines.

将现有的 `fix-ci` 学术编辑能力打包分享，包含从论文修订中提炼的措辞方式、方法描述顺序、术语一致性和证据核查要求。英文使用时采用自然英文表达；学习重点是论证与信息组织方式。

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

## 能力与适用范围 / Scope

- 中英文论文撰写、局部修改和学术翻译。
- 原稿、导师批注与修改稿之间的逐项核对。
- 对象与数据来源、样本筛选、控制条件、比较与结果的表达组织。
- 术语、数值、引用、图表指向及因果措辞的一致性审查。
- 写作与复核阶段分离；有独立代理时可分别执行，无此能力时顺序复核并说明限制。

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
