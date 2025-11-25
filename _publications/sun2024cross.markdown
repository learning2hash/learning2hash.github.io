---
layout: publication
title: Cross-modal Pre-aligned Method With Global And Local Information For Remote-sensing
  Image And Text Retrieval
authors: "Zengbao Sun, Ming Zhao, Gaorui Liu, Andr\xE9 Kaup"
conference: IEEE Transactions on Geoscience and Remote Sensing
year: 2024
bibkey: sun2024cross
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.14704'}]
tags: ["Datasets", "Efficiency", "Image Retrieval", "Re-Ranking"]
short_authors: Sun et al.
---
Remote sensing cross-modal text-image retrieval (RSCTIR) has gained attention
for its utility in information mining. However, challenges remain in
effectively integrating global and local information due to variations in
remote sensing imagery and ensuring proper feature pre-alignment before modal
fusion, which affects retrieval accuracy and efficiency. To address these
issues, we propose CMPAGL, a cross-modal pre-aligned method leveraging global
and local information. Our Gswin transformer block combines local window
self-attention and global-local window cross-attention to capture multi-scale
features. A pre-alignment mechanism simplifies modal fusion training, improving
retrieval performance. Additionally, we introduce a similarity matrix
reweighting (SMR) algorithm for reranking, and enhance the triplet loss
function with an intra-class distance term to optimize feature learning.
Experiments on four datasets, including RSICD and RSITMD, validate CMPAGL's
effectiveness, achieving up to 4.65% improvement in R@1 and 2.28% in mean
Recall (mR) over state-of-the-art methods.