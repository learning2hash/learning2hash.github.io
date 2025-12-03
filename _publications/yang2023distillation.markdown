---
layout: publication
title: Distillation Improves Visual Place Recognition For Low Quality Images
authors: Anbang Yang, Ge Jin, Junjie Huang, Yao Wang, John-Ross Rizzo, Chen Feng
conference: Arxiv
year: 2023
bibkey: yang2023distillation
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.06906'}]
tags: ["Datasets", "Distance Metric Learning", "Efficiency", "Evaluation", "Quantization"]
short_authors: Yang et al.
---
Real-time visual localization often utilizes online computing, for which
query images or videos are transmitted to remote servers for visual place
recognition (VPR). However, limited network bandwidth necessitates
image-quality reduction and thus the degradation of global image descriptors,
reducing VPR accuracy. We address this issue at the descriptor extraction level
with a knowledge-distillation methodology that learns feature representations
from high-quality images to extract more discriminative descriptors from
low-quality images. Our approach includes the Inter-channel Correlation
Knowledge Distillation (ICKD) loss, Mean Squared Error (MSE) loss, and Triplet
loss. We validate the proposed losses on multiple VPR methods and datasets
subjected to JPEG compression, resolution reduction, and video quantization. We
obtain significant improvements in VPR recall rates under all three tested
modalities of lowered image quality. Furthermore, we fill a gap in VPR
literature on video-based data and its influence on VPR performance. This work
contributes to more reliable place recognition in resource-constrained
environments.