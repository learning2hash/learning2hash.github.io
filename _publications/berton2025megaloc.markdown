---
layout: publication
title: 'Megaloc: One Retrieval To Place Them All'
authors: Gabriele Berton, Carlo Masone
conference: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2025
bibkey: berton2025megaloc
citations: 0
additional_links: [{name: Code, url: 'https://github.com/gmberton/MegaLoc'}, {name: Paper,
    url: 'https://arxiv.org/abs/2502.17237'}]
tags: ["CVPR", "Datasets", "Image Retrieval"]
short_authors: Gabriele Berton, Carlo Masone
---
Retrieving images from the same location as a given query is an important component of multiple computer vision tasks, like Visual Place Recognition, Landmark Retrieval, Visual Localization, 3D reconstruction, and SLAM. However, existing solutions are built to specifically work for one of these tasks, and are known to fail when the requirements slightly change or when they meet out-of-distribution data. In this paper we combine a variety of existing methods, training techniques, and datasets to train a retrieval model, called MegaLoc, that is performant on multiple tasks. We find that MegaLoc (1) achieves state of the art on a large number of Visual Place Recognition datasets, (2) impressive results on common Landmark Retrieval datasets, and (3) sets a new state of the art for Visual Localization on the LaMAR datasets, where we only changed the retrieval method to the existing localization pipeline. The code for MegaLoc is available at https://github.com/gmberton/MegaLoc