---
layout: publication
title: 'Learning By Aligning: Visible-infrared Person Re-identification Using Cross-modal
  Correspondences'
authors: Hyunjong Park, Sanghoon Lee, Junghyup Lee, Bumsub Ham
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: park2021learning
citations: 241
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.07422'}]
tags: ["ICCV", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Park et al.
---
We address the problem of visible-infrared person re-identification
(VI-reID), that is, retrieving a set of person images, captured by visible or
infrared cameras, in a cross-modal setting. Two main challenges in VI-reID are
intra-class variations across person images, and cross-modal discrepancies
between visible and infrared images. Assuming that the person images are
roughly aligned, previous approaches attempt to learn coarse image- or rigid
part-level person representations that are discriminative and generalizable
across different modalities. However, the person images, typically cropped by
off-the-shelf object detectors, are not necessarily well-aligned, which
distract discriminative person representation learning. In this paper, we
introduce a novel feature learning framework that addresses these problems in a
unified way. To this end, we propose to exploit dense correspondences between
cross-modal person images. This allows to address the cross-modal discrepancies
in a pixel-level, suppressing modality-related features from person
representations more effectively. This also encourages pixel-wise associations
between cross-modal local features, further facilitating discriminative feature
learning for VI-reID. Extensive experiments and analyses on standard VI-reID
benchmarks demonstrate the effectiveness of our approach, which significantly
outperforms the state of the art.