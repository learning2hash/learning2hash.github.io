---
layout: publication
title: Attention-based Ensemble for Deep Metric Learning
authors: Kim et al.
conference: Lecture Notes in Computer Science
year: 2018
bibkey: kim2018attention
citations: 237
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.00382'}]
tags: ["Distance-Metric-Learning"]
---
Deep metric learning aims to learn an embedding function, modeled as deep
neural network. This embedding function usually puts semantically similar
images close while dissimilar images far from each other in the learned
embedding space. Recently, ensemble has been applied to deep metric learning to
yield state-of-the-art results. As one important aspect of ensemble, the
learners should be diverse in their feature embeddings. To this end, we propose
an attention-based ensemble, which uses multiple attention masks, so that each
learner can attend to different parts of the object. We also propose a
divergence loss, which encourages diversity among the learners. The proposed
method is applied to the standard benchmarks of deep metric learning and
experimental results show that it outperforms the state-of-the-art methods by a
significant margin on image retrieval tasks.