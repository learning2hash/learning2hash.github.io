---
layout: publication
title: Enhancing Deformable Local Features By Jointly Learning To Detect And Describe
  Keypoints
authors: Guilherme Potje, Felipe Cadar, Andre Araujo, Renato Martins, Erickson R.
  Nascimento
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: potje2023enhancing
citations: 13
additional_links: [{name: Code, url: 'https://verlab.dcc.ufmg.br/descriptors/dalf_cvpr23'},
  {name: Paper, url: 'https://arxiv.org/abs/2304.00583'}]
tags: [Evaluation, CVPR]
short_authors: Potje et al.
---
Local feature extraction is a standard approach in computer vision for
tackling important tasks such as image matching and retrieval. The core
assumption of most methods is that images undergo affine transformations,
disregarding more complicated effects such as non-rigid deformations.
Furthermore, incipient works tailored for non-rigid correspondence still rely
on keypoint detectors designed for rigid transformations, hindering performance
due to the limitations of the detector. We propose DALF (Deformation-Aware
Local Features), a novel deformation-aware network for jointly detecting and
describing keypoints, to handle the challenging problem of matching deformable
surfaces. All network components work cooperatively through a feature fusion
approach that enforces the descriptors' distinctiveness and invariance.
Experiments using real deforming objects showcase the superiority of our
method, where it delivers 8% improvement in matching scores compared to the
previous best results. Our approach also enhances the performance of two
real-world applications: deformable object retrieval and non-rigid 3D surface
registration. Code for training, inference, and applications are publicly
available at https://verlab.dcc.ufmg.br/descriptors/dalf_cvpr23.