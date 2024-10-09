---
layout: publication
title: Idealgpt Iteratively Decomposing Vision And Language Reasoning Via Large Language Models
authors: Haoxuan You, Rui Sun, Zhecan Wang, Long Chen, Gengyu Wang, Hammad A. Ayyubi, Kai-wei Chang, Shih-fu Chang
conference: "Arxiv"
year: 2023
bibkey: you2023idealgpt
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2305.14985v1"}
  - {name: "Code", url: "https://github.com/Hxyou/IdealGPT"}
tags: ['ARXIV', 'Has Code']
---
The field of vision-and-language (VL) understanding has made unprecedented progress with end-to-end large pre-trained VL models (VLMs). However they still fall short in zero-shot reasoning tasks that require multi-step inferencing. To achieve this goal previous works resort to a divide-and-conquer pipeline. In this paper we argue that previous efforts have several inherent shortcomings 1) They rely on domain-specific sub-question decomposing models. 2) They force models to predict the final answer even if the sub-questions or sub-answers provide insufficient information. We address these limitations via IdealGPT a framework that iteratively decomposes VL reasoning using large language models (LLMs). Specifically IdealGPT utilizes an LLM to generate sub-questions a VLM to provide corresponding sub-answers and another LLM to reason to achieve the final answer. These three modules perform the divide-and-conquer procedure iteratively until the model is confident about the final answer to the main question. We evaluate IdealGPT on multiple challenging VL reasoning tasks under a zero-shot setting. In particular our IdealGPT outperforms the best existing GPT-4-like models by an absolute 1037; on VCR and 1537; on SNLI-VE. Code is available at https://github.com/Hxyou/IdealGPT
