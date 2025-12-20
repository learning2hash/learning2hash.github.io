---
layout: publication
title: Scalable Change Retrieval Using Deep 3D Neural Codes
authors: Kojima Yusuke, Tanaka Kanji, Yang Naiming, Hirota Yuji
conference: Arxiv
year: 2019
bibkey: yusuke2019scalable
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.03552'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Supervised", "Unsupervised"]
short_authors: Yusuke et al.
---
We present a novel scalable framework for image change detection (ICD) from
an on-board 3D imagery system. We argue that existing ICD systems are
constrained by the time required to align a given query image with individual
reference image coordinates. We utilize an invariant coordinate system (ICS) to
replace the time-consuming image alignment with an offline pre-processing
procedure. Our key contribution is an extension of the traditional image
comparison-based ICD tasks to setups of the image retrieval (IR) task. We
replace each component of the 3D ICD system, i.e., (1) image modeling, (2)
image alignment, and (3) image differencing, with significantly efficient
variants from the bag-of-words (BoW) IR paradigm. Further, we train a deep 3D
feature extractor in an unsupervised manner using an unsupervised Siamese
network and automatically collected training data. We conducted experiments on
a challenging cross-season ICD task using a publicly available dataset and
thereby validate the efficacy of the proposed approach.