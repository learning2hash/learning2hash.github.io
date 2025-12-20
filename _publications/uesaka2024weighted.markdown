---
layout: publication
title: Weighted Point Set Embedding For Multimodal Contrastive Learning Toward Optimal
  Similarity Metric
authors: Toshimitsu Uesaka, Taiji Suzuki, Yuhta Takida, Chieh-Hsin Lai, Naoki Murata,
  Yuki Mitsufuji
conference: Arxiv
year: 2024
bibkey: uesaka2024weighted
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.19228'}]
tags: ["Distance Metric Learning", "Evaluation", "Self-Supervised"]
short_authors: Uesaka et al.
---
In typical multimodal contrastive learning, such as CLIP, encoders produce
one point in the latent representation space for each input. However, one-point
representation has difficulty in capturing the relationship and the similarity
structure of a huge amount of instances in the real world. For richer classes
of the similarity, we propose the use of weighted point sets, namely, sets of
pairs of weight and vector, as representations of instances. In this work, we
theoretically show the benefit of our proposed method through a new
understanding of the contrastive loss of CLIP, which we call symmetric InfoNCE.
We clarify that the optimal similarity that minimizes symmetric InfoNCE is the
pointwise mutual information, and show an upper bound of excess risk on
downstream classification tasks of representations that achieve the optimal
similarity. In addition, we show that our proposed similarity based on weighted
point sets consistently achieves the optimal similarity. To verify the
effectiveness of our proposed method, we demonstrate pretraining of text-image
representation models and classification tasks on common benchmarks.