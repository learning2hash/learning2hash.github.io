---
layout: publication
title: Effective Few-shot Named Entity Linking By Meta-learning
authors: Xiuxing Li, Zhenyu Li, Zhengyan Zhang, Ning Liu, Haitao Yuan, Wei Zhang,
  Zhiyuan Liu, Jianyong Wang
conference: 2022 IEEE 38th International Conference on Data Engineering (ICDE)
year: 2022
bibkey: li2022effective
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.05280'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Li et al.
---
Entity linking aims to link ambiguous mentions to their corresponding
entities in a knowledge base, which is significant and fundamental for various
downstream applications, e.g., knowledge base completion, question answering,
and information extraction. While great efforts have been devoted to this task,
most of these studies follow the assumption that large-scale labeled data is
available. However, when the labeled data is insufficient for specific domains
due to labor-intensive annotation work, the performance of existing algorithms
will suffer an intolerable decline. In this paper, we endeavor to solve the
problem of few-shot entity linking, which only requires a minimal amount of
in-domain labeled data and is more practical in real situations. Specifically,
we firstly propose a novel weak supervision strategy to generate non-trivial
synthetic entity-mention pairs based on mention rewriting. Since the quality of
the synthetic data has a critical impact on effective model training, we
further design a meta-learning mechanism to assign different weights to each
synthetic entity-mention pair automatically. Through this way, we can
profoundly exploit rich and precious semantic information to derive a
well-trained entity linking model under the few-shot setting. The experiments
on real-world datasets show that the proposed method can extensively improve
the state-of-the-art few-shot entity linking model and achieve impressive
performance when only a small amount of labeled data is available. Moreover, we
also demonstrate the outstanding ability of the model's transferability.