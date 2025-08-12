---
layout: publication
title: 'Foundpose: Unseen Object Pose Estimation With Foundation Features'
authors: "Evin P\u0131nar \xD6rnek, Yann Labb\xE9, Bugra Tekin, Lingni Ma, Cem Keskin,\
  \ Christian Forster, Tomas Hodan"
conference: Lecture Notes in Computer Science
year: 2024
bibkey: "\xF6rnek2023foundpose"
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.18809'}]
tags: []
short_authors: "\xD6rnek et al."
---
We propose FoundPose, a model-based method for 6D pose estimation of unseen
objects from a single RGB image. The method can quickly onboard new objects
using their 3D models without requiring any object- or task-specific training.
In contrast, existing methods typically pre-train on large-scale, task-specific
datasets in order to generalize to new objects and to bridge the image-to-model
domain gap. We demonstrate that such generalization capabilities can be
observed in a recent vision foundation model trained in a self-supervised
manner. Specifically, our method estimates the object pose from image-to-model
2D-3D correspondences, which are established by matching patch descriptors from
the recent DINOv2 model between the image and pre-rendered object templates. We
find that reliable correspondences can be established by kNN matching of patch
descriptors from an intermediate DINOv2 layer. Such descriptors carry stronger
positional information than descriptors from the last layer, and we show their
importance when semantic information is ambiguous due to object symmetries or a
lack of texture. To avoid establishing correspondences against all object
templates, we develop an efficient template retrieval approach that integrates
the patch descriptors into the bag-of-words representation and can promptly
propose a handful of similarly looking templates. Additionally, we apply
featuremetric alignment to compensate for discrepancies in the 2D-3D
correspondences caused by coarse patch sampling. The resulting method
noticeably outperforms existing RGB methods for refinement-free pose estimation
on the standard BOP benchmark with seven diverse datasets and can be seamlessly
combined with an existing render-and-compare refinement method to achieve
RGB-only state-of-the-art results. Project page: evinpinar.github.io/foundpose.