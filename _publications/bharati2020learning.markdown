---
layout: publication
title: Learning Transformation-aware Embeddings For Image Forensics
authors: Aparna Bharati, Daniel Moreira, Patrick Flynn, Anderson Rocha, Kevin Bowyer,
  Walter Scheirer
conference: Arxiv
year: 2020
bibkey: bharati2020learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.04547'}]
tags: ["Image Retrieval", "Privacy & Security", "Robustness"]
short_authors: Bharati et al.
---
A dramatic rise in the flow of manipulated image content on the Internet has
led to an aggressive response from the media forensics research community. New
efforts have incorporated increased usage of techniques from computer vision
and machine learning to detect and profile the space of image manipulations.
This paper addresses Image Provenance Analysis, which aims at discovering
relationships among different manipulated image versions that share content.
One of the main sub-problems for provenance analysis that has not yet been
addressed directly is the edit ordering of images that share full content or
are near-duplicates. The existing large networks that generate image
descriptors for tasks such as object recognition may not encode the subtle
differences between these image covariates. This paper introduces a novel deep
learning-based approach to provide a plausible ordering to images that have
been generated from a single image through transformations. Our approach learns
transformation-aware descriptors using weak supervision via composited
transformations and a rank-based quadruplet loss. To establish the efficacy of
the proposed approach, comparisons with state-of-the-art handcrafted and deep
learning-based descriptors, and image matching approaches are made. Further
experimentation validates the proposed approach in the context of image
provenance analysis.