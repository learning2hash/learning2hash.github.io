---
layout: publication
title: Contrastive Visual Semantic Pretraining Magnifies The Semantics Of Natural
  Language Representations
authors: Robert Wolfe, Aylin Caliskan
conference: 'Proceedings of the 60th Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2022
bibkey: wolfe2022contrastive
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.07511'}]
tags: []
short_authors: Robert Wolfe, Aylin Caliskan
---
We examine the effects of contrastive visual semantic pretraining by
comparing the geometry and semantic properties of contextualized English
language representations formed by GPT-2 and CLIP, a zero-shot multimodal image
classifier which adapts the GPT-2 architecture to encode image captions. We
find that contrastive visual semantic pretraining significantly mitigates the
anisotropy found in contextualized word embeddings from GPT-2, such that the
intra-layer self-similarity (mean pairwise cosine similarity) of CLIP word
embeddings is under .25 in all layers, compared to greater than .95 in the top
layer of GPT-2. CLIP word embeddings outperform GPT-2 on word-level semantic
intrinsic evaluation tasks, and achieve a new corpus-based state of the art for
the RG65 evaluation, at .88. CLIP also forms fine-grained semantic
representations of sentences, and obtains Spearman's rho = .73 on the
SemEval-2017 Semantic Textual Similarity Benchmark with no fine-tuning,
compared to no greater than rho = .45 in any layer of GPT-2. Finally,
intra-layer self-similarity of CLIP sentence embeddings decreases as the layer
index increases, finishing at .25 in the top layer, while the self-similarity
of GPT-2 sentence embeddings formed using the EOS token increases
layer-over-layer and never falls below .97. Our results indicate that high
anisotropy is not an inevitable consequence of contextualization, and that
visual semantic pretraining is beneficial not only for ordering visual
representations, but also for encoding useful semantic representations of
language, both on the word level and the sentence level.