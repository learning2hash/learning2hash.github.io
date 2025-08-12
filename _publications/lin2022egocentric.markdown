---
layout: publication
title: Egocentric Video-language Pretraining @ EPIC-KITCHENS-100 Multi-instance Retrieval
  Challenge 2022
authors: Kevin Qinghong Lin, Alex Jinpeng Wang, Rui Yan, Eric Zhongcong Xu, Rongcheng
  Tu, Yanru Zhu, Wenzhe Zhao, Weijie Kong, Chengfei Cai, Hongfa Wang, Wei Liu, Mike
  Zheng Shou
conference: Arxiv
year: 2022
bibkey: lin2022egocentric
citations: 1
additional_links: [{name: Code, url: 'https://github.com/showlab/EgoVLP'}, {name: Paper,
    url: 'https://arxiv.org/abs/2207.01334'}]
tags: ["Datasets", "Evaluation"]
short_authors: Lin et al.
---
In this report, we propose a video-language pretraining (VLP) based solution
\cite\{kevin2022egovlp\} for the EPIC-KITCHENS-100 Multi-Instance Retrieval (MIR)
challenge. Especially, we exploit the recently released Ego4D dataset
\cite\{grauman2021ego4d\} to pioneer Egocentric VLP from pretraining dataset,
pretraining objective, and development set. Based on the above three designs,
we develop a pretrained video-language model that is able to transfer its
egocentric video-text representation to MIR benchmark. Furthermore, we devise
an adaptive multi-instance max-margin loss to effectively fine-tune the model
and equip the dual-softmax technique for reliable inference. Our best single
model obtains strong performance on the challenge test set with 47.39% mAP and
61.44% nDCG. The code is available at https://github.com/showlab/EgoVLP.