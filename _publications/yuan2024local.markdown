---
layout: publication
title: Local Positional Graphs And Attentive Local Features For A Data And Runtime-efficient
  Hierarchical Place Recognition Pipeline
authors: Fangming Yuan, Stefan Schubert, Peter Protzel, Peer Neubert
conference: IEEE Robotics and Automation Letters
year: 2024
bibkey: yuan2024local
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.10283'}]
tags: ["Efficiency"]
short_authors: Yuan et al.
---
Large-scale applications of Visual Place Recognition (VPR) require
computationally efficient approaches. Further, a well-balanced combination of
data-based and training-free approaches can decrease the required amount of
training data and effort and can reduce the influence of distribution shifts
between the training and application phases. This paper proposes a runtime and
data-efficient hierarchical VPR pipeline that extends existing approaches and
presents novel ideas. There are three main contributions: First, we propose
Local Positional Graphs (LPG), a training-free and runtime-efficient approach
to encode spatial context information of local image features. LPG can be
combined with existing local feature detectors and descriptors and considerably
improves the image-matching quality compared to existing techniques in our
experiments. Second, we present Attentive Local SPED (ATLAS), an extension of
our previous local features approach with an attention module that improves the
feature quality while maintaining high data efficiency. The influence of the
proposed modifications is evaluated in an extensive ablation study. Third, we
present a hierarchical pipeline that exploits hyperdimensional computing to use
the same local features as holistic HDC-descriptors for fast candidate
selection and for candidate reranking. We combine all contributions in a
runtime and data-efficient VPR pipeline that shows benefits over the
state-of-the-art method Patch-NetVLAD on a large collection of standard place
recognition datasets with 15\(%\) better performance in VPR accuracy, 54\(\times\)
faster feature comparison speed, and 55\(\times\) less descriptor storage
occupancy, making our method promising for real-world high-performance
large-scale VPR in changing environments. Code will be made available with
publication of this paper.