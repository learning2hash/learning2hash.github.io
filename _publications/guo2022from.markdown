---
layout: publication
title: From Images To Textual Prompts Zero-shot VQA With Frozen Large Language Models
authors: Jiaxian Guo, Junnan Li, Dongxu Li, Anthony Meng Huat Tiong, Boyang Li, Dacheng Tao, Steven C. H. Hoi
conference: "Arxiv"
year: 2022
bibkey: guo2022from
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2212.10846v3"}
tags: ['ARXIV']
---
Large language models (LLMs) have demonstrated excellent zero-shot generalization to new language tasks. However effective utilization of LLMs for zero-shot visual question-answering (VQA) remains challenging primarily due to the modality disconnection and task disconnection between LLM and VQA task. End-to-end training on vision and language data may bridge the disconnections but is inflexible and computationally expensive. To address this issue we propose emphImg2Prompt a plug-and-play module that provides the prompts that can bridge the aforementioned modality and task disconnections so that LLMs can perform zero-shot VQA tasks without end-to-end training. In order to provide such prompts we further employ LLM-agnostic models to provide prompts that can describe image content and self-constructed question-answer pairs which can effectively guide LLM to perform zero-shot VQA tasks. Img2Prompt offers the following benefits 1) It can flexibly work with various LLMs to perform VQA. 2)~Without the needing of end-to-end training it significantly reduces the cost of deploying LLM for zero-shot VQA tasks. 3) It achieves comparable or better performance than methods relying on end-to-end training. For example we outperform Flamingo citeDeepmindFlamingo2022 by 5.637; on VQAv2. On the challenging A-OKVQA dataset our method even outperforms few-shot methods by as much as 2037;.
