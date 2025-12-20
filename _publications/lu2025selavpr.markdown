---
layout: publication
title: 'Selavpr++: Towards Seamless Adaptation Of Foundation Models For Efficient
  Place Recognition'
authors: Feng Lu, Tong Jin, Xiangyuan Lan, Lijun Zhang, Yunpeng Liu, Yaowei Wang,
  Chun Yuan
conference: Arxiv
year: 2025
bibkey: lu2025selavpr
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.16601'}]
tags: ["Datasets", "Efficiency", "Hashing Methods", "Memory Efficiency", "Re-Ranking"]
short_authors: Lu et al.
---
Recent studies show that the visual place recognition (VPR) method using
pre-trained visual foundation models can achieve promising performance. In our
previous work, we propose a novel method to realize seamless adaptation of
foundation models to VPR (SelaVPR). This method can produce both global and
local features that focus on discriminative landmarks to recognize places for
two-stage VPR by a parameter-efficient adaptation approach. Although SelaVPR
has achieved competitive results, we argue that the previous adaptation is
inefficient in training time and GPU memory usage, and the re-ranking paradigm
is also costly in retrieval latency and storage usage. In pursuit of higher
efficiency and better performance, we propose an extension of the SelaVPR,
called SelaVPR++. Concretely, we first design a parameter-, time-, and
memory-efficient adaptation method that uses lightweight multi-scale
convolution (MultiConv) adapters to refine intermediate features from the
frozen foundation backbone. This adaptation method does not back-propagate
gradients through the backbone during training, and the MultiConv adapter
facilitates feature interactions along the spatial axes and introduces proper
local priors, thus achieving higher efficiency and better performance.
Moreover, we propose an innovative re-ranking paradigm for more efficient VPR.
Instead of relying on local features for re-ranking, which incurs huge overhead
in latency and storage, we employ compact binary features for initial retrieval
and robust floating-point (global) features for re-ranking. To obtain such
binary features, we propose a similarity-constrained deep hashing method, which
can be easily integrated into the VPR pipeline. Finally, we improve our
training strategy and unify the training protocol of several common training
datasets to merge them for better training of VPR models. Extensive experiments
show that ......