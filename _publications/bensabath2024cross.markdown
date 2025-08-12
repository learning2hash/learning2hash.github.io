---
layout: publication
title: A Cross-dataset Study For Text-based 3D Human Motion Retrieval
authors: "L\xE9ore Bensabath, Mathis Petrovich, G\xFCl Varol"
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2024
bibkey: bensabath2024cross
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.16909'}]
tags: ["CVPR", "Datasets"]
short_authors: "L\xE9ore Bensabath, Mathis Petrovich, G\xFCl Varol"
---
We provide results of our study on text-based 3D human motion retrieval and
particularly focus on cross-dataset generalization. Due to practical reasons
such as dataset-specific human body representations, existing works typically
benchmarkby training and testing on partitions from the same dataset. Here, we
employ a unified SMPL body format for all datasets, which allows us to perform
training on one dataset, testing on the other, as well as training on a
combination of datasets. Our results suggest that there exist dataset biases in
standard text-motion benchmarks such as HumanML3D, KIT Motion-Language, and
BABEL. We show that text augmentations help close the domain gap to some
extent, but the gap remains. We further provide the first zero-shot action
recognition results on BABEL, without using categorical action labels during
training, opening up a new avenue for future research.