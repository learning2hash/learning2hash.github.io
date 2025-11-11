---
layout: publication
title: 3D Binary Signatures
authors: Siddharth Srivastava, Brejesh Lall
conference: Proceedings of the Tenth Indian Conference on Computer Vision, Graphics
  and Image Processing
year: 2016
bibkey: srivastava20163d
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.07937'}]
tags: ["Efficiency", "Evaluation"]
short_authors: Siddharth Srivastava, Brejesh Lall
---
In this paper, we propose a novel binary descriptor for 3D point clouds. The
proposed descriptor termed as 3D Binary Signature (3DBS) is motivated from the
matching efficiency of the binary descriptors for 2D images. 3DBS describes
keypoints from point clouds with a binary vector resulting in extremely fast
matching. The method uses keypoints from standard keypoint detectors. The
descriptor is built by constructing a Local Reference Frame and aligning a
local surface patch accordingly. The local surface patch constitutes of
identifying nearest neighbours based upon an angular constraint among them. The
points are ordered with respect to the distance from the keypoints. The normals
of the ordered pairs of these keypoints are projected on the axes and the
relative magnitude is used to assign a binary digit. The vector thus
constituted is used as a signature for representing the keypoints. The matching
is done by using hamming distance. We show that 3DBS outperforms state of the
art descriptors on various evaluation metrics.