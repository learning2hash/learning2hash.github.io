---
layout: publication
title: 'Compress: Self-supervised Learning By Compressing Representations'
authors: Soroush Abbasi Koohpayegani, Ajinkya Tejankar, Hamed Pirsiavash
conference: Arxiv
year: 2020
bibkey: koohpayegani2020compress
citations: 33
additional_links: [{name: Code, url: 'https://github.com/UMBCvision/CompRess'}, {
    name: Paper, url: 'https://arxiv.org/abs/2010.14713'}]
tags: [Self-Supervised, Supervised, Evaluation]
short_authors: Soroush Abbasi Koohpayegani, Ajinkya Tejankar, Hamed Pirsiavash
---
Self-supervised learning aims to learn good representations with unlabeled
data. Recent works have shown that larger models benefit more from
self-supervised learning than smaller models. As a result, the gap between
supervised and self-supervised learning has been greatly reduced for larger
models. In this work, instead of designing a new pseudo task for
self-supervised learning, we develop a model compression method to compress an
already learned, deep self-supervised model (teacher) to a smaller one
(student). We train the student model so that it mimics the relative similarity
between the data points in the teacher's embedding space. For AlexNet, our
method outperforms all previous methods including the fully supervised model on
ImageNet linear evaluation (59.0% compared to 56.5%) and on nearest neighbor
evaluation (50.7% compared to 41.4%). To the best of our knowledge, this is the
first time a self-supervised AlexNet has outperformed supervised one on
ImageNet classification. Our code is available here:
https://github.com/UMBCvision/CompRess