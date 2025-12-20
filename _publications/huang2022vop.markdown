---
layout: publication
title: 'Vop: Text-video Co-operative Prompt Tuning For Cross-modal Retrieval'
authors: Siteng Huang, Biao Gong, Yulin Pan, Jianwen Jiang, Yiliang Lv, Yuyuan Li,
  Donglin Wang
conference: Arxiv
year: 2022
bibkey: huang2022vop
citations: 3
additional_links: [{name: Code, url: 'https://github.com/bighuang624/VoP'}, {name: Paper,
    url: 'https://arxiv.org/abs/2211.12764'}]
tags: ["Evaluation", "Multimodal Retrieval", "Tools & Libraries", "Video Retrieval"]
short_authors: Huang et al.
---
Many recent studies leverage the pre-trained CLIP for text-video cross-modal
retrieval by tuning the backbone with additional heavy modules, which not only
brings huge computational burdens with much more parameters, but also leads to
the knowledge forgetting from upstream models. In this work, we propose the
VoP: Text-Video Co-operative Prompt Tuning for efficient tuning on the
text-video retrieval task. The proposed VoP is an end-to-end framework with
both video & text prompts introducing, which can be regarded as a powerful
baseline with only 0.1% trainable parameters. Further, based on the
spatio-temporal characteristics of videos, we develop three novel video prompt
mechanisms to improve the performance with different scales of trainable
parameters. The basic idea of the VoP enhancement is to model the frame
position, frame context, and layer function with specific trainable prompts,
respectively. Extensive experiments show that compared to full fine-tuning, the
enhanced VoP achieves a 1.4% average R@1 gain across five text-video retrieval
benchmarks with 6x less parameter overhead. The code will be available at
https://github.com/bighuang624/VoP.