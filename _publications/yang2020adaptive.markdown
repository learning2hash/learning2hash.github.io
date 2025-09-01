---
layout: publication
title: Adaptive Deep Metric Embeddings For Person Re-identification Under Occlusions
authors: Wanxiang Yang, Yan Yan, Si Chen
conference: Neurocomputing
year: 2019
bibkey: yang2020adaptive
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.02603'}]
tags: ["Datasets", "Evaluation"]
short_authors: Wanxiang Yang, Yan Yan, Si Chen
---
Person re-identification (ReID) under occlusions is a challenging problem in
video surveillance. Most of existing person ReID methods take advantage of
local features to deal with occlusions. However, these methods usually
independently extract features from the local regions of an image without
considering the relationship among different local regions. In this paper, we
propose a novel person ReID method, which learns the spatial dependencies
between the local regions and extracts the discriminative feature
representation of the pedestrian image based on Long Short-Term Memory (LSTM),
dealing with the problem of occlusions. In particular, we propose a novel loss
(termed the adaptive nearest neighbor loss) based on the classification
uncertainty to effectively reduce intra-class variations while enlarging
inter-class differences within the adaptive neighborhood of the sample. The
proposed loss enables the deep neural network to adaptively learn
discriminative metric embeddings, which significantly improve the
generalization capability of recognizing unseen person identities. Extensive
comparative evaluations on challenging person ReID datasets demonstrate the
significantly improved performance of the proposed method compared with several
state-of-the-art methods.