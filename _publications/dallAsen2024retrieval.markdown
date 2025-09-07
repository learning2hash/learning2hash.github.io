---
layout: publication
title: Retrieval-enriched Zero-shot Image Classification In Low-resource Domains
authors: Nicola Dall'Asen, Yiming Wang, Enrico Fini, Elisa Ricci
conference: Proceedings of the 2024 Conference on Empirical Methods in Natural Language
  Processing
year: 2024
bibkey: dallAsen2024retrieval
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.00988'}]
tags: ["EMNLP", "Evaluation", "Few Shot & Zero Shot"]
short_authors: Dall'Asen et al.
---
Low-resource domains, characterized by scarce data and annotations, present
significant challenges for language and visual understanding tasks, with the
latter much under-explored in the literature. Recent advancements in
Vision-Language Models (VLM) have shown promising results in high-resource
domains but fall short in low-resource concepts that are under-represented
(e.g. only a handful of images per category) in the pre-training set. We tackle
the challenging task of zero-shot low-resource image classification from a
novel perspective. By leveraging a retrieval-based strategy, we achieve this in
a training-free fashion. Specifically, our method, named CoRE (Combination of
Retrieval Enrichment), enriches the representation of both query images and
class prototypes by retrieving relevant textual information from large
web-crawled databases. This retrieval-based enrichment significantly boosts
classification performance by incorporating the broader contextual information
relevant to the specific class. We validate our method on a newly established
benchmark covering diverse low-resource domains, including medical imaging,
rare plants, and circuits. Our experiments demonstrate that CORE outperforms
existing state-of-the-art methods that rely on synthetic data generation and
model fine-tuning.