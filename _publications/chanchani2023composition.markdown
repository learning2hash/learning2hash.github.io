---
layout: publication
title: Composition-contrastive Learning For Sentence Embeddings
authors: Sachin J. Chanchani, Ruihong Huang
conference: 'Proceedings of the 61st Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2023
bibkey: chanchani2023composition
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.07380'}]
tags: ["Self-Supervised", "Similarity Search"]
short_authors: Sachin J. Chanchani, Ruihong Huang
---
Vector representations of natural language are ubiquitous in search
applications. Recently, various methods based on contrastive learning have been
proposed to learn textual representations from unlabelled data; by maximizing
alignment between minimally-perturbed embeddings of the same text, and
encouraging a uniform distribution of embeddings across a broader corpus.
Differently, we propose maximizing alignment between texts and a composition of
their phrasal constituents. We consider several realizations of this objective
and elaborate the impact on representations in each case. Experimental results
on semantic textual similarity tasks show improvements over baselines that are
comparable with state-of-the-art approaches. Moreover, this work is the first
to do so without incurring costs in auxiliary training objectives or additional
network parameters.