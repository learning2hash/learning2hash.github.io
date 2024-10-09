---
layout: publication
title: Large Language Models Can Self-improve
authors: Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu, Jiawei Han
conference: "Arxiv"
year: 2022
bibkey: huang2022large
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2210.11610v2"}
tags: ['ARXIV', 'Supervised']
---
Large Language Models (LLMs) have achieved excellent performances in various tasks. However fine-tuning an LLM requires extensive supervision. Human on the other hand may improve their reasoning abilities by self-thinking without external inputs. In this work we demonstrate that an LLM is also capable of self-improving with only unlabeled datasets. We use a pre-trained LLM to generate high-confidence rationale-augmented answers for unlabeled questions using Chain-of-Thought prompting and self-consistency and fine-tune the LLM using those self-generated solutions as target outputs. We show that our approach improves the general reasoning ability of a 540B-parameter LLM (74.437;-82.137; on GSM8K 78.237;-83.037; on DROP 90.037;-94.437; on OpenBookQA and 63.437;-67.937; on ANLI-A3) and achieves state-of-the-art-level performance without any ground truth label. We conduct ablation studies and show that fine-tuning on reasoning is critical for self-improvement.
