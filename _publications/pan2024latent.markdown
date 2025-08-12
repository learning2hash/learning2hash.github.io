---
layout: publication
title: Latent Fingerprint Matching Via Dense Minutia Descriptor
authors: Zhiyu Pan, Yongjie Duan, Xiongjun Guan, Jianjiang Feng, Jie Zhou
conference: Arxiv
year: 2024
bibkey: pan2024latent
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.01199'}]
tags: []
short_authors: Pan et al.
---
Latent fingerprint matching is a daunting task, primarily due to the poor
quality of latent fingerprints. In this study, we propose a deep-learning based
dense minutia descriptor (DMD) for latent fingerprint matching. A DMD is
obtained by extracting the fingerprint patch aligned by its central minutia,
capturing detailed minutia information and texture information. Our dense
descriptor takes the form of a three-dimensional representation, with two
dimensions associated with the original image plane and the other dimension
representing the abstract features. Additionally, the extraction process
outputs the fingerprint segmentation map, ensuring that the descriptor is only
valid in the foreground region. The matching between two descriptors occurs in
their overlapping regions, with a score normalization strategy to reduce the
impact brought by the differences outside the valid area. Our descriptor
achieves state-of-the-art performance on several latent fingerprint datasets.
Overall, our DMD is more representative and interpretable compared to previous
methods.