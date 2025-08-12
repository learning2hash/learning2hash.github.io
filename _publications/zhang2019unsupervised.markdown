---
layout: publication
title: Unsupervised Part Mining For Fine-grained Image Classification
authors: Runsheng Zhang, Jian Zhang, Yaping Huang, Qi Zou
conference: Arxiv
year: 2019
bibkey: zhang2019unsupervised
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.09941'}]
tags: ["Unsupervised"]
short_authors: Zhang et al.
---
Fine-grained image classification remains challenging due to the large
intra-class variance and small inter-class variance. Since the subtle visual
differences are only in local regions of discriminative parts among
subcategories, part localization is a key issue for fine-grained image
classification. Most existing approaches localize object or parts in an image
with object or part annotations, which are expensive and labor-consuming. To
tackle this issue, we propose a fully unsupervised part mining (UPM) approach
to localize the discriminative parts without even image-level annotations,
which largely improves the fine-grained classification performance. We first
utilize pattern mining techniques to discover frequent patterns, i.e.,
co-occurrence highlighted regions, in the feature maps extracted from a
pre-trained convolutional neural network (CNN) model. Inspired by the fact that
these relevant meaningful patterns typically hold appearance and spatial
consistency, we then cluster the mined regions to obtain the cluster centers
and the discriminative parts surrounding the cluster centers are generated.
Importantly, any annotations and sophisticated training procedures are not used
in our proposed part localization approach. Finally, a multi-stream
classification network is built for aggregating the original, object-level and
part-level features simultaneously. Compared with other state-of-the-art
approaches, our UPM approach achieves the competitive performance.