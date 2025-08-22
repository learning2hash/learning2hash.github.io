---
layout: publication
title: 'Pointnetvlad: Deep Point Cloud Based Retrieval For Large-scale Place Recognition'
authors: Mikaela Angelina Uy, Gim Hee Lee
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: uy2018pointnetvlad
citations: 484
additional_links: [{name: Code, url: 'http://github.com/mikacuy/pointnetvlad/'}, {
    name: Paper, url: 'https://arxiv.org/abs/1804.03492'}]
tags: ["CVPR", "Datasets", "Evaluation", "Scalability"]
short_authors: Mikaela Angelina Uy, Gim Hee Lee
---
Unlike its image based counterpart, point cloud based retrieval for place
recognition has remained as an unexplored and unsolved problem. This is largely
due to the difficulty in extracting local feature descriptors from a point
cloud that can subsequently be encoded into a global descriptor for the
retrieval task. In this paper, we propose the PointNetVLAD where we leverage on
the recent success of deep networks to solve point cloud based retrieval for
place recognition. Specifically, our PointNetVLAD is a combination/modification
of the existing PointNet and NetVLAD, which allows end-to-end training and
inference to extract the global descriptor from a given 3D point cloud.
Furthermore, we propose the "lazy triplet and quadruplet" loss functions that
can achieve more discriminative and generalizable global descriptors to tackle
the retrieval task. We create benchmark datasets for point cloud based
retrieval for place recognition, and the experimental results on these datasets
show the feasibility of our PointNetVLAD. Our code and the link for the
benchmark dataset downloads are available in our project website.
http://github.com/mikacuy/pointnetvlad/