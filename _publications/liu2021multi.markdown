---
layout: publication
title: Multi-stage Pre-training Over Simplified Multimodal Pre-training Models
authors: Tongtong Liu, Fangxiang Feng, Xiaojie Wang
conference: 'Proceedings of the 59th Annual Meeting of the Association for Computational
  Linguistics and the 11th International Joint Conference on Natural Language Processing
  (Volume 1: Long Papers)'
year: 2021
bibkey: liu2021multi
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.14596'}]
tags: [Text Retrieval, Evaluation, Datasets, ACL]
short_authors: Tongtong Liu, Fangxiang Feng, Xiaojie Wang
---
Multimodal pre-training models, such as LXMERT, have achieved excellent
results in downstream tasks. However, current pre-trained models require large
amounts of training data and have huge model sizes, which make them difficult
to apply in low-resource situations. How to obtain similar or even better
performance than a larger model under the premise of less pre-training data and
smaller model size has become an important problem. In this paper, we propose a
new Multi-stage Pre-training (MSP) method, which uses information at different
granularities from word, phrase to sentence in both texts and images to
pre-train the model in stages. We also design several different pre-training
tasks suitable for the information granularity in different stage in order to
efficiently capture the diverse knowledge from a limited corpus. We take a
Simplified LXMERT (LXMERT- S), which has only 45.9% parameters of the original
LXMERT model and 11.76% of the original pre-training data as the testbed of our
MSP method. Experimental results show that our method achieves comparable
performance to the original LXMERT model in all downstream tasks, and even
outperforms the original model in Image-Text Retrieval task.