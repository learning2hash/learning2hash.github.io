---
layout: publication
title: 'Mumur : Multilingual Multimodal Universal Retrieval'
authors: Avinash Madasu, Estelle Aflalo, Gabriela Ben Melech Stan, Shachar Rosenman,
  Shao-yen Tseng, Gedas Bertasius, Vasudev Lal
conference: Information Retrieval Journal
year: 2023
bibkey: madasu2022mumur
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.11553'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Video Retrieval"]
short_authors: Madasu et al.
---
Multi-modal retrieval has seen tremendous progress with the development of
vision-language models. However, further improving these models require
additional labelled data which is a huge manual effort. In this paper, we
propose a framework MuMUR, that utilizes knowledge transfer from a multilingual
model to boost the performance of multi-modal (image and video) retrieval. We
first use state-of-the-art machine translation models to construct pseudo
ground-truth multilingual visual-text pairs. We then use this data to learn a
joint vision-text representation where English and non-English text queries are
represented in a common embedding space based on pretrained multilingual
models. We evaluate our proposed approach on a diverse set of retrieval
datasets: five video retrieval datasets such as MSRVTT, MSVD, DiDeMo, Charades
and MSRVTT multilingual, two image retrieval datasets such as Flickr30k and
Multi30k . Experimental results demonstrate that our approach achieves
state-of-the-art results on all video retrieval datasets outperforming previous
models. Additionally, our framework MuMUR significantly beats other
multilingual video retrieval dataset. We also observe that MuMUR exhibits
strong performance on image retrieval. This demonstrates the universal ability
of MuMUR to perform retrieval across all visual inputs (image and video) and
text inputs (monolingual and multilingual).