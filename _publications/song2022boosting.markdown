---
layout: publication
title: 'Boosting Vision Transformers For Image Retrieval'
authors: Chull Hwan Song, Jooyoung Yoon, Shunghyun Choi, Yannis Avrithis
conference: "Arxiv"
year: 2022
citations: 28
bibkey: song2022boosting
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2210.11909'}
  - {name: "Code", url: 'https://github.com/dealicious-inc/DToP'}
tags: ['Cross-Modal', 'Deep', 'Model Design', 'Retrieval Models', 'Has Code', 'Supervised', 'Training Strategy', 'Applications']
---
Vision transformers have achieved remarkable progress in vision tasks such as
image classification and detection. However, in instance-level image retrieval,
transformers have not yet shown good performance compared to convolutional
networks. We propose a number of improvements that make transformers outperform
the state of the art for the first time. (1) We show that a hybrid architecture
is more effective than plain transformers, by a large margin. (2) We introduce
two branches collecting global (classification token) and local (patch tokens)
information, from which we form a global image representation. (3) In each
branch, we collect multi-layer features from the transformer encoder,
corresponding to skip connections across distant layers. (4) We enhance
locality of interactions at the deeper layers of the encoder, which is the
relative weakness of vision transformers. We train our model on all commonly
used training sets and, for the first time, we make fair comparisons separately
per training set. In all cases, we outperform previous models based on global
representation. Public code is available at
https://github.com/dealicious-inc/DToP.
