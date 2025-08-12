---
layout: publication
title: Part-guided Relational Transformers For Fine-grained Visual Recognition
authors: Yifan Zhao, Jia Li, Xiaowu Chen, Yonghong Tian
conference: IEEE Transactions on Image Processing
year: 2021
bibkey: zhao2021part
citations: 42
additional_links: [{name: Code, url: 'https://github.com/iCVTEAM/PART'}, {name: Paper,
    url: 'https://arxiv.org/abs/2212.13685'}]
tags: []
short_authors: Zhao et al.
---
Fine-grained visual recognition is to classify objects with visually similar
appearances into subcategories, which has made great progress with the
development of deep CNNs. However, handling subtle differences between
different subcategories still remains a challenge. In this paper, we propose to
solve this issue in one unified framework from two aspects, i.e., constructing
feature-level interrelationships, and capturing part-level discriminative
features. This framework, namely PArt-guided Relational Transformers (PART), is
proposed to learn the discriminative part features with an automatic part
discovery module, and to explore the intrinsic correlations with a feature
transformation module by adapting the Transformer models from the field of
natural language processing. The part discovery module efficiently discovers
the discriminative regions which are highly-corresponded to the gradient
descent procedure. Then the second feature transformation module builds
correlations within the global embedding and multiple part embedding, enhancing
spatial interactions among semantic pixels. Moreover, our proposed approach
does not rely on additional part branches in the inference time and reaches
state-of-the-art performance on 3 widely-used fine-grained object recognition
benchmarks. Experimental results and explainable visualizations demonstrate the
effectiveness of our proposed approach. The code can be found at
https://github.com/iCVTEAM/PART.