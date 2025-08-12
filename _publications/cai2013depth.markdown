---
layout: publication
title: Depth-dependent Parallel Visualization With 3D Stylized Dense Tubes
authors: Haipeng Cai, Jian Chen, Alexander P. Auchus
conference: International Journal of Image and Graphics. Vol. 16 No. 01 1650002 (2016)
year: 2013
bibkey: cai2013depth
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1310.2994'}]
tags: []
short_authors: Haipeng Cai, Jian Chen, Alexander P. Auchus
---
We present a parallel visualization algorithm for the illustrative rendering
of depth-dependent stylized dense tube data at interactive frame rates. While
this computation could be efficiently performed on a GPU device, we target a
parallel framework to enable it to be efficiently running on an ordinary
multi-core CPU platform which is much more available than GPUs for common
users. Our approach is to map the depth information in each tube onto each of
the visual dimensions of shape, color, texture, value, and size on the basis of
Bertin's semiology theory. The purpose is to enable more legible displays in
the dense tube environments. A major contribution of our work is an efficient
and effective parallel depthordering algorithm that makes use of the message
passing interface (MPI) with VTK. We evaluated our framework with
visualizations of depth-stylized tubes derived from 3D diffusion tensor MRI
data by comparing its efficiency with several other alternative parallelization
platforms running the same computations. As our results show, the
parallelization framework we proposed can efficiently render highly dense 3D
data sets like the tube data and thus is useful as a complement to parallel
visualization environments that rely on GPUs.