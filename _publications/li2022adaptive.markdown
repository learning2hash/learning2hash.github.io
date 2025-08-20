---
layout: publication
title: Adaptive Structural Similarity Preserving For Unsupervised Cross Modal Hashing
authors: Liang Li, Baihua Zheng, Weiwei Sun
conference: Proceedings of the 30th ACM International Conference on Multimedia
year: 2022
bibkey: li2022adaptive
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.04214'}]
tags: [Hashing Methods, Unsupervised, Evaluation, Tools & Libraries, Neural Hashing]
short_authors: Liang Li, Baihua Zheng, Weiwei Sun
---
Cross-modal hashing is an important approach for multimodal data management
and application. Existing unsupervised cross-modal hashing algorithms mainly
rely on data features in pre-trained models to mine their similarity
relationships. However, their optimization objectives are based on the static
metric between the original uni-modal features, without further exploring data
correlations during the training. In addition, most of them mainly focus on
association mining and alignment among pairwise instances in continuous space
but ignore the latent structural correlations contained in the semantic hashing
space. In this paper, we propose an unsupervised hash learning framework,
namely Adaptive Structural Similarity Preservation Hashing (ASSPH), to solve
the above problems. Firstly, we propose an adaptive learning scheme, with
limited data and training batches, to enrich semantic correlations of unlabeled
instances during the training process and meanwhile to ensure a smooth
convergence of the training process. Secondly, we present an asymmetric
structural semantic representation learning scheme. We introduce structural
semantic metrics based on graph adjacency relations during the semantic
reconstruction and correlation mining stage and meanwhile align the structure
semantics in the hash space with an asymmetric binary optimization process.
Finally, we conduct extensive experiments to validate the enhancements of our
work in comparison with existing works.