---
layout: publication
title: Dual Prototypical Contrastive Learning For Few-shot Semantic Segmentation
authors: Hyeongjun Kwon, Somi Jeong, Sunok Kim, Kwanghoon Sohn
conference: Arxiv
year: 2021
bibkey: kwon2021dual
citations: 9
additional_links: [{name: Code, url: 'https://github.com/kwonjunn01/DPCL1'}, {name: Paper,
    url: 'https://arxiv.org/abs/2111.04982'}]
tags: ["Few Shot & Zero Shot", "Self-Supervised"]
short_authors: Kwon et al.
---
We address the problem of few-shot semantic segmentation (FSS), which aims to
segment novel class objects in a target image with a few annotated samples.
Though recent advances have been made by incorporating prototype-based metric
learning, existing methods still show limited performance under extreme
intra-class object variations and semantically similar inter-class objects due
to their poor feature representation. To tackle this problem, we propose a dual
prototypical contrastive learning approach tailored to the FSS task to capture
the representative semanticfeatures effectively. The main idea is to encourage
the prototypes more discriminative by increasing inter-class distance while
reducing intra-class distance in prototype feature space. To this end, we first
present a class-specific contrastive loss with a dynamic prototype dictionary
that stores the class-aware prototypes during training, thus enabling the same
class prototypes similar and the different class prototypes to be dissimilar.
Furthermore, we introduce a class-agnostic contrastive loss to enhance the
generalization ability to unseen classes by compressing the feature
distribution of semantic class within each episode. We demonstrate that the
proposed dual prototypical contrastive learning approach outperforms
state-of-the-art FSS methods on PASCAL-5i and COCO-20i datasets. The code is
available at:https://github.com/kwonjunn01/DPCL1.