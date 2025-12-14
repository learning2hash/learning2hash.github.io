---
layout: publication
title: Pedestrian Alignment Network For Large-scale Person Re-identification
authors: Zhedong Zheng, Liang Zheng, Yi Yang
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2017
bibkey: zheng2017pedestrian
citations: 550
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.00408'}]
tags: [Scalability, Image Retrieval, Datasets]
short_authors: Zhedong Zheng, Liang Zheng, Yi Yang
---
Person re-identification (person re-ID) is mostly viewed as an image
retrieval problem. This task aims to search a query person in a large image
pool. In practice, person re-ID usually adopts automatic detectors to obtain
cropped pedestrian images. However, this process suffers from two types of
detector errors: excessive background and part missing. Both errors deteriorate
the quality of pedestrian alignment and may compromise pedestrian matching due
to the position and scale variances. To address the misalignment problem, we
propose that alignment can be learned from an identification procedure. We
introduce the pedestrian alignment network (PAN) which allows discriminative
embedding learning and pedestrian alignment without extra annotations. Our key
observation is that when the convolutional neural network (CNN) learns to
discriminate between different identities, the learned feature maps usually
exhibit strong activations on the human body rather than the background. The
proposed network thus takes advantage of this attention mechanism to adaptively
locate and align pedestrians within a bounding box. Visual examples show that
pedestrians are better aligned with PAN. Experiments on three large-scale re-ID
datasets confirm that PAN improves the discriminative ability of the feature
embeddings and yields competitive accuracy with the state-of-the-art methods.