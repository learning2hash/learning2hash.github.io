---
layout: publication
title: REPLUG Retrieval-augmented Black-box Language Models
authors: Weijia Shi, Sewon Min, Michihiro Yasunaga, Minjoon Seo, Rich James, Mike Lewis, Luke Zettlemoyer, Wen-tau Yih
conference: "Arxiv"
year: 2023
bibkey: shi2023replug
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2301.12652v4"}
tags: ['ARXIV', 'Supervised']
---
We introduce REPLUG a retrieval-augmented language modeling framework that treats the language model (LM) as a black box and augments it with a tuneable retrieval model. Unlike prior retrieval-augmented LMs that train language models with special cross attention mechanisms to encode the retrieved text REPLUG simply prepends retrieved documents to the input for the frozen black-box LM. This simple design can be easily applied to any existing retrieval and language models. Furthermore we show that the LM can be used to supervise the retrieval model which can then find documents that help the LM make better predictions. Our experiments demonstrate that REPLUG with the tuned retriever significantly improves the performance of GPT-3 (175B) on language modeling by 6.337; as well as the performance of Codex on five-shot MMLU by 5.137;.
