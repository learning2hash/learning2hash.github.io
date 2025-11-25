---
layout: publication
title: Affine Steerers For Structured Keypoint Description
authors: "Georg B\xF6kman, Johan Edstedt, Michael Felsberg, Fredrik Kahl"
conference: Lecture Notes in Computer Science
year: 2024
bibkey: "b\xF6kman2024affine"
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.14186'}]
tags: ["Evaluation", "Image Retrieval"]
short_authors: "B\xF6kman et al."
---
We propose a way to train deep learning based keypoint descriptors that makes
them approximately equivariant for locally affine transformations of the image
plane. The main idea is to use the representation theory of GL(2) to generalize
the recently introduced concept of steerers from rotations to affine
transformations. Affine steerers give high control over how keypoint
descriptions transform under image transformations. We demonstrate the
potential of using this control for image matching. Finally, we propose a way
to finetune keypoint descriptors with a set of steerers on upright images and
obtain state-of-the-art results on several standard benchmarks. Code will be
published at github.com/georg-bn/affine-steerers.