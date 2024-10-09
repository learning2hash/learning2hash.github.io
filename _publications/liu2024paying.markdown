---
layout: publication
title: Paying More Attention To Image A Training-free Method For Alleviating Hallucination In Lvlms
authors: Shi Liu, Kecheng Zheng, Wei Chen
conference: "Arxiv"
year: 2024
bibkey: liu2024paying
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2407.21771v1"}
  - {name: "Code", url: "https://lalbj.github.io/projects/PAI/"}
tags: ['ARXIV', 'Cross Modal', 'Has Code']
---
Existing Large Vision-Language Models (LVLMs) primarily align image features of vision encoder with Large Language Models (LLMs) to leverage their superior text generation capabilities. However the scale disparity between vision encoder and language model may led to LLMs assuming a predominant role in multi-modal comprehension. This imbalance in LVLMs may result in the instances of hallucinatory. Concretely LVLMs may generate consistent descriptions with or without visual input indicating that certain outputs are influenced solely by context text. We refer to this phenomenon as text inertia. To counteract this issue we introduce a training-free algorithm to find an equilibrium point between image comprehension and language inference. Specifically we adaptively involve adjusting and amplifying the attention weights assigned to image tokens thereby granting greater prominence to visual elements. Meanwhile we subtract the logits of multi-modal inputs from ones of pure text input which can help LVLMs be not biased towards LLMs. By enhancing images tokens and reducing the stubborn output of LLM we can let LVLM pay more attention to images towards alleviating text inertia and reducing the hallucination in LVLMs. Our extensive experiments shows that this method substantially reduces the frequency of hallucinatory outputs in various LVLMs in terms of different metrics. Project page is available at https://lalbj.github.io/projects/PAI/.
