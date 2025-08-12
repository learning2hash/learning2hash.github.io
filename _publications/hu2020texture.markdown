---
layout: publication
title: Texture Classification Using Block Intensity And Gradient Difference (BIGD)
  Descriptor
authors: Yuting Hu, Zhen Wang, Ghassan Alregib
conference: 'Signal Processing: Image Communication'
year: 2020
bibkey: hu2020texture
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.01154'}]
tags: []
short_authors: Yuting Hu, Zhen Wang, Ghassan Alregib
---
In this paper, we present an efficient and distinctive local descriptor,
namely block intensity and gradient difference (BIGD). In an image patch, we
randomly sample multi-scale block pairs and utilize the intensity and gradient
differences of pairwise blocks to construct the local BIGD descriptor. The
random sampling strategy and the multi-scale framework help BIGD descriptors
capture the distinctive patterns of patches at different orientations and
spatial granularity levels. We use vectors of locally aggregated descriptors
(VLAD) or improved Fisher vector (IFV) to encode local BIGD descriptors into a
full image descriptor, which is then fed into a linear support vector machine
(SVM) classifier for texture classification. We compare the proposed descriptor
with typical and state-of-the-art ones by evaluating their classification
performance on five public texture data sets including Brodatz, CUReT,
KTH-TIPS, and KTH-TIPS-2a and -2b. Experimental results show that the proposed
BIGD descriptor with stronger discriminative power yields 0.12% ~ 6.43% higher
classification accuracy than the state-of-the-art texture descriptor, dense
microblock difference (DMD).