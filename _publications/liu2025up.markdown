---
layout: publication
title: 'Up-person: Unified Parameter-efficient Transfer Learning For Text-based Person
  Retrieval'
authors: Yating Liu, Yaowei Li, Xiangyuan Lan, Wenming Yang, Zimo Liu, Qingmin Liao
conference: Arxiv
year: 2025
bibkey: liu2025up
citations: 0
additional_links: [{name: Code, url: 'https://github.com/Liu-Yating/UP-Person'}, {
    name: Paper, url: 'https://arxiv.org/abs/2504.10084'}]
tags: ["Datasets", "Evaluation", "Multimodal Retrieval"]
short_authors: Liu et al.
---
Text-based Person Retrieval (TPR) as a multi-modal task, which aims to
retrieve the target person from a pool of candidate images given a text
description, has recently garnered considerable attention due to the progress
of contrastive visual-language pre-trained model. Prior works leverage
pre-trained CLIP to extract person visual and textual features and fully
fine-tune the entire network, which have shown notable performance improvements
compared to uni-modal pre-training models. However, full-tuning a large model
is prone to overfitting and hinders the generalization ability. In this paper,
we propose a novel Unified Parameter-Efficient Transfer Learning (PETL) method
for Text-based Person Retrieval (UP-Person) to thoroughly transfer the
multi-modal knowledge from CLIP. Specifically, UP-Person simultaneously
integrates three lightweight PETL components including Prefix, LoRA and
Adapter, where Prefix and LoRA are devised together to mine local information
with task-specific information prompts, and Adapter is designed to adjust
global feature representations. Additionally, two vanilla submodules are
optimized to adapt to the unified architecture of TPR. For one thing, S-Prefix
is proposed to boost attention of prefix and enhance the gradient propagation
of prefix tokens, which improves the flexibility and performance of the vanilla
prefix. For another thing, L-Adapter is designed in parallel with layer
normalization to adjust the overall distribution, which can resolve conflicts
caused by overlap and interaction among multiple submodules. Extensive
experimental results demonstrate that our UP-Person achieves state-of-the-art
results across various person retrieval datasets, including CUHK-PEDES,
ICFG-PEDES and RSTPReid while merely fine-tuning 4.7% parameters. Code is
available at https://github.com/Liu-Yating/UP-Person.