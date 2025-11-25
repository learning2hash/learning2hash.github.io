---
layout: publication
title: Challenging Decoder Helps In Masked Auto-encoder Pre-training For Dense Passage
  Retrieval
authors: Zehan Li, Yanzhao Zhang, Dingkun Long, Pengjun Xie
conference: Arxiv
year: 2023
bibkey: li2023challenging
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.13197'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "Supervised", "Unsupervised"]
short_authors: Li et al.
---
Recently, various studies have been directed towards exploring dense passage
retrieval techniques employing pre-trained language models, among which the
masked auto-encoder (MAE) pre-training architecture has emerged as the most
promising. The conventional MAE framework relies on leveraging the passage
reconstruction of decoder to bolster the text representation ability of
encoder, thereby enhancing the performance of resulting dense retrieval
systems. Within the context of building the representation ability of the
encoder through passage reconstruction of decoder, it is reasonable to
postulate that a ``more demanding'' decoder will necessitate a corresponding
increase in the encoder's ability. To this end, we propose a novel token
importance aware masking strategy based on pointwise mutual information to
intensify the challenge of the decoder. Importantly, our approach can be
implemented in an unsupervised manner, without adding additional expenses to
the pre-training phase. Our experiments verify that the proposed method is both
effective and robust on large-scale supervised passage retrieval datasets and
out-of-domain zero-shot retrieval benchmarks.