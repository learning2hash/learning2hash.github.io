---
layout: publication
title: 'Dns: Distill-and-select For Efficient And Accurate Video Indexing And Retrieval'
authors: Giorgos Kordopatis-zilos, Christos Tzelepis, Symeon Papadopoulos, Ioannis
  Kompatsiaris, Ioannis Patras
conference: International Journal of Computer Vision
year: 2022
bibkey: kordopatiszilos2021dns
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.13266'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Hashing Methods", "Scalability", "Video Retrieval"]
short_authors: Kordopatis-zilos et al.
---
In this paper, we address the problem of high performance and computationally
efficient content-based video retrieval in large-scale datasets. Current
methods typically propose either: (i) fine-grained approaches employing
spatio-temporal representations and similarity calculations, achieving high
performance at a high computational cost or (ii) coarse-grained approaches
representing/indexing videos as global vectors, where the spatio-temporal
structure is lost, providing low performance but also having low computational
cost. In this work, we propose a Knowledge Distillation framework, called
Distill-and-Select (DnS), that starting from a well-performing fine-grained
Teacher Network learns: a) Student Networks at different retrieval performance
and computational efficiency trade-offs and b) a Selector Network that at test
time rapidly directs samples to the appropriate student to maintain both high
retrieval performance and high computational efficiency. We train several
students with different architectures and arrive at different trade-offs of
performance and efficiency, i.e., speed and storage requirements, including
fine-grained students that store/index videos using binary representations.
Importantly, the proposed scheme allows Knowledge Distillation in large,
unlabelled datasets -- this leads to good students. We evaluate DnS on five
public datasets on three different video retrieval tasks and demonstrate a)
that our students achieve state-of-the-art performance in several cases and b)
that the DnS framework provides an excellent trade-off between retrieval
performance, computational speed, and storage space. In specific
configurations, the proposed method achieves similar mAP with the teacher but
is 20 times faster and requires 240 times less storage space. The collected
dataset and implementation are publicly available:
https://github.com/mever-team/distill-and-select.