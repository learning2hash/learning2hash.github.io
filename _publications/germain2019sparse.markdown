---
layout: publication
title: Sparse-to-dense Hypercolumn Matching For Long-term Visual Localization
authors: Hugo Germain, Guillaume Bourmaud, Vincent Lepetit
conference: 2019 International Conference on 3D Vision (3DV)
year: 2019
bibkey: germain2019sparse
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.03965'}]
tags: [Datasets]
short_authors: Hugo Germain, Guillaume Bourmaud, Vincent Lepetit
---
We propose a novel approach to feature point matching, suitable for robust
and accurate outdoor visual localization in long-term scenarios. Given a query
image, we first match it against a database of registered reference images,
using recent retrieval techniques. This gives us a first estimate of the camera
pose. To refine this estimate, like previous approaches, we match 2D points
across the query image and the retrieved reference image. This step, however,
is prone to fail as it is still very difficult to detect and match sparse
feature points across images captured in potentially very different conditions.
Our key contribution is to show that we need to extract sparse feature points
only in the retrieved reference image: We then search for the corresponding 2D
locations in the query image exhaustively. This search can be performed
efficiently using convolutional operations, and robustly by using hypercolumn
descriptors, i.e. image features computed for retrieval. We refer to this
method as Sparse-to-Dense Hypercolumn Matching. Because we know the 3D
locations of the sparse feature points in the reference images thanks to an
offline reconstruction stage, it is then possible to accurately estimate the
camera pose from these matches. Our experiments show that this method allows us
to outperform the state-of-the-art on several challenging outdoor datasets.