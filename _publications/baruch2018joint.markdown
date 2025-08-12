---
layout: publication
title: Joint Detection And Matching Of Feature Points In Multimodal Images
authors: Elad Ben Baruch, Yosi Keller
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2021
bibkey: baruch2018joint
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.12941'}]
tags: []
short_authors: Elad Ben Baruch, Yosi Keller
---
In this work, we propose a novel Convolutional Neural Network (CNN)
architecture for the joint detection and matching of feature points in images
acquired by different sensors using a single forward pass. The resulting
feature detector is tightly coupled with the feature descriptor, in contrast to
classical approaches (SIFT, etc.), where the detection phase precedes and
differs from computing the descriptor. Our approach utilizes two CNN
subnetworks, the first being a Siamese CNN and the second, consisting of dual
non-weight-sharing CNNs. This allows simultaneous processing and fusion of the
joint and disjoint cues in the multimodal image patches. The proposed approach
is experimentally shown to outperform contemporary state-of-the-art schemes
when applied to multiple datasets of multimodal images. It is also shown to
provide repeatable feature points detections across multisensor images,
outperforming state-of-the-art detectors. To the best of our knowledge, it is
the first unified approach for the detection and matching of such images.