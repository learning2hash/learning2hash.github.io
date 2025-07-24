---
layout: publication
title: Keypoint-aligned Embeddings For Image Retrieval And Re-identification
authors: Olga Moskvyak, Frederic Maire, Feras Dayoub, Mahsa Baktashmotlagh
conference: 2021 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2021
bibkey: moskvyak2020keypoint
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.11368'}]
tags: ["Datasets", "Evaluation", "Image Retrieval"]
short_authors: Moskvyak et al.
---
Learning embeddings that are invariant to the pose of the object is crucial
in visual image retrieval and re-identification. The existing approaches for
person, vehicle, or animal re-identification tasks suffer from high intra-class
variance due to deformable shapes and different camera viewpoints. To overcome
this limitation, we propose to align the image embedding with a predefined
order of the keypoints. The proposed keypoint aligned embeddings model
(KAE-Net) learns part-level features via multi-task learning which is guided by
keypoint locations. More specifically, KAE-Net extracts channels from a feature
map activated by a specific keypoint through learning the auxiliary task of
heatmap reconstruction for this keypoint. The KAE-Net is compact, generic and
conceptually simple. It achieves state of the art performance on the benchmark
datasets of CUB-200-2011, Cars196 and VeRi-776 for retrieval and
re-identification tasks.