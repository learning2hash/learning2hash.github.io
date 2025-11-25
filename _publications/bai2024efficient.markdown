---
layout: publication
title: Efficient 3D Implicit Head Avatar With Mesh-anchored Hash Table Blendshapes
authors: Ziqian Bai, Feitong Tan, Sean Fanello, Rohit Pandey, Mingsong Dou, Shichen
  Liu, Ping Tan, Yinda Zhang
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: bai2024efficient
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.01543'}]
tags: ["CVPR", "Efficiency"]
short_authors: Bai et al.
---
3D head avatars built with neural implicit volumetric representations have
achieved unprecedented levels of photorealism. However, the computational cost
of these methods remains a significant barrier to their widespread adoption,
particularly in real-time applications such as virtual reality and
teleconferencing. While attempts have been made to develop fast neural
rendering approaches for static scenes, these methods cannot be simply employed
to support realistic facial expressions, such as in the case of a dynamic
facial performance. To address these challenges, we propose a novel fast 3D
neural implicit head avatar model that achieves real-time rendering while
maintaining fine-grained controllability and high rendering quality. Our key
idea lies in the introduction of local hash table blendshapes, which are
learned and attached to the vertices of an underlying face parametric model.
These per-vertex hash-tables are linearly merged with weights predicted via a
CNN, resulting in expression dependent embeddings. Our novel representation
enables efficient density and color predictions using a lightweight MLP, which
is further accelerated by a hierarchical nearest neighbor search method.
Extensive experiments show that our approach runs in real-time while achieving
comparable rendering quality to state-of-the-arts and decent results on
challenging expressions.