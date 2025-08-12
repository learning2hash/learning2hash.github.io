---
layout: publication
title: A Secure Fingerprinting Framework For Distributed Image Classification
authors: Guowen Xu, Xingshuo Han, Anguo Zhang, Tianwei Zhang
conference: Arxiv
year: 2022
bibkey: xu2022secure
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.04668'}]
tags: ["Robustness"]
short_authors: Xu et al.
---
The deep learning (DL) technology has been widely used for image
classification in many scenarios, e.g., face recognition and suspect tracking.
Such a highly commercialized application has given rise to intellectual
property protection of its DL model. To combat that, the mainstream method is
to embed a unique watermark into the target model during the training process.
However, existing efforts focus on detecting copyright infringement for a given
model, while rarely consider the problem of traitors tracking. Moreover, the
watermark embedding process can incur privacy issues for the training data in a
distributed manner. In this paper, we propose SECUREMARK-DL, a novel
fingerprinting framework to address the above two problems in a distributed
learning environment. It embeds a unique fingerprint into the target model for
each customer, which can be extracted and verified from any suspicious model
once a dispute arises. In addition, it adopts a new privacy partitioning
technique in the training process to protect the training data privacy.
Extensive experiments demonstrate the robustness of SECUREMARK-DL against
various attacks, and its high classification accuracy (> 95%) even if a
long-bit (304-bit) fingerprint is embedded into an input image.