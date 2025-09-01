---
layout: publication
title: Semi-heterogeneous Three-way Joint Embedding Network For Sketch-based Image
  Retrieval
authors: Jianjun Lei, Yuxin Song, Bo Peng, Zhanyu Ma, Ling Shao, Yi-Zhe Song
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2019
bibkey: lei2019semi
citations: 52
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.04470'}]
tags: ["Datasets", "Distance Metric Learning", "Image Retrieval"]
short_authors: Lei et al.
---
Sketch-based image retrieval (SBIR) is a challenging task due to the large
cross-domain gap between sketches and natural images. How to align abstract
sketches and natural images into a common high-level semantic space remains a
key problem in SBIR. In this paper, we propose a novel semi-heterogeneous
three-way joint embedding network (Semi3-Net), which integrates three branches
(a sketch branch, a natural image branch, and an edgemap branch) to learn more
discriminative cross-domain feature representations for the SBIR task. The key
insight lies with how we cultivate the mutual and subtle relationships amongst
the sketches, natural images, and edgemaps. A semi-heterogeneous feature
mapping is designed to extract bottom features from each domain, where the
sketch and edgemap branches are shared while the natural image branch is
heterogeneous to the other branches. In addition, a joint semantic embedding is
introduced to embed the features from different domains into a common
high-level semantic space, where all of the three branches are shared. To
further capture informative features common to both natural images and the
corresponding edgemaps, a co-attention model is introduced to conduct common
channel-wise feature recalibration between different domains. A hybrid-loss
mechanism is designed to align the three branches, where an alignment loss and
a sketch-edgemap contrastive loss are presented to encourage the network to
learn invariant cross-domain representations. Experimental results on two
widely used category-level datasets (Sketchy and TU-Berlin Extension)
demonstrate that the proposed method outperforms state-of-the-art methods.