---
layout: publication
title: 'Bent & Broken Bicycles: Leveraging Synthetic Data For Damaged Object Re-identification'
authors: "Luca Piano, Filippo Gabriele Prattic\xF2, Alessandro Sebastian Russo, Lorenzo\
  \ Lanari, Lia Morra, Fabrizio Lamberti"
conference: 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2023
bibkey: piano2023bent
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.07883'}]
tags: ["Datasets", "Image Retrieval"]
short_authors: Piano et al.
---
Instance-level object re-identification is a fundamental computer vision
task, with applications from image retrieval to intelligent monitoring and
fraud detection. In this work, we propose the novel task of damaged object
re-identification, which aims at distinguishing changes in visual appearance
due to deformations or missing parts from subtle intra-class variations. To
explore this task, we leverage the power of computer-generated imagery to
create, in a semi-automatic fashion, high-quality synthetic images of the same
bike before and after a damage occurs. The resulting dataset, Bent & Broken
Bicycles (BBBicycles), contains 39,200 images and 2,800 unique bike instances
spanning 20 different bike models. As a baseline for this task, we propose
TransReI3D, a multi-task, transformer-based deep network unifying damage
detection (framed as a multi-label classification task) with object
re-identification. The BBBicycles dataset is available at
https://huggingface.co/datasets/GrainsPolito/BBBicycles