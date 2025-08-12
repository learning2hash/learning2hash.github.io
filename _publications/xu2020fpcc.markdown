---
layout: publication
title: 'FPCC: Fast Point Cloud Clustering Based Instance Segmentation For Industrial
  Bin-picking'
authors: Yajun Xu, Shogo Arai, Diyi Liu, Fangzhou Lin, Kazuhiro Kosuge
conference: Neurocomputing
year: 2022
bibkey: xu2020fpcc
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.14618'}]
tags: []
short_authors: Xu et al.
---
Instance segmentation is an important pre-processing task in numerous
real-world applications, such as robotics, autonomous vehicles, and
human-computer interaction. Compared with the rapid development of deep
learning for two-dimensional (2D) image tasks, deep learning-based instance
segmentation of 3D point cloud still has a lot of room for development. In
particular, distinguishing a large number of occluded objects of the same class
is a highly challenging problem, which is seen in a robotic bin-picking. In a
usual bin-picking scene, many identical objects are stacked together and the
model of the objects is known. Thus, the semantic information can be ignored;
instead, the focus in the bin-picking is put on the segmentation of instances.
Based on this task requirement, we propose a Fast Point Cloud Clustering (FPCC)
for instance segmentation of bin-picking scene. FPCC includes a network named
FPCC-Net and a fast clustering algorithm. FPCC-net has two subnets, one for
inferring the geometric centers for clustering and the other for describing
features of each point. FPCC-Net extracts features of each point and infers
geometric center points of each instance simultaneously. After that, the
proposed clustering algorithm clusters the remaining points to the closest
geometric center in feature embedding space. Experiments show that FPCC also
surpasses the existing works in bin-picking scenes and is more computationally
efficient. Our code and data are available at https://github.com/xyjbaal/FPCC.