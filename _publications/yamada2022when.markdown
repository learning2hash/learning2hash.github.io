---
layout: publication
title: When Are Lemons Purple? The Concept Association Bias Of Vision-language Models
authors: Yutaro Yamada, Yingtian Tang, Yoyo Zhang, Ilker Yildirim
conference: Arxiv
year: 2022
bibkey: yamada2022when
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.12043'}]
tags: ["Distance Metric Learning", "Evaluation", "Few Shot & Zero Shot", "Multimodal Retrieval", "Text Retrieval"]
short_authors: Yamada et al.
---
Large-scale vision-language models such as CLIP have shown impressive
performance on zero-shot image classification and image-to-text retrieval.
However, such performance does not realize in tasks that require a
finer-grained correspondence between vision and language, such as Visual
Question Answering (VQA). As a potential cause of the difficulty of applying
these models to VQA and similar tasks, we report an interesting phenomenon of
vision-language models, which we call the Concept Association Bias (CAB). We
find that models with CAB tend to treat input as a bag of concepts and attempt
to fill in the other missing concept crossmodally, leading to an unexpected
zero-shot prediction. We demonstrate CAB by showing that CLIP's zero-shot
classification performance greatly suffers when there is a strong concept
association between an object (e.g. eggplant) and an attribute (e.g. color
purple). We also show that the strength of CAB predicts the performance on VQA.
We observe that CAB is prevalent in vision-language models trained with
contrastive losses, even when autoregressive losses are jointly employed.
However, a model that solely relies on autoregressive loss seems to exhibit
minimal or no signs of CAB.