---
layout: publication
title: 'Leveraging Cutting Edge Deep Learning Based Image Matching For Reconstructing A Large Scene From Sparse Images'
authors: Georg Bökman, Johan Edstedt
conference: "Arxiv"
year: 2023
citations: 0
bibkey: bökman2023leveraging
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2310.01092'}
tags: ['Cross-Modal', 'Deep', 'Unsupervised', 'Retrieval Models', 'Conferences', 'Applications']
---
We present the top ranked solution for the AISG-SLA Visual Localisation
Challenge benchmark (IJCAI 2023), where the task is to estimate relative motion
between images taken in sequence by a camera mounted on a car driving through
an urban scene.
  For matching images we use our recent deep learning based matcher RoMa.
Matching image pairs sequentially and estimating relative motion from point
correspondences sampled by RoMa already gives very competitive results -- third
rank on the challenge benchmark.
  To improve the estimations we extract keypoints in the images, match them
using RoMa, and perform structure from motion reconstruction using COLMAP. We
choose our recent DeDoDe keypoints for their high repeatability. Further, we
address time jumps in the image sequence by matching specific non-consecutive
image pairs based on image retrieval with DINOv2. These improvements yield a
solution beating all competitors.
  We further present a loose upper bound on the accuracy obtainable by the
image retrieval approach by also matching hand-picked non-consecutive pairs.
