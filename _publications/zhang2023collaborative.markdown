---
layout: publication
title: 'Collaborative Group: Composed Image Retrieval Via Consensus Learning From
  Noisy Annotations'
authors: Xu Zhang, Zhedong Zheng, Linchao Zhu, Yi Yang
conference: Knowl. Based. Syst. 300 (2024) 112135
year: 2023
bibkey: zhang2023collaborative
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.02092'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Zhang et al.
---
Composed image retrieval extends content-based image retrieval systems by
enabling users to search using reference images and captions that describe
their intention. Despite great progress in developing image-text compositors to
extract discriminative visual-linguistic features, we identify a hitherto
overlooked issue, triplet ambiguity, which impedes robust feature extraction.
Triplet ambiguity refers to a type of semantic ambiguity that arises between
the reference image, the relative caption, and the target image. It is mainly
due to the limited representation of the annotated text, resulting in many
noisy triplets where multiple visually dissimilar candidate images can be
matched to an identical reference pair (i.e., a reference image + a relative
caption). To address this challenge, we propose the Consensus Network
(Css-Net), inspired by the psychological concept that groups outperform
individuals. Css-Net comprises two core components: (1) a consensus module with
four diverse compositors, each generating distinct image-text embeddings,
fostering complementary feature extraction and mitigating dependence on any
single, potentially biased compositor; (2) a Kullback-Leibler divergence loss
that encourages learning of inter-compositor interactions to promote consensual
outputs. During evaluation, the decisions of the four compositors are combined
through a weighting scheme, enhancing overall agreement. On benchmark datasets,
particularly FashionIQ, Css-Net demonstrates marked improvements. Notably, it
achieves significant recall gains, with a 2.77% increase in R@10 and 6.67%
boost in R@50, underscoring its competitiveness in addressing the fundamental
limitations of existing methods.