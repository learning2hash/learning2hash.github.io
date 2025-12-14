---
layout: publication
title: 'Cot-mae V2: Contextual Masked Auto-encoder With Multi-view Modeling For Passage
  Retrieval'
authors: Xing Wu, Guangyuan Ma, Peng Wang, Meng Lin, Zijia Lin, Fuzheng Zhang, Songlin
  Hu
conference: Arxiv
year: 2023
bibkey: wu2023cot
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.03158'}]
tags: [Scalability, Evaluation, Few-shot & Zero-shot]
short_authors: Wu et al.
---
Growing techniques have been emerging to improve the performance of passage
retrieval. As an effective representation bottleneck pretraining technique, the
contextual masked auto-encoder utilizes contextual embedding to assist in the
reconstruction of passages. However, it only uses a single auto-encoding
pre-task for dense representation pre-training. This study brings multi-view
modeling to the contextual masked auto-encoder. Firstly, multi-view
representation utilizes both dense and sparse vectors as multi-view
representations, aiming to capture sentence semantics from different aspects.
Moreover, multiview decoding paradigm utilizes both autoencoding and
auto-regressive decoders in representation bottleneck pre-training, aiming to
provide both reconstructive and generative signals for better contextual
representation pretraining. We refer to this multi-view pretraining method as
CoT-MAE v2. Through extensive experiments, we show that CoT-MAE v2 is effective
and robust on large-scale passage retrieval benchmarks and out-of-domain
zero-shot benchmarks.