---
layout: publication
title: Rationale-augmented Ensembles In Language Models
authors: Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Denny Zhou
conference: "Arxiv"
year: 2022
bibkey: wang2022rationale
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2207.00747v1"}
tags: ['ARXIV']
---
Recent research has shown that rationales or step-by-step chains of thought can be used to improve performance in multi-step reasoning tasks. We reconsider rationale-augmented prompting for few-shot in-context learning where (input - output) prompts are expanded to (input rationale - output) prompts. For rationale-augmented prompting we demonstrate how existing approaches which rely on manual prompt engineering are subject to sub-optimal rationales that may harm performance. To mitigate this brittleness we propose a unified framework of rationale-augmented ensembles where we identify rationale sampling in the output space as the key component to robustly improve performance. This framework is general and can easily be extended to common natural language processing tasks even those that do not traditionally leverage intermediate steps such as question answering word sense disambiguation and sentiment analysis. We demonstrate that rationale-augmented ensembles achieve more accurate and interpretable results than existing prompting approaches--including standard prompting without rationales and rationale-based chain-of-thought prompting--while simultaneously improving interpretability of model predictions through the associated rationales.
