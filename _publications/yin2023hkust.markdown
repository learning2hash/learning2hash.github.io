---
layout: publication
title: 'HKUST At Semeval-2023 Task 1: Visual Word Sense Disambiguation With Context
  Augmentation And Visual Assistance'
authors: Zhuohao Yin, Xin Huang
conference: Arxiv
year: 2023
bibkey: yin2023hkust
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.18273'}]
tags: []
short_authors: Zhuohao Yin, Xin Huang
---
Visual Word Sense Disambiguation (VWSD) is a multi-modal task that aims to
select, among a batch of candidate images, the one that best entails the target
word's meaning within a limited context. In this paper, we propose a
multi-modal retrieval framework that maximally leverages pretrained
Vision-Language models, as well as open knowledge bases and datasets. Our
system consists of the following key components: (1) Gloss matching: a
pretrained bi-encoder model is used to match contexts with proper senses of the
target words; (2) Prompting: matched glosses and other textual information,
such as synonyms, are incorporated using a prompting template; (3) Image
retrieval: semantically matching images are retrieved from large open datasets
using prompts as queries; (4) Modality fusion: contextual information from
different modalities are fused and used for prediction. Although our system
does not produce the most competitive results at SemEval-2023 Task 1, we are
still able to beat nearly half of the teams. More importantly, our experiments
reveal acute insights for the field of Word Sense Disambiguation (WSD) and
multi-modal learning. Our code is available on GitHub.