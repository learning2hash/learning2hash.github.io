---
layout: publication
title: "Weakly Supervised Deep Image Hashing through Tag Embeddings"
authors: Vijetha Gattupalli, Yaoxin Zhuo, Baoxin Li
conference: CVPR
year: 2019
bibkey: gattupalli2019weakly
additional_links:
   - {name: "Paper", url: "https://arxiv.org/abs/1806.05804"}
   - {name: "Code", url: "https://github.com/Vijetha1/WDHT"}
---
Many approaches to semantic image hashing have been formulated as supervised learning problems that utilize images and label information to learn the binary hash codes. However, large-scale labeled image data is expensive to obtain, thus imposing a restriction on the usage of such algorithms. On the other hand, unlabelled image data is abundant due to the existence of many Web image repositories. Such Web images may often come with images tags that contain useful information, although raw tags, in general, do not readily lead to semantic labels.
Motivated by this scenario, we formulate the problem of semantic image hashing as a weakly-supervised learning problem. We utilize the information contained in the user-generated tags associated with the images to learn the hash codes. More specifically, we extract the word2vec semantic embeddings of the tags and use the information contained in them for constraining the learning.
Accordingly, we name our model Weakly Supervised Deep Hashing using Tag Embeddings (WDHT). WDHT is tested for the task of semantic image retrieval and is compared against several state-of-art models. Results show that our approach sets a new state-of-art in the area of weekly supervised image hashing.
