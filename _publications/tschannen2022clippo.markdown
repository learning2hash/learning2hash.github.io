---
layout: publication
title: 'CLIPPO: Image-and-language Understanding From Pixels Only'
authors: Michael Tschannen, Basil Mustafa, Neil Houlsby
conference: Arxiv
year: 2022
bibkey: tschannen2022clippo
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.08045'}]
tags: ["Few Shot & Zero Shot", "Multimodal Retrieval", "Self-Supervised"]
short_authors: Michael Tschannen, Basil Mustafa, Neil Houlsby
---
Multimodal models are becoming increasingly effective, in part due to unified
components, such as the Transformer architecture. However, multimodal models
still often consist of many task- and modality-specific pieces and training
procedures. For example, CLIP (Radford et al., 2021) trains independent text
and image towers via a contrastive loss. We explore an additional unification:
the use of a pure pixel-based model to perform image, text, and multimodal
tasks. Our model is trained with contrastive loss alone, so we call it
CLIP-Pixels Only (CLIPPO). CLIPPO uses a single encoder that processes both
regular images and text rendered as images. CLIPPO performs image-based tasks
such as retrieval and zero-shot image classification almost as well as
CLIP-style models, with half the number of parameters and no text-specific
tower or embedding. When trained jointly via image-text contrastive learning
and next-sentence contrastive learning, CLIPPO can perform well on natural
language understanding tasks, without any word-level loss (language modelling
or masked language modelling), outperforming pixel-based prior work.
Surprisingly, CLIPPO can obtain good accuracy in visual question answering,
simply by rendering the question and image together. Finally, we exploit the
fact that CLIPPO does not require a tokenizer to show that it can achieve
strong performance on multilingual multimodal retrieval without modifications.