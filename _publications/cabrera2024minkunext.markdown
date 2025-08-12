---
layout: publication
title: 'Minkunext: Point Cloud-based Large-scale Place Recognition Using 3D Sparse
  Convolutions'
authors: "J. J. Cabrera, A. Santo, A. Gil, C. Viegas, L. Pay\xE1"
conference: Arxiv
year: 2024
bibkey: cabrera2024minkunext
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.07593'}]
tags: ["Scalability"]
short_authors: Cabrera et al.
---
This paper presents MinkUNeXt, an effective and efficient architecture for
place-recognition from point clouds entirely based on the new 3D MinkNeXt
Block, a residual block composed of 3D sparse convolutions that follows the
philosophy established by recent Transformers but purely using simple 3D
convolutions. Feature extraction is performed at different scales by a U-Net
encoder-decoder network and the feature aggregation of those features into a
single descriptor is carried out by a Generalized Mean Pooling (GeM). The
proposed architecture demonstrates that it is possible to surpass the current
state-of-the-art by only relying on conventional 3D sparse convolutions without
making use of more complex and sophisticated proposals such as Transformers,
Attention-Layers or Deformable Convolutions. A thorough assessment of the
proposal has been carried out using the Oxford RobotCar and the In-house
datasets. As a result, MinkUNeXt proves to outperform other methods in the
state-of-the-art.