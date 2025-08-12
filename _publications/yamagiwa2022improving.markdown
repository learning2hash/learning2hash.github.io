---
layout: publication
title: Improving Word Mover's Distance By Leveraging Self-attention Matrix
authors: Hiroaki Yamagiwa, Sho Yokoi, Hidetoshi Shimodaira
conference: Arxiv
year: 2022
bibkey: yamagiwa2022improving
citations: 0
additional_links: [{name: Code, url: 'https://github.com/ymgw55/WSMD'}, {name: Paper,
    url: 'https://arxiv.org/abs/2211.06229'}]
tags: []
short_authors: Hiroaki Yamagiwa, Sho Yokoi, Hidetoshi Shimodaira
---
Measuring the semantic similarity between two sentences is still an important
task. The word mover's distance (WMD) computes the similarity via the optimal
alignment between the sets of word embeddings. However, WMD does not utilize
word order, making it challenging to distinguish sentences with significant
overlaps of similar words, even if they are semantically very different. Here,
we attempt to improve WMD by incorporating the sentence structure represented
by BERT's self-attention matrix (SAM). The proposed method is based on the
Fused Gromov-Wasserstein distance, which simultaneously considers the
similarity of the word embedding and the SAM for calculating the optimal
transport between two sentences. Experiments demonstrate the proposed method
enhances WMD and its variants in paraphrase identification with near-equivalent
performance in semantic textual similarity. Our code is available at
https://github.com/ymgw55/WSMD.