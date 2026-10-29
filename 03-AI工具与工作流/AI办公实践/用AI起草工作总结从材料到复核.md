---
title: 用 AI 起草工作总结：从材料到复核
created: '2026-10-06'
updated: 2026-10-29
tags:
- asi/public-sharing
- ai/practical
type: 📚 Guide
status: 🟢 Permanent
priority: Normal
domain: '[[03-AI工具与工作流/AI工具与工作流导航]]'
aliases: []
description: 演示把原始记录整理为事实表、总结草稿和修改记录，避免把计划或中间产物写成成果。
audience:
- 职场
- 大众
level: practical
publication_status: ready
evidence_status: verified
last_verified: '2026-10-06'
content_kind: article
article_id: ASI-W02
series: share-2026-01
editorial_review: 来源与所引论断核对、示例复核；未进行真实用户试读
sources:
- title: Claude prompting best practices
  url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
  accessed: '2026-10-06'
  supports: Anthropic官方指导；明确任务、输入结构、示例与输出约束。其他模型应自行验证
- title: On Faithfulness and Factuality in Abstractive Summarization
  url: https://arxiv.org/abs/2005.00661
  accessed: '2026-10-06'
  supports: ACL 2020原始论文；摘要可能产生与输入不一致的内容
---

AI 可以帮助你组织工作总结，写得可靠的前提是先整理事实，再调整表达。最需要检查的地方通常是完成状态、数字和结果归因。

## 输入：三条模拟原始记录

本案例沿用资料问答的D1—D3：12条需求中8条已归类、4条待确认；报告提纲已完成，正文尚未提交审核；下周计划确认剩余需求，负责人和截止日未定。数字仅用于教学，不表示真实项目成果。

先把记录变成事实表：

| 事项 | 已完成 | 未完成 | 可以写出的结果 |
|---|---|---|---|
| 需求整理 | 收集12条、归类8条 | 确认4条 | 需求范围已形成部分分类 |
| 报告 | 提纲 | 正文及审核 | 有了结构，尚未形成审核稿 |
| 下一步 | 计划描述 | 人员与期限确认 | 可以写计划，不能承诺日期 |

这种拆解是本文的编辑方法。[Claude prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) 对明确任务与输出要求提供了厂商指导；不应把指导误写为经过统一量化验证的效率提升。

## 步骤：先事实，再成稿

```text
根据以下事实表起草一段工作总结。
结构为：本周进展、未完成事项、下一步安排。
保留数字与完成状态；不要新增成果、满意度、节省成本或因果判断。
计划必须使用“计划”“待确认”等表达。
完成后另列需要我补充的信息，不要把补充问题混进总结正文。
```

参考成稿由作者编写并依据材料复核：

> 本周收集12条需求，已完成其中8条的归类，剩余4条待确认。报告提纲已完成，正文尚未提交审核。下一步计划确认剩余需求，并明确负责人和截止时间。

它不华丽，但每一项都能回到记录。若需要描述价值，应补充真实验收记录或具体用途，而不是让 AI 自行补上“显著提升效率”。

## 修改记录也属于交付

| 草稿中的问题写法 | 修改后 | 理由 |
|---|---|---|
| 完成12条需求归类 | 收集12条，归类8条 | 保留分母与进度 |
| 报告已提交审核 | 报告提纲完成，正文未送审 | 分清中间产物 |
| 下周五全部完成 | 负责人和期限待确认 | 原文没有承诺 |

```mermaid
flowchart LR
    A[原始记录] --> B[事实表]
    B --> C[按结构起草]
    C --> D[逐句核对状态与数字]
    D --> E[修改记录和最终稿]
```

## 怎样判断这次使用是否有价值

检查总结是否覆盖重要进展、是否保留未完成事项、是否适合收件人阅读。[On Faithfulness and Factuality in Abstractive Summarization](https://arxiv.org/abs/2005.00661) 支持“摘要忠实性需要单独检查”，没有证明本案例节省了多少时间。

如果你以后记录实际效率，应保留人工写作和AI辅助两种过程的时间、任务难度及复核成本。本轮没有这些实测数据，所以只交付可检查的方法，不报告省时百分比。

涉及他人的评价或敏感信息，应先脱敏并确认使用范围。成稿最后由了解事实的人负责确认，不能以语言自然代替内容正确。

## 分享摘要

用 AI 写工作总结，先把材料拆成已完成、未完成和下一步。检查数字、状态和承诺，再调整语言；没有真实记录的“显著提效”或“成果突出”不要自动补进去。

## 相关阅读

- [[怎样让AI根据资料回答并标出依据]]
- [[零散记录转行动清单]]
- [[长文摘要怎样保留关键信息]]

## 来源与核验

查询日期：2026-10-06。下列资料支持基础机制和方法；本文任务材料、提示词与参考答案为作者编写的教学演示。论文结论仅对应其被测任务与模型。

- [Claude prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic官方指导；明确任务、输入结构、示例与输出约束。其他模型应自行验证。
- [On Faithfulness and Factuality in Abstractive Summarization](https://arxiv.org/abs/2005.00661)：ACL 2020原始论文；摘要可能产生与输入不一致的内容。
