---
layout: publication
title: Bags Of Affine Subspaces For Robust Object Tracking
authors: Sareh Shirazi, Conrad Sanderson, Chris Mccool, Mehrtash T. Harandi
conference: '2015 International Conference on Digital Image Computing: Techniques
  and Applications (DICTA)'
year: 2015
bibkey: shirazi2014bags
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1408.2313'}]
tags: ["Robustness"]
short_authors: Shirazi et al.
---
We propose an adaptive tracking algorithm where the object is modelled as a
continuously updated bag of affine subspaces, with each subspace constructed
from the object's appearance over several consecutive frames. In contrast to
linear subspaces, affine subspaces explicitly model the origin of subspaces.
Furthermore, instead of using a brittle point-to-subspace distance during the
search for the object in a new frame, we propose to use a subspace-to-subspace
distance by representing candidate image areas also as affine subspaces.
Distances between subspaces are then obtained by exploiting the non-Euclidean
geometry of Grassmann manifolds. Experiments on challenging videos (containing
object occlusions, deformations, as well as variations in pose and
illumination) indicate that the proposed method achieves higher tracking
accuracy than several recent discriminative trackers.