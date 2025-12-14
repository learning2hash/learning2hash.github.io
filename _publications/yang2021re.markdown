---
layout: publication
title: Re-rank Coarse Classification With Local Region Enhanced Features For Fine-grained
  Image Recognition
authors: Shaokang Yang, Shuai Liu, Cheng Yang, Changhu Wang
conference: Arxiv
year: 2021
bibkey: yang2021re
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.09875'}]
tags: [Evaluation, Supervised, Tools & Libraries]
short_authors: Yang et al.
---
Fine-grained image recognition is very challenging due to the difficulty of
capturing both semantic global features and discriminative local features.
Meanwhile, these two features are not easy to be integrated, which are even
conflicting when used simultaneously. In this paper, a retrieval-based
coarse-to-fine framework is proposed, where we re-rank the TopN classification
results by using the local region enhanced embedding features to improve the
Top1 accuracy (based on the observation that the correct category usually
resides in TopN results). To obtain the discriminative regions for
distinguishing the fine-grained images, we introduce a weakly-supervised method
to train a box generating branch with only image-level labels. In addition, to
learn more effective semantic global features, we design a multi-level loss
over an automatically constructed hierarchical category structure. Experimental
results show that our method achieves state-of-the-art performance on three
benchmarks: CUB-200-2011, Stanford Cars, and FGVC Aircraft. Also,
visualizations and analysis are provided for better understanding.