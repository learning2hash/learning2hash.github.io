---
layout: publication
title: Negative Object Presence Evaluation (NOPE) To Measure Object Hallucination In Vision-language Models
authors: Holy Lovenia, Wenliang Dai, Samuel Cahyawijaya, Ziwei Ji, Pascale Fung
conference: "Arxiv"
year: 2023
bibkey: lovenia2023negative
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2310.05338v2"}
tags: ['ARXIV', 'Cross Modal', 'Supervised']
---
Object hallucination poses a significant challenge in vision-language (VL) models often leading to the generation of nonsensical or unfaithful responses with non-existent objects. However the absence of a general measurement for evaluating object hallucination in VL models has hindered our understanding and ability to mitigate this issue. In this work we present NOPE (Negative Object Presence Evaluation) a novel benchmark designed to assess object hallucination in VL models through visual question answering (VQA). We propose a cost-effective and scalable approach utilizing large language models to generate 29.5k synthetic negative pronoun (NegP) data of high quality for NOPE. We extensively investigate the performance of 10 state-of-the-art VL models in discerning the non-existence of objects in visual questions where the ground truth answers are denoted as NegP (e.g. none). Additionally we evaluate their standard performance on visual questions on 9 other VQA datasets. Through our experiments we demonstrate that no VL model is immune to the vulnerability of object hallucination as all models achieve accuracy below 1037; on NegP. Furthermore we uncover that lexically diverse visual questions question types with large scopes and scene-relevant objects capitalize the risk of object hallucination in VL models.
