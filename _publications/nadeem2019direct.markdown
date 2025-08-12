---
layout: publication
title: Direct Image To Point Cloud Descriptors Matching For 6-DOF Camera Localization
  In Dense 3D Point Cloud
authors: Uzair Nadeem, Mohammad A. A. K. Jalwana, Mohammed Bennamoun, Roberto Togneri,
  Ferdous Sohel
conference: Lecture Notes in Computer Science
year: 2019
bibkey: nadeem2019direct
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.06064'}]
tags: []
short_authors: Nadeem et al.
---
We propose a novel concept to directly match feature descriptors extracted
from RGB images, with feature descriptors extracted from 3D point clouds. We
use this concept to localize the position and orientation (pose) of the camera
of a query image in dense point clouds. We generate a dataset of matching 2D
and 3D descriptors, and use it to train a proposed Descriptor-Matcher
algorithm. To localize a query image in a point cloud, we extract 2D keypoints
and descriptors from the query image. Then the Descriptor-Matcher is used to
find the corresponding pairs 2D and 3D keypoints by matching the 2D descriptors
with the pre-extracted 3D descriptors of the point cloud. This information is
used in a robust pose estimation algorithm to localize the query image in the
3D point cloud. Experiments demonstrate that directly matching 2D and 3D
descriptors is not only a viable idea but also achieves competitive accuracy
compared to other state-of-the-art approaches for camera pose localization.