---
layout: publication
title: CIEM Contrastive Instruction Evaluation Method For Better Instruction Tuning
authors: Hongyu Hu, Jiyuan Zhang, Minyi Zhao, Zhenbang Sun
conference: "Arxiv"
year: 2023
bibkey: hu2023ciem
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2309.02301v2"}
tags: ['ARXIV', 'Cross Modal']
---
Nowadays the research on Large Vision-Language Models (LVLMs) has been significantly promoted thanks to the success of Large Language Models (LLM). Nevertheless these Vision-Language Models (VLMs) are suffering from the drawback of hallucination -- due to insufficient understanding of vision and language modalities VLMs may generate incorrect perception information when doing downstream applications for example captioning a non-existent entity. To address the hallucination phenomenon on the one hand we introduce a Contrastive Instruction Evaluation Method (CIEM) which is an automatic pipeline that leverages an annotated image-text dataset coupled with an LLM to generate factual/contrastive question-answer pairs for the evaluation of the hallucination of VLMs. On the other hand based on CIEM we further propose a new instruction tuning method called CIT (the abbreviation of Contrastive Instruction Tuning) to alleviate the hallucination of VLMs by automatically producing high-quality factual/contrastive question-answer pairs and corresponding justifications for model tuning. Through extensive experiments on CIEM and CIT we pinpoint the hallucination issues commonly present in existing VLMs the disability of the current instruction-tuning dataset to handle the hallucination phenomenon and the superiority of CIT-tuned VLMs over both CIEM and public datasets.
