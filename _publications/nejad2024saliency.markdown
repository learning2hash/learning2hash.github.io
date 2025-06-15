---
layout: publication
title: 'Saliency Map-based Image Retrieval Using Invariant Krawtchouk Moments'
authors: Ashkan Nejad, Mohammad Reza Faraji, Xiaojun Qi
conference: "Arxiv"
year: 2024
citations: 0
bibkey: nejad2024saliency
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2411.08567'}
tags: ['Cross-Modal', 'Quantisation', 'Retrieval Models', 'Shallow', 'Datasets', 'Applications']
---
With the widespread adoption of digital devices equipped with cameras and the
rapid development of Internet technology, numerous content-based image
retrieval systems and novel image feature extraction techniques have emerged in
recent years. This paper introduces a saliency map-based image retrieval
approach using invariant Krawtchouk moments (SM-IKM) to enhance retrieval speed
and accuracy. The proposed method applies a global contrast-based salient
region detection algorithm to create a saliency map that effectively isolates
the foreground from the background. It then combines multiple orders of
invariant Krawtchouk moments (IKM) with local binary patterns (LBPs) and color
histograms to comprehensively represent the foreground and background.
Additionally, it incorporates LBPs derived from the saliency map to improve
discriminative power, facilitating more precise image differentiation. A
bag-of-visual-words (BoVW) model is employed to generate a codebook for
classification and discrimination. By using compact IKMs in the BoVW framework
and integrating a range of region-based feature-including color histograms,
LBPs, and saliency map-enhanced LBPs, our proposed SM-IKM achieves efficient
and accurate image retrieval. Extensive experiments on publicly available
datasets, such as Caltech 101 and Wang, demonstrate that SM-IKM outperforms
recent state-of-the-art retrieval methods. The source code for SM-IKM is
available at github.com/arnejad/SMIKM.
