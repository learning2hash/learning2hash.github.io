---
layout: publication
title: Asymmetric Distribution Measure For Few-shot Learning
authors: Wenbin Li, Lei Wang, Jing Huo, Yinghuan Shi, Yang Gao, Jiebo Luo
conference: Proceedings of the Twenty-Ninth International Joint Conference on Artificial
  Intelligence
year: 2020
bibkey: li2020asymmetric
citations: 72
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.00153'}]
tags: ["Few Shot & Zero Shot", "IJCAI"]
short_authors: Li et al.
---
The core idea of metric-based few-shot image classification is to directly
measure the relations between query images and support classes to learn
transferable feature embeddings. Previous work mainly focuses on image-level
feature representations, which actually cannot effectively estimate a class's
distribution due to the scarcity of samples. Some recent work shows that local
descriptor based representations can achieve richer representations than
image-level based representations. However, such works are still based on a
less effective instance-level metric, especially a symmetric metric, to measure
the relations between query images and support classes. Given the natural
asymmetric relation between a query image and a support class, we argue that an
asymmetric measure is more suitable for metric-based few-shot learning. To that
end, we propose a novel Asymmetric Distribution Measure (ADM) network for
few-shot learning by calculating a joint local and global asymmetric measure
between two multivariate local distributions of queries and classes. Moreover,
a task-aware Contrastive Measure Strategy (CMS) is proposed to further enhance
the measure function. On popular miniImageNet and tieredImageNet, we achieve
\(3.02%\) and \(1.56%\) gains over the state-of-the-art method on the \(5\)-way
\(1\)-shot task, respectively, validating our innovative design of asymmetric
distribution measures for few-shot learning.