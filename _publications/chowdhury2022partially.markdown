---
layout: publication
title: 'Partially Does It: Towards Scene-level FG-SBIR With Partial Input'
authors: Pinaki Nath Chowdhury, Ayan Kumar Bhunia, Viswanatha Reddy Gajjala, Aneeshan
  Sain, Tao Xiang, Yi-Zhe Song
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: chowdhury2022partially
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.14804'}]
tags: ["CVPR", "Datasets", "Evaluation", "Image Retrieval"]
short_authors: Chowdhury et al.
---
We scrutinise an important observation plaguing scene-level sketch research
-- that a significant portion of scene sketches are "partial". A quick pilot
study reveals: (i) a scene sketch does not necessarily contain all objects in
the corresponding photo, due to the subjective holistic interpretation of
scenes, (ii) there exists significant empty (white) regions as a result of
object-level abstraction, and as a result, (iii) existing scene-level
fine-grained sketch-based image retrieval methods collapse as scene sketches
become more partial. To solve this "partial" problem, we advocate for a simple
set-based approach using optimal transport (OT) to model cross-modal region
associativity in a partially-aware fashion. Importantly, we improve upon OT to
further account for holistic partialness by comparing intra-modal adjacency
matrices. Our proposed method is not only robust to partial scene-sketches but
also yields state-of-the-art performance on existing datasets.