---
layout: publication
title: Task-independent Knowledge Makes For Transferable Representations For Generalized
  Zero-shot Learning
authors: Chaoqun Wang, Xuejin Chen, Shaobo Min, Xiaoyan Sun, Houqiang Li
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2021
bibkey: wang2021task
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.01832'}]
tags: ["AAAI"]
short_authors: Wang et al.
---
Generalized Zero-Shot Learning (GZSL) targets recognizing new categories by
learning transferable image representations. Existing methods find that, by
aligning image representations with corresponding semantic labels, the
semantic-aligned representations can be transferred to unseen categories.
However, supervised by only seen category labels, the learned semantic
knowledge is highly task-specific, which makes image representations biased
towards seen categories. In this paper, we propose a novel Dual-Contrastive
Embedding Network (DCEN) that simultaneously learns task-specific and
task-independent knowledge via semantic alignment and instance discrimination.
First, DCEN leverages task labels to cluster representations of the same
semantic category by cross-modal contrastive learning and exploring
semantic-visual complementarity. Besides task-specific knowledge, DCEN then
introduces task-independent knowledge by attracting representations of
different views of the same image and repelling representations of different
images. Compared to high-level seen category supervision, this instance
discrimination supervision encourages DCEN to capture low-level visual
knowledge, which is less biased toward seen categories and alleviates the
representation bias. Consequently, the task-specific and task-independent
knowledge jointly make for transferable representations of DCEN, which obtains
averaged 4.1% improvement on four public benchmarks.