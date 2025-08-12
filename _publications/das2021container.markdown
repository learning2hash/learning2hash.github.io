---
layout: publication
title: 'Container: Few-shot Named Entity Recognition Via Contrastive Learning'
authors: Sarkar Snigdha Sarathi Das, Arzoo Katiyar, Rebecca J. Passonneau, Rui Zhang
conference: 'Proceedings of the 60th Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2022
bibkey: das2021container
citations: 118
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.07589'}]
tags: []
short_authors: Das et al.
---
Named Entity Recognition (NER) in Few-Shot setting is imperative for entity
tagging in low resource domains. Existing approaches only learn class-specific
semantic features and intermediate representations from source domains. This
affects generalizability to unseen target domains, resulting in suboptimal
performances. To this end, we present CONTaiNER, a novel contrastive learning
technique that optimizes the inter-token distribution distance for Few-Shot
NER. Instead of optimizing class-specific attributes, CONTaiNER optimizes a
generalized objective of differentiating between token categories based on
their Gaussian-distributed embeddings. This effectively alleviates overfitting
issues originating from training domains. Our experiments in several
traditional test domains (OntoNotes, CoNLL'03, WNUT '17, GUM) and a new large
scale Few-Shot NER dataset (Few-NERD) demonstrate that on average, CONTaiNER
outperforms previous methods by 3%-13% absolute F1 points while showing
consistent performance trends, even in challenging scenarios where previous
approaches could not achieve appreciable performance.