---
layout: publication
title: Multi-shot Person Re-identification Via Relational Stein Divergence
authors: Azadeh Alavi, Yan Yang, Mehrtash Harandi, Conrad Sanderson
conference: 2013 IEEE International Conference on Image Processing
year: 2013
bibkey: alavi2013multi
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1403.0699'}]
tags: []
short_authors: Alavi et al.
---
Person re-identification is particularly challenging due to significant
appearance changes across separate camera views. In order to re-identify
people, a representative human signature should effectively handle differences
in illumination, pose and camera parameters. While general appearance-based
methods are modelled in Euclidean spaces, it has been argued that some
applications in image and video analysis are better modelled via non-Euclidean
manifold geometry. To this end, recent approaches represent images as
covariance matrices, and interpret such matrices as points on Riemannian
manifolds. As direct classification on such manifolds can be difficult, in this
paper we propose to represent each manifold point as a vector of similarities
to class representers, via a recently introduced form of Bregman matrix
divergence known as the Stein divergence. This is followed by using a
discriminative mapping of similarity vectors for final classification. The use
of similarity vectors is in contrast to the traditional approach of embedding
manifolds into tangent spaces, which can suffer from representing the manifold
structure inaccurately. Comparative evaluations on benchmark ETHZ and iLIDS
datasets for the person re-identification task show that the proposed approach
obtains better performance than recent techniques such as Histogram Plus
Epitome, Partial Least Squares, and Symmetry-Driven Accumulation of Local
Features.