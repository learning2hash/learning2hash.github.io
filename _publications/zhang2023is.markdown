---
layout: publication
title: Is Chatgpt Fair For Recommendation Evaluating Fairness In Large Language Model Recommendation
authors: Jizhi Zhang, Keqin Bao, Yang Zhang, Wenjie Wang, Fuli Feng, Xiangnan He
conference: "Arxiv"
year: 2023
bibkey: zhang2023is
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2305.07609v3"}
  - {name: "Code", url: "https://github.com/jizhi-zhang/FaiRLLM"}
tags: ['ARXIV', 'Has Code']
---
The remarkable achievements of Large Language Models (LLMs) have led to the emergence of a novel recommendation paradigm -- Recommendation via LLM (RecLLM). Nevertheless it is important to note that LLMs may contain social prejudices and therefore the fairness of recommendations made by RecLLM requires further investigation. To avoid the potential risks of RecLLM it is imperative to evaluate the fairness of RecLLM with respect to various sensitive attributes on the user side. Due to the differences between the RecLLM paradigm and the traditional recommendation paradigm it is problematic to directly use the fairness benchmark of traditional recommendation. To address the dilemma we propose a novel benchmark called Fairness of Recommendation via LLM (FaiRLLM). This benchmark comprises carefully crafted metrics and a dataset that accounts for eight sensitive attributes1 in two recommendation scenarios music and movies. By utilizing our FaiRLLM benchmark we conducted an evaluation of ChatGPT and discovered that it still exhibits unfairness to some sensitive attributes when generating recommendations. Our code and dataset can be found at https://github.com/jizhi-zhang/FaiRLLM.
