---
layout: publication
title: A Zero-shot Framework For Sketch-based Image Retrieval
authors: Sasi Kiran Yelamarthi, Shiva Krishna Reddy, Ashish Mishra, Anurag Mittal
conference: Lecture Notes in Computer Science
year: 2018
bibkey: yelamarthi2018zero
citations: 184
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.11724'}]
tags: ["Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Yelamarthi et al.
---
Sketch-based image retrieval (SBIR) is the task of retrieving images from a
natural image database that correspond to a given hand-drawn sketch. Ideally,
an SBIR model should learn to associate components in the sketch (say, feet,
tail, etc.) with the corresponding components in the image having similar shape
characteristics. However, current evaluation methods simply focus only on
coarse-grained evaluation where the focus is on retrieving images which belong
to the same class as the sketch but not necessarily having the same shape
characteristics as in the sketch. As a result, existing methods simply learn to
associate sketches with classes seen during training and hence fail to
generalize to unseen classes. In this paper, we propose a new benchmark for
zero-shot SBIR where the model is evaluated in novel classes that are not seen
during training. We show through extensive experiments that existing models for
SBIR that are trained in a discriminative setting learn only class specific
mappings and fail to generalize to the proposed zero-shot setting. To
circumvent this, we propose a generative approach for the SBIR task by
proposing deep conditional generative models that take the sketch as an input
and fill the missing information stochastically. Experiments on this new
benchmark created from the "Sketchy" dataset, which is a large-scale database
of sketch-photo pairs demonstrate that the performance of these generative
models is significantly better than several state-of-the-art approaches in the
proposed zero-shot framework of the coarse-grained SBIR task.