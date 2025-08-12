---
layout: publication
title: Learning Co-segmentation By Segment Swapping For Retrieval And Discovery
authors: Xi Shen, Alexei A. Efros, Armand Joulin, Mathieu Aubry
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2022
bibkey: shen2021learning
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.15904'}]
tags: ["CVPR"]
short_authors: Shen et al.
---
The goal of this work is to efficiently identify visually similar patterns in
images, e.g. identifying an artwork detail copied between an engraving and an
oil painting, or recognizing parts of a night-time photograph visible in its
daytime counterpart. Lack of training data is a key challenge for this
co-segmentation task. We present a simple yet surprisingly effective approach
to overcome this difficulty: we generate synthetic training pairs by selecting
segments in an image and copy-pasting them into another image. We then learn to
predict the repeated region masks. We find that it is crucial to predict the
correspondences as an auxiliary task and to use Poisson blending and style
transfer on the training pairs to generalize on real data. We analyse results
with two deep architectures relevant to our joint image analysis task: a
transformer-based architecture and Sparse Nc-Net, a recent network designed to
predict coarse correspondences using 4D convolutions. We show our approach
provides clear improvements for artwork details retrieval on the Brueghel
dataset and achieves competitive performance on two place recognition
benchmarks, Tokyo247 and Pitts30K. We also demonstrate the potential of our
approach for unsupervised image collection analysis by introducing a spectral
graph clustering approach to object discovery and demonstrating it on the
object discovery dataset of \cite\{rubinstein2013unsupervised\} and the Brueghel
dataset. Our code and data are available at
http://imagine.enpc.fr/~shenx/SegSwap/.