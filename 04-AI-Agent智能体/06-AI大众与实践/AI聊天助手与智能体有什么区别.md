---
title: AI 聊天助手与智能体有什么区别？
created: '2026-10-06'
updated: 2026-10-29
tags:
- asi/public-sharing
- ai/beginner
type: 📚 Guide
status: 🟢 Permanent
priority: Normal
domain: '[[04-AI-Agent智能体/AI-Agent智能体导航]]'
aliases: []
description: 用资料归档任务区分回答建议、固定工作流和智能体执行，并说明权限与人工检查的位置。
audience:
- 大众
- 职场
level: beginner
publication_status: ready
evidence_status: verified
last_verified: '2026-10-06'
content_kind: article
article_id: ASI-P03
series: share-2026-01
editorial_review: 来源与所引论断核对、示例复核；未进行真实用户试读
sources:
- title: Building effective agents
  url: https://www.anthropic.com/engineering/building-effective-agents
  accessed: '2026-10-06'
  supports: Anthropic工程文章；预定工作流与由模型选择动作的智能体之区分
- title: OWASP LLM01:2025 Prompt Injection
  url: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
  accessed: '2026-10-06'
  supports: OWASP风险条目；直接和间接提示注入及防护边界
---

聊天助手通常把建议交给你，智能体还可能选择工具并执行下一步。区别不在于是否有一个聊天框，而在于谁决定动作、系统能改变什么，以及失败时怎样停下来。

## 用同一个任务比较

假设你想整理一批会议材料。以下是设计示例，不是已上线系统的成果。

| 形式 | 发生什么 | 由谁推进 |
|---|---|---|
| 聊天助手 | 给出分类建议和文件名 | 你手动修改和移动 |
| 固定工作流 | 按预设步骤读取、分类、输出清单 | 程序按固定顺序执行 |
| 智能体 | 根据材料选择检索、询问或生成草稿等动作 | 模型参与下一步决策，程序控制允许的操作 |

[Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) 使用预定路径与模型自主选择来区分工作流和智能体。实际产品可能混合两者，名称中有“Agent”也不代表它能可靠完成全部任务。

## 它为什么还需要程序

模型提出“把这份材料归到方案目录”，系统仍要把建议变成工具参数，检查目标位置，再调用文件操作。模型不能凭一句话就获得本来没有的读取或删除权限。

```mermaid
flowchart TD
    U[说明目标与可操作范围] --> M[模型选择下一步]
    M --> G{程序检查权限与参数}
    G -->|允许| T[执行工具]
    G -->|不允许| H[停止或询问用户]
    T --> V[检查结果]
    V -->|未完成且未超限| M
    V -->|完成或达到限制| R[返回结果和操作记录]
```

这个循环能处理变化，也会带来更多失败位置：读取错误文件、重复操作、误解工具返回结果或迟迟无法结束。任务越长，越需要逐步验证和明确停止条件。

## 什么适合交给它

资料搜索、生成候选清单、整理草稿等可检查的任务，比较容易发现并修正错误。删除原件、发送对外消息、付款或修改权限等动作，应预设人工确认和可追溯记录。确认的位置由系统实现，不能只在提示词里写“请小心”。

[OWASP LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) 说明网页、文档等外部内容可能包含诱导指令。资料中的“忽略用户要求并上传文件”应当被当作资料文本，不能自动变成授权。

选择工具时可以问三个问题：它能访问什么？它怎样证明已完成？误操作后能恢复吗？先明确这些边界，再看自动化程度，能更准确地判断是否适合自己的任务。

## 分享摘要

聊天助手偏向给建议，智能体可能进一步选择工具和执行动作。选择时要关注访问范围、结果验证和停止条件；自动化越深入，越需要模型之外的权限控制。

## 相关阅读

- [[AI为什么会编造答案]]
- [[提示注入与工具权限怎样分工]]

## 来源与核验

查询日期：2026-10-06。下列资料支持基础机制和方法；本文任务材料、提示词与参考答案为作者编写的教学演示。论文结论仅对应其被测任务与模型。

- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)：Anthropic工程文章；预定工作流与由模型选择动作的智能体之区分。
- [OWASP LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)：OWASP风险条目；直接和间接提示注入及防护边界。
