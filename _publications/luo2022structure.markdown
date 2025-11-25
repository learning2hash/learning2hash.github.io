---
layout: publication
title: Structure-aware 3D VR Sketch To 3D Shape Retrieval
authors: Ling Luo, Yulia Gryaditskaya, Tao Xiang, Yi-Zhe Song
conference: 2022 International Conference on 3D Vision (3DV)
year: 2022
bibkey: luo2022structure
citations: 9
additional_links: [{name: Code, url: 'https://github.com/Rowl1ng/Structure-Aware-VR-Sketch-Shape-Retrieval'},
  {name: Paper, url: 'https://arxiv.org/abs/2209.09043'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation"]
short_authors: Luo et al.
---
We study the practical task of fine-grained 3D-VR-sketch-based 3D shape
retrieval. This task is of particular interest as 2D sketches were shown to be
effective queries for 2D images. However, due to the domain gap, it remains
hard to achieve strong performance in 3D shape retrieval from 2D sketches.
Recent work demonstrated the advantage of 3D VR sketching on this task. In our
work, we focus on the challenge caused by inherent inaccuracies in 3D VR
sketches. We observe that retrieval results obtained with a triplet loss with a
fixed margin value, commonly used for retrieval tasks, contain many irrelevant
shapes and often just one or few with a similar structure to the query. To
mitigate this problem, we for the first time draw a connection between adaptive
margin values and shape similarities. In particular, we propose to use a
triplet loss with an adaptive margin value driven by a "fitting gap", which is
the similarity of two shapes under structure-preserving deformations. We also
conduct a user study which confirms that this fitting gap is indeed a suitable
criterion to evaluate the structural similarity of shapes. Furthermore, we
introduce a dataset of 202 VR sketches for 202 3D shapes drawn from memory
rather than from observation. The code and data are available at
https://github.com/Rowl1ng/Structure-Aware-VR-Sketch-Shape-Retrieval.