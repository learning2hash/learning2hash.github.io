---
layout: publication
title: Prompting GPT-3 To Be Reliable
authors: Chenglei Si, Zhe Gan, Zhengyuan Yang, Shuohang Wang, Jianfeng Wang, Jordan Boyd-graber, Lijuan Wang
conference: "Arxiv"
year: 2022
bibkey: si2022prompting
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2210.09150v2"}
tags: ['ARXIV', 'Graph', 'Supervised']
---
Large language models (LLMs) show impressive abilities via few-shot prompting. Commercialized APIs such as OpenAI GPT-3 further increase their use in real-world language applications. However the crucial problem of how to improve the reliability of GPT-3 is still under-explored. While reliability is a broad and vaguely defined term we decompose reliability into four main facets that correspond to the existing framework of ML safety and are well-recognized to be important generalizability social biases calibration and factuality. Our core contribution is to establish simple and effective prompts that improve GPT-3s reliability as it 1) generalizes out-of-distribution 2) balances demographic distribution and uses natural language instructions to reduce social biases 3) calibrates output probabilities and 4) updates the LLMs factual knowledge and reasoning chains. With appropriate prompts GPT-3 is more reliable than smaller-scale supervised models on all these facets. We release all processed datasets evaluation scripts and model predictions. Our systematic empirical study not only sheds new insights on the reliability of prompting LLMs but more importantly our prompting strategies can help practitioners more reliably use LLMs like GPT-3.
