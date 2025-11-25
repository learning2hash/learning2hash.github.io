---
layout: publication
title: 'Pre-training For Ad-hoc Retrieval: Hyperlink Is Also You Need'
authors: Zhengyi Ma, Zhicheng Dou, Wei Xu, Xinyu Zhang, Hao Jiang, Zhao Cao, Ji-Rong
  Wen
conference: Arxiv
year: 2021
bibkey: ma2021pre
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.09346'}]
tags: ["Datasets", "Evaluation", "Scalability", "Supervised", "Text Retrieval"]
short_authors: Ma et al.
---
Designing pre-training objectives that more closely resemble the downstream
tasks for pre-trained language models can lead to better performance at the
fine-tuning stage, especially in the ad-hoc retrieval area. Existing
pre-training approaches tailored for IR tried to incorporate weak supervised
signals, such as query-likelihood based sampling, to construct pseudo
query-document pairs from the raw textual corpus. However, these signals rely
heavily on the sampling method. For example, the query likelihood model may
lead to much noise in the constructed pre-training data. \blfootnote\{\(\dagger\)
This work was done during an internship at Huawei.\} In this paper, we propose
to leverage the large-scale hyperlinks and anchor texts to pre-train the
language model for ad-hoc retrieval. Since the anchor texts are created by
webmasters and can usually summarize the target document, it can help to build
more accurate and reliable pre-training samples than a specific algorithm.
Considering different views of the downstream ad-hoc retrieval, we devise four
pre-training tasks based on the hyperlinks. We then pre-train the Transformer
model to predict the pair-wise preference, jointly with the Masked Language
Model objective. Experimental results on two large-scale ad-hoc retrieval
datasets show the significant improvement of our model compared with the
existing methods.