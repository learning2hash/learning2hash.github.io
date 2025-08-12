---
layout: publication
title: 'Familiarity: Better Evaluation Of Zero-shot Named Entity Recognition By Quantifying
  Label Shifts In Synthetic Training Data'
authors: Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, Alan
  Akbik
conference: 'Proceedings of the 2025 Conference of the Nations of the Americas Chapter
  of the Association for Computational Linguistics: Human Language Technologies (Volume
  1: Long Papers)'
year: 2025
bibkey: golde2024familiarity
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.10121'}]
tags: ["Evaluation"]
short_authors: Golde et al.
---
Zero-shot named entity recognition (NER) is the task of detecting named
entities of specific types (such as 'Person' or 'Medicine') without any
training examples. Current research increasingly relies on large synthetic
datasets, automatically generated to cover tens of thousands of distinct entity
types, to train zero-shot NER models. However, in this paper, we find that
these synthetic datasets often contain entity types that are semantically
highly similar to (or even the same as) those in standard evaluation
benchmarks. Because of this overlap, we argue that reported F1 scores for
zero-shot NER overestimate the true capabilities of these approaches. Further,
we argue that current evaluation setups provide an incomplete picture of
zero-shot abilities since they do not quantify the label shift (i.e., the
similarity of labels) between training and evaluation datasets. To address
these issues, we propose Familiarity, a novel metric that captures both the
semantic similarity between entity types in training and evaluation, as well as
their frequency in the training data, to provide an estimate of label shift. It
allows researchers to contextualize reported zero-shot NER scores when using
custom synthetic training datasets. Further, it enables researchers to generate
evaluation setups of various transfer difficulties for fine-grained analysis of
zero-shot NER.