---
layout: publication
title: 'Webly Supervised Image Classification With Metadata: Automatic Noisy Label
  Correction Via Visual-semantic Graph'
authors: Jingkang Yang, Weirong Chen, Litong Feng, Xiaopeng Yan, Huabin Zheng, Wayne
  Zhang
conference: Proceedings of the 28th ACM International Conference on Multimedia
year: 2020
bibkey: yang2020webly
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.05864'}]
tags: ["Datasets", "Supervised"]
short_authors: Yang et al.
---
Webly supervised learning becomes attractive recently for its efficiency in
data expansion without expensive human labeling. However, adopting search
queries or hashtags as web labels of images for training brings massive noise
that degrades the performance of DNNs. Especially, due to the semantic
confusion of query words, the images retrieved by one query may contain
tremendous images belonging to other concepts. For example, searching `tiger
cat' on Flickr will return a dominating number of tiger images rather than the
cat images. These realistic noisy samples usually have clear visual semantic
clusters in the visual space that mislead DNNs from learning accurate semantic
labels. To correct real-world noisy labels, expensive human annotations seem
indispensable. Fortunately, we find that metadata can provide extra knowledge
to discover clean web labels in a labor-free fashion, making it feasible to
automatically provide correct semantic guidance among the massive label-noisy
web data. In this paper, we propose an automatic label corrector VSGraph-LC
based on the visual-semantic graph. VSGraph-LC starts from anchor selection
referring to the semantic similarity between metadata and correct label
concepts, and then propagates correct labels from anchors on a visual graph
using graph neural network (GNN). Experiments on realistic webly supervised
learning datasets Webvision-1000 and NUS-81-Web show the effectiveness and
robustness of VSGraph-LC. Moreover, VSGraph-LC reveals its advantage on the
open-set validation set.