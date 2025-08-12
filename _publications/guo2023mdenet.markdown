---
layout: publication
title: 'Mdenet: Multi-modal Dual-embedding Networks For Malware Open-set Recognition'
authors: Jingcai Guo, Yuanyuan Xu, Wenchao Xu, Yufeng Zhan, Yuxia Sun, Song Guo
conference: Arxiv
year: 2023
bibkey: guo2023mdenet
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.01245'}]
tags: []
short_authors: Guo et al.
---
Malware open-set recognition (MOSR) aims at jointly classifying malware
samples from known families and detect the ones from novel unknown families,
respectively. Existing works mostly rely on a well-trained classifier
considering the predicted probabilities of each known family with a
threshold-based detection to achieve the MOSR. However, our observation reveals
that the feature distributions of malware samples are extremely similar to each
other even between known and unknown families. Thus the obtained classifier may
produce overly high probabilities of testing unknown samples toward known
families and degrade the model performance. In this paper, we propose the
Multi-modal Dual-Embedding Networks, dubbed MDENet, to take advantage of
comprehensive malware features (i.e., malware images and malware sentences)
from different modalities to enhance the diversity of malware feature space,
which is more representative and discriminative for down-stream recognition.
Last, to further guarantee the open-set recognition, we dually embed the fused
multi-modal representation into one primary space and an associated sub-space,
i.e., discriminative and exclusive spaces, with contrastive sampling and
rho-bounded enclosing sphere regularizations, which resort to classification
and detection, respectively. Moreover, we also enrich our previously proposed
large-scaled malware dataset MAL-100 with multi-modal characteristics and
contribute an improved version dubbed MAL-100+. Experimental results on the
widely used malware dataset Mailing and the proposed MAL-100+ demonstrate the
effectiveness of our method.