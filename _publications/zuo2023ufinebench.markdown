---
layout: publication
title: 'Ufinebench: Towards Text-based Person Retrieval With Ultra-fine Granularity'
authors: Jialong Zuo, Hanyu Zhou, Ying Nie, Feng Zhang, Tianyu Guo, Nong Sang, Yunhe
  Wang, Changxin Gao
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: zuo2023ufinebench
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.03441'}]
tags: ["CVPR"]
short_authors: Zuo et al.
---
Existing text-based person retrieval datasets often have relatively
coarse-grained text annotations. This hinders the model to comprehend the
fine-grained semantics of query texts in real scenarios. To address this
problem, we contribute a new benchmark named \textbf\{UFineBench\} for text-based
person retrieval with ultra-fine granularity.
  Firstly, we construct a new \textbf\{dataset\} named UFine6926. We collect a
large number of person images and manually annotate each image with two
detailed textual descriptions, averaging 80.8 words each. The average word
count is three to four times that of the previous datasets. In addition of
standard in-domain evaluation, we also propose a special \textbf\{evaluation
paradigm\} more representative of real scenarios. It contains a new evaluation
set with cross domains, cross textual granularity and cross textual styles,
named UFine3C, and a new evaluation metric for accurately measuring retrieval
ability, named mean Similarity Distribution (mSD). Moreover, we propose CFAM, a
more efficient \textbf\{algorithm\} especially designed for text-based person
retrieval with ultra fine-grained texts. It achieves fine granularity mining by
adopting a shared cross-modal granularity decoder and hard negative match
mechanism.
  With standard in-domain evaluation, CFAM establishes competitive performance
across various datasets, especially on our ultra fine-grained UFine6926.
Furthermore, by evaluating on UFine3C, we demonstrate that training on our
UFine6926 significantly improves generalization to real scenarios compared with
other coarse-grained datasets. The dataset and code will be made publicly
available at https://github.com/Zplusdragon/UFineBench.