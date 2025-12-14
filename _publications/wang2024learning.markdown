---
layout: publication
title: Learning Visual Hierarchies In Hyperbolic Space For Image Retrieval
authors: Ziwei Wang, Sameera Ramasinghe, Chenchen Xu, Julien Monteil, Loris Bazzani,
  Thalaiyasingam Ajanthan
conference: Arxiv
year: 2024
bibkey: wang2024learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.17490'}]
tags: [Distance Metric Learning, Image Retrieval, Evaluation]
short_authors: Wang et al.
---
Structuring latent representations in a hierarchical manner enables models to
learn patterns at multiple levels of abstraction. However, most prevalent image
understanding models focus on visual similarity, and learning visual
hierarchies is relatively unexplored. In this work, for the first time, we
introduce a learning paradigm that can encode user-defined multi-level complex
visual hierarchies in hyperbolic space without requiring explicit hierarchical
labels. As a concrete example, first, we define a part-based image hierarchy
using object-level annotations within and across images. Then, we introduce an
approach to enforce the hierarchy using contrastive loss with pairwise
entailment metrics. Finally, we discuss new evaluation metrics to effectively
measure hierarchical image retrieval. Encoding these complex relationships
ensures that the learned representations capture semantic and structural
information that transcends mere visual similarity. Experiments in part-based
image retrieval show significant improvements in hierarchical retrieval tasks,
demonstrating the capability of our model in capturing visual hierarchies.