---
layout: publication
title: 'Boq: A Place Is Worth A Bag Of Learnable Queries'
authors: "Ali-bey Amar, Chaib-draa Brahim, Gigu\xE8re Philippe"
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: alibey2024boq
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.07364'}]
tags: ["CVPR"]
---
In visual place recognition, accurately identifying and matching images of
locations under varying environmental conditions and viewpoints remains a
significant challenge. In this paper, we introduce a new technique, called
Bag-of-Queries (BoQ), which learns a set of global queries designed to capture
universal place-specific attributes. Unlike existing methods that employ
self-attention and generate the queries directly from the input features, BoQ
employs distinct learnable global queries, which probe the input features via
cross-attention, ensuring consistent information aggregation. In addition, our
technique provides an interpretable attention mechanism and integrates with
both CNN and Vision Transformer backbones. The performance of BoQ is
demonstrated through extensive experiments on 14 large-scale benchmarks. It
consistently outperforms current state-of-the-art techniques including NetVLAD,
MixVPR and EigenPlaces. Moreover, as a global retrieval technique (one-stage),
BoQ surpasses two-stage retrieval methods, such as Patch-NetVLAD, TransVPR and
R2Former, all while being orders of magnitude faster and more efficient. The
code and model weights are publicly available at
https://github.com/amaralibey/Bag-of-Queries.