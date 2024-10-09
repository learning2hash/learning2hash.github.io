---
layout: publication
title: Text And Patterns For Effective Chain Of Thought It Takes Two To Tango
authors: Aman Madaan, Amir Yazdanbakhsh
conference: "Arxiv"
year: 2022
bibkey: madaan2022text
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2209.07686v2"}
tags: ['ARXIV']
---
The past decade has witnessed dramatic gains in natural language processing and an unprecedented scaling of large language models. These developments have been accelerated by the advent of few-shot techniques such as chain of thought (CoT) prompting. Specifically CoT pushes the performance of large language models in a few-shot setup by augmenting the prompts with intermediate steps. Despite impressive results across various tasks the reasons behind their success have not been explored. This work uses counterfactual prompting to develop a deeper understanding of CoT-based few-shot prompting mechanisms in large language models. We first systematically identify and define the key components of a prompt symbols patterns and text. Then we devise and conduct an exhaustive set of experiments across four different tasks by querying the model with counterfactual prompts where only one of these components is altered. Our experiments across three models (PaLM GPT-3 and CODEX) reveal several surprising findings and brings into question the conventional wisdom around few-shot prompting. First the presence of factual patterns in a prompt is practically immaterial to the success of CoT. Second our results conclude that the primary role of intermediate steps may not be to facilitate learning how to solve a task. The intermediate steps are rather a beacon for the model to realize what symbols to replicate in the output to form a factual answer. Further text imbues patterns with commonsense knowledge and meaning. Our empirical and qualitative analysis reveals that a symbiotic relationship between text and patterns explains the success of few-shot prompting text helps extract commonsense from the question to help patterns and patterns enforce task understanding and direct text generation.
