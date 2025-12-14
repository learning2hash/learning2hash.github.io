---
layout: publication
title: Semantic-aware Knowledge Preservation For Zero-shot Sketch-based Image Retrieval
authors: Qing Liu, Lingxi Xie, Huiyu Wang, Alan Yuille
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: liu2019semantic
citations: 116
additional_links: [{name: Code, url: 'https://github.com/qliu24/SAKE'}, {name: Paper,
    url: 'https://arxiv.org/abs/1904.03208'}]
tags: [Evaluation, ICCV, Image Retrieval, Few-shot & Zero-shot, Datasets, Tools &
    Libraries]
short_authors: Liu et al.
---
Sketch-based image retrieval (SBIR) is widely recognized as an important
vision problem which implies a wide range of real-world applications. Recently,
research interests arise in solving this problem under the more realistic and
challenging setting of zero-shot learning. In this paper, we investigate this
problem from the viewpoint of domain adaptation which we show is critical in
improving feature embedding in the zero-shot scenario. Based on a framework
which starts with a pre-trained model on ImageNet and fine-tunes it on the
training set of SBIR benchmark, we advocate the importance of preserving
previously acquired knowledge, e.g., the rich discriminative features learned
from ImageNet, to improve the model's transfer ability. For this purpose, we
design an approach named Semantic-Aware Knowledge prEservation (SAKE), which
fine-tunes the pre-trained model in an economical way and leverages semantic
information, e.g., inter-class relationship, to achieve the goal of knowledge
preservation. Zero-shot experiments on two extended SBIR datasets, TU-Berlin
and Sketchy, verify the superior performance of our approach. Extensive
diagnostic experiments validate that knowledge preserved benefits SBIR in
zero-shot settings, as a large fraction of the performance gain is from the
more properly structured feature embedding for photo images. Code is available
at: https://github.com/qliu24/SAKE.