---
layout: publication
title: Cross Euclidean-to-riemannian Metric Learning With Application To Face Recognition
  From Video
authors: Zhiwu Huang, Ruiping Wang, Shiguang Shan, Luc van Gool, Xilin Chen
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2017
bibkey: huang2016cross
citations: 77
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1608.04200'}]
tags: ["Distance Metric Learning"]
short_authors: Huang et al.
---
Riemannian manifolds have been widely employed for video representations in
visual classification tasks including video-based face recognition. The success
mainly derives from learning a discriminant Riemannian metric which encodes the
non-linear geometry of the underlying Riemannian manifolds. In this paper, we
propose a novel metric learning framework to learn a distance metric across a
Euclidean space and a Riemannian manifold to fuse the average appearance and
pattern variation of faces within one video. The proposed metric learning
framework can handle three typical tasks of video-based face recognition:
Video-to-Still, Still-to-Video and Video-to-Video settings. To accomplish this
new framework, by exploiting typical Riemannian geometries for kernel
embedding, we map the source Euclidean space and Riemannian manifold into a
common Euclidean subspace, each through a corresponding high-dimensional
Reproducing Kernel Hilbert Space (RKHS). With this mapping, the problem of
learning a cross-view metric between the two source heterogeneous spaces can be
expressed as learning a single-view Euclidean distance metric in the target
common Euclidean space. By learning information on heterogeneous data with the
shared label, the discriminant metric in the common space improves face
recognition from videos. Extensive experiments on four challenging video face
databases demonstrate that the proposed framework has a clear advantage over
the state-of-the-art methods in the three classical video-based face
recognition tasks.