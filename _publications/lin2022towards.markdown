---
layout: publication
title: Towards Fast Adaptation Of Pretrained Contrastive Models For Multi-channel
  Video-language Retrieval
authors: Xudong Lin, Simran Tiwari, Shiyuan Huang, Manling Li, Mike Zheng Shou, Heng
  Ji, Shih-Fu Chang
conference: Arxiv
year: 2022
bibkey: lin2022towards
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.02082'}]
tags: [Evaluation, Datasets]
short_authors: Lin et al.
---
Multi-channel video-language retrieval require models to understand
information from different channels (e.g. video\(+\)question, video\(+\)speech) to
correctly link a video with a textual response or query. Fortunately,
contrastive multimodal models are shown to be highly effective at aligning
entities in images/videos and text, e.g., CLIP; text contrastive models are
extensively studied recently for their strong ability of producing
discriminative sentence embeddings, e.g., SimCSE. However, there is not a clear
way to quickly adapt these two lines to multi-channel video-language retrieval
with limited data and resources. In this paper, we identify a principled model
design space with two axes: how to represent videos and how to fuse video and
text information. Based on categorization of recent methods, we investigate the
options of representing videos using continuous feature vectors or discrete
text tokens; for the fusion method, we explore the use of a multimodal
transformer or a pretrained contrastive text model. We extensively evaluate the
four combinations on five video-language datasets. We surprisingly find that
discrete text tokens coupled with a pretrained contrastive text model yields
the best performance, which can even outperform state-of-the-art on the iVQA
and How2QA datasets without additional training on millions of video-text data.
Further analysis shows that this is because representing videos as text tokens
captures the key visual information and text tokens are naturally aligned with
text models that are strong retrievers after the contrastive pretraining
process. All the empirical analysis establishes a solid foundation for future
research on affordable and upgradable multimodal intelligence.