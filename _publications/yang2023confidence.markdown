---
layout: publication
title: Confidence-calibrated Ensemble Dense Phrase Retrieval
authors: William Yang, Noah Bergam, Arnav Jain, Nima Sheikhoslami
conference: Arxiv
year: 2023
bibkey: yang2023confidence
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.15917'}]
tags: ["Datasets", "Evaluation", "Text Retrieval"]
short_authors: Yang et al.
---
In this paper, we consider the extent to which the transformer-based Dense
Passage Retrieval (DPR) algorithm, developed by (Karpukhin et. al. 2020), can
be optimized without further pre-training. Our method involves two particular
insights: we apply the DPR context encoder at various phrase lengths (e.g.
one-sentence versus five-sentence segments), and we take a
confidence-calibrated ensemble prediction over all of these different
segmentations. This somewhat exhaustive approach achieves start-of-the-art
results on benchmark datasets such as Google NQ and SQuAD. We also apply our
method to domain-specific datasets, and the results suggest how different
granularities are optimal for different domains