---
layout: publication
title: Universal Multimodal Representation For Language Understanding
authors: Zhuosheng Zhang, Kehai Chen, Rui Wang, Masao Utiyama, Eiichiro Sumita, Zuchao
  Li, Hai Zhao
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2023
bibkey: zhang2023universal
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.03344'}]
tags: []
short_authors: Zhang et al.
---
Representation learning is the foundation of natural language processing
(NLP). This work presents new methods to employ visual information as assistant
signals to general NLP tasks. For each sentence, we first retrieve a flexible
number of images either from a light topic-image lookup table extracted over
the existing sentence-image pairs or a shared cross-modal embedding space that
is pre-trained on out-of-shelf text-image pairs. Then, the text and images are
encoded by a Transformer encoder and convolutional neural network,
respectively. The two sequences of representations are further fused by an
attention layer for the interaction of the two modalities. In this study, the
retrieval process is controllable and flexible. The universal visual
representation overcomes the lack of large-scale bilingual sentence-image
pairs. Our method can be easily applied to text-only tasks without manually
annotated multimodal parallel corpora. We apply the proposed method to a wide
range of natural language generation and understanding tasks, including neural
machine translation, natural language inference, and semantic similarity.
Experimental results show that our method is generally effective for different
tasks and languages. Analysis indicates that the visual signals enrich textual
representations of content words, provide fine-grained grounding information
about the relationship between concepts and events, and potentially conduce to
disambiguation.