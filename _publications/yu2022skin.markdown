---
layout: publication
title: Skin Lesion Recognition With Class-hierarchy Regularized Hyperbolic Embeddings
authors: Zhen Yu, Toan Nguyen, Yaniv Gal, Lie Ju, Shekhar S. Chandra, Lei Zhang, Paul
  Bonnington, Victoria Mar, Zhiyong Wang, Zongyuan Ge
conference: Lecture Notes in Computer Science
year: 2022
bibkey: yu2022skin
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.05842'}]
tags: []
short_authors: Yu et al.
---
In practice, many medical datasets have an underlying taxonomy defined over
the disease label space. However, existing classification algorithms for
medical diagnoses often assume semantically independent labels. In this study,
we aim to leverage class hierarchy with deep learning algorithms for more
accurate and reliable skin lesion recognition. We propose a hyperbolic network
to learn image embeddings and class prototypes jointly. The hyperbola provably
provides a space for modeling hierarchical relations better than Euclidean
geometry. Meanwhile, we restrict the distribution of hyperbolic prototypes with
a distance matrix that is encoded from the class hierarchy. Accordingly, the
learned prototypes preserve the semantic class relations in the embedding space
and we can predict the label of an image by assigning its feature to the
nearest hyperbolic class prototype. We use an in-house skin lesion dataset
which consists of around 230k dermoscopic images on 65 skin diseases to verify
our method. Extensive experiments provide evidence that our model can achieve
higher accuracy with less severe classification errors than models without
considering class relations.