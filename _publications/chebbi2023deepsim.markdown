---
layout: publication
title: 'Deepsim-nets: Deep Similarity Networks For Stereo Image Matching'
authors: Mohamed Ali Chebbi, Ewelina Rupnik, Marc Pierrot-Deseilligny, Paul Lopes
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2023
bibkey: chebbi2023deepsim
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.08056'}]
tags: ["CVPR", "Datasets", "Distance Metric Learning", "Robustness"]
short_authors: Chebbi et al.
---
We present three multi-scale similarity learning architectures, or DeepSim
networks. These models learn pixel-level matching with a contrastive loss and
are agnostic to the geometry of the considered scene. We establish a middle
ground between hybrid and end-to-end approaches by learning to densely allocate
all corresponding pixels of an epipolar pair at once. Our features are learnt
on large image tiles to be expressive and capture the scene's wider context. We
also demonstrate that curated sample mining can enhance the overall robustness
of the predicted similarities and improve the performance on radiometrically
homogeneous areas. We run experiments on aerial and satellite datasets. Our
DeepSim-Nets outperform the baseline hybrid approaches and generalize better to
unseen scene geometries than end-to-end methods. Our flexible architecture can
be readily adopted in standard multi-resolution image matching pipelines.