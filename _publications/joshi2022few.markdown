---
layout: publication
title: Few-shot Mining Of Naturally Occurring Inputs And Outputs
authors: Mandar Joshi, Terra Blevins, Mike Lewis, Daniel S. Weld, Luke Zettlemoyer
conference: Arxiv
year: 2022
bibkey: joshi2022few
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.04050'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Joshi et al.
---
Creating labeled natural language training data is expensive and requires
significant human effort. We mine input output examples from large corpora
using a supervised mining function trained using a small seed set of only 100
examples. The mining consists of two stages -- (1) a biencoder-based
recall-oriented dense search which pairs inputs with potential outputs, and (2)
a crossencoder-based filter which re-ranks the output of the biencoder stage
for better precision. Unlike model-generated data augmentation, our method
mines naturally occurring high-quality input output pairs to mimic the style of
the seed set for multiple tasks. On SQuAD-style reading comprehension,
augmenting the seed set with the mined data results in an improvement of 13 F1
over a BART-large baseline fine-tuned only on the seed set. Likewise, we see
improvements of 1.46 ROUGE-L on Xsum abstractive summarization.