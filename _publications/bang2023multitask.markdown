---
layout: publication
title: A Multitask Multilingual Multimodal Evaluation Of Chatgpt On Reasoning Hallucination And Interactivity
authors: Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy Lovenia, Ziwei Ji, Tiezheng Yu, Willy Chung, Quyet V. Do, Yan Xu, Pascale Fung
conference: "Arxiv"
year: 2023
bibkey: bang2023multitask
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2302.04023v4"}
tags: ['ARXIV', 'Cross Modal', 'Dataset']
---
This paper proposes a framework for quantitatively evaluating interactive LLMs such as ChatGPT using publicly available data sets. We carry out an extensive technical evaluation of ChatGPT using 23 data sets covering 8 different common NLP application tasks. We evaluate the multitask multilingual and multi-modal aspects of ChatGPT based on these data sets and a newly designed multimodal dataset. We find that ChatGPT outperforms LLMs with zero-shot learning on most tasks and even outperforms fine-tuned models on some tasks. We find that it is better at understanding non-Latin script languages than generating them. It is able to generate multimodal content from textual prompts via an intermediate code generation step. Moreover we find that ChatGPT is 63.4137; accurate on average in 10 different reasoning categories under logical reasoning non-textual reasoning and commonsense reasoning hence making it an unreliable reasoner. It is for example better at deductive than inductive reasoning. ChatGPT suffers from hallucination problems like other LLMs and it generates more extrinsic hallucinations from its parametric memory as it does not have access to an external knowledge base. Finally the interactive feature of ChatGPT enables human collaboration with the underlying LLM to improve its performance i.e 837; ROUGE-1 on summarization and 237; ChrF++ on machine translation in a multi-turn prompt engineering fashion. We also release codebase for evaluation set extraction.
