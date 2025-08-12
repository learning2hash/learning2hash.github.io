---
layout: publication
title: 'Beyond Triplet Loss: Meta Prototypical N-tuple Loss For Person Re-identification'
authors: Zhizheng Zhang, Cuiling Lan, Wenjun Zeng, Zhibo Chen, Shih-fu Chang
conference: IEEE Transactions on Multimedia
year: 2021
bibkey: zhang2020beyond
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.04991'}]
tags: ["Distance Metric Learning"]
short_authors: Zhang et al.
---
Person Re-identification (ReID) aims at matching a person of interest across
images. In convolutional neural network (CNN) based approaches, loss design
plays a vital role in pulling closer features of the same identity and pushing
far apart features of different identities. In recent years, triplet loss
achieves superior performance and is predominant in ReID. However, triplet loss
considers only three instances of two classes in per-query optimization (with
an anchor sample as query) and it is actually equivalent to a two-class
classification. There is a lack of loss design which enables the joint
optimization of multiple instances (of multiple classes) within per-query
optimization for person ReID. In this paper, we introduce a multi-class
classification loss, i.e., N-tuple loss, to jointly consider multiple (N)
instances for per-query optimization. This in fact aligns better with the ReID
test/inference process, which conducts the ranking/comparisons among multiple
instances. Furthermore, for more efficient multi-class classification, we
propose a new meta prototypical N-tuple loss. With the multi-class
classification incorporated, our model achieves the state-of-the-art
performance on the benchmark person ReID datasets.