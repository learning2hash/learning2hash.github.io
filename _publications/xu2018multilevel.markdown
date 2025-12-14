---
layout: publication
title: Multilevel Language And Vision Integration For Text-to-clip Retrieval
authors: Huijuan Xu, Kun He, Bryan A. Plummer, Leonid Sigal, Stan Sclaroff, Kate Saenko
conference: Arxiv
year: 2018
bibkey: xu2018multilevel
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.05113'}]
tags: [Distance Metric Learning, Evaluation]
short_authors: Xu et al.
---
We address the problem of text-based activity retrieval in video. Given a
sentence describing an activity, our task is to retrieve matching clips from an
untrimmed video. To capture the inherent structures present in both text and
video, we introduce a multilevel model that integrates vision and language
features earlier and more tightly than prior work. First, we inject text
features early on when generating clip proposals, to help eliminate unlikely
clips and thus speed up processing and boost performance. Second, to learn a
fine-grained similarity metric for retrieval, we use visual features to
modulate the processing of query sentences at the word level in a recurrent
neural network. A multi-task loss is also employed by adding query
re-generation as an auxiliary task. Our approach significantly outperforms
prior work on two challenging benchmarks: Charades-STA and ActivityNet
Captions.