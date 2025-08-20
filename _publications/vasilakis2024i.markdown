---
layout: publication
title: 'I Can Listen But Cannot Read: An Evaluation Of Two-tower Multimodal Systems
  For Instrument Recognition'
authors: Yannis Vasilakis, Rachel Bittner, Johan Pauwels
conference: Arxiv
year: 2024
bibkey: vasilakis2024i
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.18058'}]
tags: [Few-shot & Zero-shot, Evaluation]
short_authors: Yannis Vasilakis, Rachel Bittner, Johan Pauwels
---
Music two-tower multimodal systems integrate audio and text modalities into a
joint audio-text space, enabling direct comparison between songs and their
corresponding labels. These systems enable new approaches for classification
and retrieval, leveraging both modalities. Despite the promising results they
have shown for zero-shot classification and retrieval tasks, closer inspection
of the embeddings is needed. This paper evaluates the inherent zero-shot
properties of joint audio-text spaces for the case-study of instrument
recognition. We present an evaluation and analysis of two-tower systems for
zero-shot instrument recognition and a detailed analysis of the properties of
the pre-joint and joint embeddings spaces. Our findings suggest that audio
encoders alone demonstrate good quality, while challenges remain within the
text encoder or joint space projection. Specifically, two-tower systems exhibit
sensitivity towards specific words, favoring generic prompts over musically
informed ones. Despite the large size of textual encoders, they do not yet
leverage additional textual context or infer instruments accurately from their
descriptions. Lastly, a novel approach for quantifying the semantic
meaningfulness of the textual space leveraging an instrument ontology is
proposed. This method reveals deficiencies in the systems' understanding of
instruments and provides evidence of the need for fine-tuning text encoders on
musical data.