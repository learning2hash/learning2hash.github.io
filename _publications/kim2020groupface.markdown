---
layout: publication
title: 'Groupface: Learning Latent Groups And Constructing Group-based Representations
  For Face Recognition'
authors: Yonghyun Kim, Wonpyo Park, Myung-Cheol Roh, Jongju Shin
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: kim2020groupface
citations: 92
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.10497'}]
tags: [CVPR, Datasets]
short_authors: Kim et al.
---
In the field of face recognition, a model learns to distinguish millions of
face images with fewer dimensional embedding features, and such vast
information may not be properly encoded in the conventional model with a single
branch. We propose a novel face-recognition-specialized architecture called
GroupFace that utilizes multiple group-aware representations, simultaneously,
to improve the quality of the embedding feature. The proposed method provides
self-distributed labels that balance the number of samples belonging to each
group without additional human annotations, and learns the group-aware
representations that can narrow down the search space of the target identity.
We prove the effectiveness of the proposed method by showing extensive ablation
studies and visualizations. All the components of the proposed method can be
trained in an end-to-end manner with a marginal increase of computational
complexity. Finally, the proposed method achieves the state-of-the-art results
with significant improvements in 1:1 face verification and 1:N face
identification tasks on the following public datasets: LFW, YTF, CALFW, CPLFW,
CFP, AgeDB-30, MegaFace, IJB-B and IJB-C.