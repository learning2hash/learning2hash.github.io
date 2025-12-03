---
layout: publication
title: Unifying Latent And Lexicon Representations For Effective Video-text Retrieval
authors: Haowei Liu, Yaya Shi, Haiyang Xu, Chunfeng Yuan, Qinghao Ye, Chenliang Li,
  Ming Yan, Ji Zhang, Fei Huang, Bing Li, Weiming Hu
conference: Arxiv
year: 2024
bibkey: liu2024unifying
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.16769'}]
tags: ["Efficiency", "Evaluation", "Text Retrieval", "Tools & Libraries"]
short_authors: Liu et al.
---
In video-text retrieval, most existing methods adopt the dual-encoder
architecture for fast retrieval, which employs two individual encoders to
extract global latent representations for videos and texts. However, they face
challenges in capturing fine-grained semantic concepts. In this work, we
propose the UNIFY framework, which learns lexicon representations to capture
fine-grained semantics and combines the strengths of latent and lexicon
representations for video-text retrieval. Specifically, we map videos and texts
into a pre-defined lexicon space, where each dimension corresponds to a
semantic concept. A two-stage semantics grounding approach is proposed to
activate semantically relevant dimensions and suppress irrelevant dimensions.
The learned lexicon representations can thus reflect fine-grained semantics of
videos and texts. Furthermore, to leverage the complementarity between latent
and lexicon representations, we propose a unified learning scheme to facilitate
mutual learning via structure sharing and self-distillation. Experimental
results show our UNIFY framework largely outperforms previous video-text
retrieval methods, with 4.8% and 8.2% Recall@1 improvement on MSR-VTT and
DiDeMo respectively.