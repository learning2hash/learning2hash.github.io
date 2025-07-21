---
layout: publication
title: 'Mean Local Group Average Precision (mlgap): A New Performance Metric For Hashing-based
  Retrieval'
authors: Ding Pak Lun Kevin, Li Yikang, Li Baoxin
conference: Encyclopedia of Database Systems
year: 2018
bibkey: ding2018mean
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.09763'}]
tags: ["Hashing Methods", "Evaluation"]
---
The research on hashing techniques for visual data is gaining increased
attention in recent years due to the need for compact representations
supporting efficient search/retrieval in large-scale databases such as online
images. Among many possibilities, Mean Average Precision(mAP) has emerged as
the dominant performance metric for hashing-based retrieval. One glaring
shortcoming of mAP is its inability in balancing retrieval accuracy and
utilization of hash codes: pushing a system to attain higher mAP will
inevitably lead to poorer utilization of the hash codes. Poor utilization of
the hash codes hinders good retrieval because of increased collision of samples
in the hash space. This means that a model giving a higher mAP values does not
necessarily do a better job in retrieval. In this paper, we introduce a new
metric named Mean Local Group Average Precision (mLGAP) for better evaluation
of the performance of hashing-based retrieval. The new metric provides a
retrieval performance measure that also reconciles the utilization of hash
codes, leading to a more practically meaningful performance metric than
conventional ones like mAP. To this end, we start by mathematical analysis of
the deficiencies of mAP for hashing-based retrieval. We then propose mLGAP and
show why it is more appropriate for hashing-based retrieval. Experiments on
image retrieval are used to demonstrate the effectiveness of the proposed
metric.