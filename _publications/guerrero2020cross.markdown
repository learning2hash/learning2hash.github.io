---
layout: publication
title: 'Cross-modal Retrieval And Synthesis (X-MRS): Closing The Modality Gap In Shared
  Representation Learning'
authors: Ricardo Guerrero, Hai Xuan Pham, Vladimir Pavlovic
conference: Arxiv
year: 2020
bibkey: guerrero2020cross
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.01345'}]
tags: ["Multimodal Retrieval"]
short_authors: Ricardo Guerrero, Hai Xuan Pham, Vladimir Pavlovic
---
Computational food analysis (CFA) naturally requires multi-modal evidence of
a particular food, e.g., images, recipe text, etc. A key to making CFA possible
is multi-modal shared representation learning, which aims to create a joint
representation of the multiple views (text and image) of the data. In this work
we propose a method for food domain cross-modal shared representation learning
that preserves the vast semantic richness present in the food data. Our
proposed method employs an effective transformer-based multilingual recipe
encoder coupled with a traditional image embedding architecture. Here, we
propose the use of imperfect multilingual translations to effectively
regularize the model while at the same time adding functionality across
multiple languages and alphabets. Experimental analysis on the public Recipe1M
dataset shows that the representation learned via the proposed method
significantly outperforms the current state-of-the-arts (SOTA) on retrieval
tasks. Furthermore, the representational power of the learned representation is
demonstrated through a generative food image synthesis model conditioned on
recipe embeddings. Synthesized images can effectively reproduce the visual
appearance of paired samples, indicating that the learned representation
captures the joint semantics of both the textual recipe and its visual content,
thus narrowing the modality gap.