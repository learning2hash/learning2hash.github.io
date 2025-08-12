---
layout: publication
title: Faster Matrix Completion Using Randomized SVD
authors: Xu Feng, Wenjian Yu, Yaohang Li
conference: 2018 IEEE 30th International Conference on Tools with Artificial Intelligence
  (ICTAI)
year: 2018
bibkey: feng2018faster
citations: 35
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.06860'}]
tags: []
short_authors: Xu Feng, Wenjian Yu, Yaohang Li
---
Matrix completion is a widely used technique for image inpainting and
personalized recommender system, etc. In this work, we focus on accelerating
the matrix completion using faster randomized singular value decomposition
(rSVD). Firstly, two fast randomized algorithms (rSVD-PI and rSVD- BKI) are
proposed for handling sparse matrix. They make use of an eigSVD procedure and
several accelerating skills. Then, with the rSVD-BKI algorithm and a new
subspace recycling technique, we accelerate the singular value thresholding
(SVT) method in [1] to realize faster matrix completion. Experiments show that
the proposed rSVD algorithms can be 6X faster than the basic rSVD algorithm [2]
while keeping same accuracy. For image inpainting and movie-rating estimation
problems, the proposed accelerated SVT algorithm consumes 15X and 8X less CPU
time than the methods using svds and lansvd respectively, without loss of
accuracy.