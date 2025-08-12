---
layout: publication
title: A Closer Look At Novel Class Discovery From The Labeled Set
authors: Ziyun Li, Jona Otholt, Ben Dai, di Hu, Christoph Meinel, Haojin Yang
conference: Arxiv
year: 2022
bibkey: li2022closer
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.09120'}]
tags: []
short_authors: Li et al.
---
Novel class discovery (NCD) aims to infer novel categories in an unlabeled
dataset leveraging prior knowledge of a labeled set comprising disjoint but
related classes. Existing research focuses primarily on utilizing the labeled
set at the methodological level, with less emphasis on the analysis of the
labeled set itself. Thus, in this paper, we rethink novel class discovery from
the labeled set and focus on two core questions: (i) Given a specific unlabeled
set, what kind of labeled set can best support novel class discovery? (ii) A
fundamental premise of NCD is that the labeled set must be related to the
unlabeled set, but how can we measure this relation? For (i), we propose and
substantiate the hypothesis that NCD could benefit more from a labeled set with
a large degree of semantic similarity to the unlabeled set. Specifically, we
establish an extensive and large-scale benchmark with varying degrees of
semantic similarity between labeled/unlabeled datasets on ImageNet by
leveraging its hierarchical class structure. As a sharp contrast, the existing
NCD benchmarks are developed based on labeled sets with different number of
categories and images, and completely ignore the semantic relation. For (ii),
we introduce a mathematical definition for quantifying the semantic similarity
between labeled and unlabeled sets. In addition, we use this metric to confirm
the validity of our proposed benchmark and demonstrate that it highly
correlates with NCD performance. Furthermore, without quantitative analysis,
previous works commonly believe that label information is always beneficial.
However, counterintuitively, our experimental results show that using labels
may lead to sub-optimal outcomes in low-similarity settings.