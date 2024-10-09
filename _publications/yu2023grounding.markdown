---
layout: publication
title: Grounding Language Models To Images For Multimodal Inputs And Outputs
authors: Jing Yu Koh, Ruslan Salakhutdinov, Daniel Fried
conference: "Arxiv"
year: 2023
bibkey: yu2023grounding
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2301.13823v4"}
tags: ['ARXIV', 'Cross Modal', 'Image Retrieval']
---
We propose an efficient method to ground pretrained text-only language models to the visual domain enabling them to process arbitrarily interleaved image-and-text data and generate text interleaved with retrieved images. Our method leverages the abilities of language models learnt from large scale text-only pretraining such as in-context learning and free-form text generation. We keep the language model frozen and finetune input and output linear layers to enable cross-modality interactions. This allows our model to process arbitrarily interleaved image-and-text inputs and generate free-form text interleaved with retrieved images. We achieve strong zero-shot performance on grounded tasks such as contextual image retrieval and multimodal dialogue and showcase compelling interactive abilities. Our approach works with any off-the-shelf language model and paves the way towards an effective general solution for leveraging pretrained language models in visually grounded settings.
