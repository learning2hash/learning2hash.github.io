---
layout: publication
title: 'Tasks Integrated Networks: Joint Detection And Retrieval For Image Search'
authors: Lei Zhang, Zhenwei He, Yi Yang, Liang Wang, Xinbo Gao
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2020
bibkey: zhang2020tasks
citations: 37
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.01438'}]
tags: ["Datasets", "Image Retrieval", "Robustness"]
short_authors: Zhang et al.
---
The traditional object retrieval task aims to learn a discriminative feature
representation with intra-similarity and inter-dissimilarity, which supposes
that the objects in an image are manually or automatically pre-cropped exactly.
However, in many real-world searching scenarios (e.g., video surveillance), the
objects (e.g., persons, vehicles, etc.) are seldom accurately detected or
annotated. Therefore, object-level retrieval becomes intractable without
bounding-box annotation, which leads to a new but challenging topic, i.e.
image-level search. In this paper, to address the image search issue, we first
introduce an end-to-end Integrated Net (I-Net), which has three merits: 1) A
Siamese architecture and an on-line pairing strategy for similar and dissimilar
objects in the given images are designed. 2) A novel on-line pairing (OLP) loss
is introduced with a dynamic feature dictionary, which alleviates the
multi-task training stagnation problem, by automatically generating a number of
negative pairs to restrict the positives. 3) A hard example priority (HEP)
based softmax loss is proposed to improve the robustness of classification task
by selecting hard categories. With the philosophy of divide and conquer, we
further propose an improved I-Net, called DC-I-Net, which makes two new
contributions: 1) two modules are tailored to handle different tasks separately
in the integrated framework, such that the task specification is guaranteed. 2)
A class-center guided HEP loss (C2HEP) by exploiting the stored class centers
is proposed, such that the intra-similarity and inter-dissimilarity can be
captured for ultimate retrieval. Extensive experiments on famous image-level
search oriented benchmark datasets demonstrate that the proposed DC-I-Net
outperforms the state-of-the-art tasks-integrated and tasks-separated image
search models.