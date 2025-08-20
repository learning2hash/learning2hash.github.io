---
layout: publication
title: On The Evolution Of (hateful) Memes By Means Of Multimodal Contrastive Learning
authors: Yiting Qu, Xinlei He, Shannon Pierson, Michael Backes, Yang Zhang, Savvas
  Zannettou
conference: 2023 IEEE Symposium on Security and Privacy (SP)
year: 2023
bibkey: qu2023evolution
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.06573'}]
tags: [Tools & Libraries, Datasets]
short_authors: Qu et al.
---
The dissemination of hateful memes online has adverse effects on social media
platforms and the real world. Detecting hateful memes is challenging, one of
the reasons being the evolutionary nature of memes; new hateful memes can
emerge by fusing hateful connotations with other cultural ideas or symbols. In
this paper, we propose a framework that leverages multimodal contrastive
learning models, in particular OpenAI's CLIP, to identify targets of hateful
content and systematically investigate the evolution of hateful memes. We find
that semantic regularities exist in CLIP-generated embeddings that describe
semantic relationships within the same modality (images) or across modalities
(images and text). Leveraging this property, we study how hateful memes are
created by combining visual elements from multiple images or fusing textual
information with a hateful image. We demonstrate the capabilities of our
framework for analyzing the evolution of hateful memes by focusing on
antisemitic memes, particularly the Happy Merchant meme. Using our framework on
a dataset extracted from 4chan, we find 3.3K variants of the Happy Merchant
meme, with some linked to specific countries, persons, or organizations. We
envision that our framework can be used to aid human moderators by flagging new
variants of hateful memes so that moderators can manually verify them and
mitigate the problem of hateful content online.