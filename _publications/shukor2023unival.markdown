---
layout: publication
title: Unival Unified Model For Image Video Audio And Language Tasks
authors: Mustafa Shukor, Corentin Dancette, Alexandre Rame, Matthieu Cord
conference: "Arxiv"
year: 2023
bibkey: shukor2023unival
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2307.16184v2"}
  - {name: "Code", url: "https://github.com/mshukor/UnIVAL"}
tags: ['ARXIV', 'Cross Modal', 'Has Code']
---
Large Language Models (LLMs) have made the ambitious quest for generalist agents significantly far from being a fantasy. A key hurdle for building such general models is the diversity and heterogeneity of tasks and modalities. A promising solution is unification allowing the support of a myriad of tasks and modalities within one unified framework. While few large models (e.g. Flamingo (Alayrac et al. 2022) trained on massive datasets can support more than two modalities current small to mid-scale unified models are still limited to 2 modalities usually image-text or video-text. The question that we ask is is it possible to build efficiently a unified model that can support all modalities To answer this we propose UnIVAL a step further towards this ambitious goal. Without relying on fancy datasets sizes or models with billions of parameters the ~ 0.25B parameter UnIVAL model goes beyond two modalities and unifies text images video and audio into a single model. Our model is efficiently pretrained on many tasks based on task balancing and multimodal curriculum learning. UnIVAL shows competitive performance to existing state-of-the-art approaches across image and video-text tasks. The feature representations learned from image and video-text modalities allows the model to achieve competitive performance when finetuned on audio-text tasks despite not being pretrained on audio. Thanks to the unified model we propose a novel study on multimodal model merging via weight interpolation of models trained on different multimodal tasks showing their benefits in particular for out-of-distribution generalization. Finally we motivate unification by showing the synergy between tasks. The model weights and code are released here https://github.com/mshukor/UnIVAL.
