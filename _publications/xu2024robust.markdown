---
layout: publication
title: Robust Multi-bit Text Watermark With Llm-based Paraphrasers
authors: Xiaojun Xu, Jinghan Jia, Yuanshun Yao, Yang Liu, Hang Li
conference: Arxiv
year: 2024
bibkey: xu2024robust
citations: 0
additional_links: [{name: Code, url: 'https://github.com/xiaojunxu/multi-bit-text-watermark'},
  {name: Paper, url: 'https://arxiv.org/abs/2412.03123'}]
tags: ["Evaluation"]
short_authors: Xu et al.
---
We propose an imperceptible multi-bit text watermark embedded by paraphrasing with LLMs. We fine-tune a pair of LLM paraphrasers that are designed to behave differently so that their paraphrasing difference reflected in the text semantics can be identified by a trained decoder. To embed our multi-bit watermark, we use two paraphrasers alternatively to encode the pre-defined binary code at the sentence level. Then we use a text classifier as the decoder to decode each bit of the watermark. Through extensive experiments, we show that our watermarks can achieve over 99.99% detection AUC with small (1.1B) text paraphrasers while keeping the semantic information of the original sentence. More importantly, our pipeline is robust under word substitution and sentence paraphrasing perturbations and generalizes well to out-of-distributional data. We also show the stealthiness of our watermark with LLM-based evaluation. We open-source the code: https://github.com/xiaojunxu/multi-bit-text-watermark.