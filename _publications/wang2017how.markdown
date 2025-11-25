---
layout: publication
title: How To Train Triplet Networks With 100K Identities?
authors: Chong Wang, Xue Zhang, Xipeng Lan
conference: 2017 IEEE International Conference on Computer Vision Workshops (ICCVW)
year: 2017
bibkey: wang2017how
citations: 45
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.02940'}]
tags: ["ICCV", "Image Retrieval", "Scalability"]
short_authors: Chong Wang, Xue Zhang, Xipeng Lan
---
Training triplet networks with large-scale data is challenging in face
recognition. Due to the number of possible triplets explodes with the number of
samples, previous studies adopt the online hard negative mining(OHNM) to handle
it. However, as the number of identities becomes extremely large, the training
will suffer from bad local minima because effective hard triplets are difficult
to be found. To solve the problem, in this paper, we propose training triplet
networks with subspace learning, which splits the space of all identities into
subspaces consisting of only similar identities. Combined with the batch OHNM,
hard triplets can be found much easier. Experiments on the large-scale
MS-Celeb-1M challenge with 100K identities demonstrate that the proposed method
can largely improve the performance. In addition, to deal with heavy noise and
large-scale retrieval, we also make some efforts on robust noise removing and
efficient image retrieval, which are used jointly with the subspace learning to
obtain the state-of-the-art performance on the MS-Celeb-1M competition (without
external data in Challenge1).