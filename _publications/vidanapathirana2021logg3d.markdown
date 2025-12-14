---
layout: publication
title: 'Logg3d-net: Locally Guided Global Descriptor Learning For 3D Place Recognition'
authors: Kavisha Vidanapathirana, Milad Ramezani, Peyman Moghadam, Sridha Sridharan,
  Clinton Fookes
conference: Arxiv
year: 2021
bibkey: vidanapathirana2021logg3d
citations: 0
additional_links: [{name: Code, url: 'https://github.com/csiro-robotics/LoGG3D-Net'},
  {name: Paper, url: 'https://arxiv.org/abs/2109.08336'}]
tags: [Scalability, Evaluation, Efficiency]
short_authors: Vidanapathirana et al.
---
Retrieval-based place recognition is an efficient and effective solution for
re-localization within a pre-built map, or global data association for
Simultaneous Localization and Mapping (SLAM). The accuracy of such an approach
is heavily dependent on the quality of the extracted scene-level
representation. While end-to-end solutions - which learn a global descriptor
from input point clouds - have demonstrated promising results, such approaches
are limited in their ability to enforce desirable properties at the local
feature level. In this paper, we introduce a local consistency loss to guide
the network towards learning local features which are consistent across
revisits, hence leading to more repeatable global descriptors resulting in an
overall improvement in 3D place recognition performance. We formulate our
approach in an end-to-end trainable architecture called LoGG3D-Net. Experiments
on two large-scale public benchmarks (KITTI and MulRan) show that our method
achieves mean \(F1_\{max\}\) scores of \(0.939\) and \(0.968\) on KITTI and MulRan
respectively, achieving state-of-the-art performance while operating in near
real-time. The open-source implementation is available at:
https://github.com/csiro-robotics/LoGG3D-Net.