---
layout: publication
title: 'Efficient Diffusion On Region Manifolds: Recovering Small Objects With Compact
  CNN Representations'
authors: Ahmet Iscen, Giorgos Tolias, Yannis Avrithis, Teddy Furon, Ondrej Chum
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: iscen2016efficient
citations: 188
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.05113'}]
tags: [Image Retrieval, Efficiency, CVPR, Evaluation]
short_authors: Iscen et al.
---
Query expansion is a popular method to improve the quality of image retrieval
with both conventional and CNN representations. It has been so far limited to
global image similarity. This work focuses on diffusion, a mechanism that
captures the image manifold in the feature space. The diffusion is carried out
on descriptors of overlapping image regions rather than on a global image
descriptor like in previous approaches. An efficient off-line stage allows
optional reduction in the number of stored regions. In the on-line stage, the
proposed handling of unseen queries in the indexing stage removes additional
computation to adjust the precomputed data. We perform diffusion through a
sparse linear system solver, yielding practical query times well below one
second. Experimentally, we observe a significant boost in performance of image
retrieval with compact CNN descriptors on standard benchmarks, especially when
the query object covers only a small part of the image. Small objects have been
a common failure case of CNN-based retrieval.