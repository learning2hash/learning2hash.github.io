---
layout: publication
title: Unsupervised Domain Adaption For Neural Information Retrieval
authors: Carlos Dominguez, Jon Ander Campos, Eneko Agirre, Gorka Azkune
conference: Arxiv
year: 2023
bibkey: dominguez2023unsupervised
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.09350'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Unsupervised"]
short_authors: Dominguez et al.
---
Neural information retrieval requires costly annotated data for each target
domain to be competitive. Synthetic annotation by query generation using Large
Language Models or rule-based string manipulation has been proposed as an
alternative, but their relative merits have not been analysed. In this paper,
we compare both methods head-to-head using the same neural IR architecture. We
focus on the BEIR benchmark, which includes test datasets from several domains
with no training data, and explore two scenarios: zero-shot, where the
supervised system is trained in a large out-of-domain dataset (MS-MARCO); and
unsupervised domain adaptation, where, in addition to MS-MARCO, the system is
fine-tuned in synthetic data from the target domain. Our results indicate that
Large Language Models outperform rule-based methods in all scenarios by a large
margin, and, more importantly, that unsupervised domain adaptation is effective
compared to applying a supervised IR system in a zero-shot fashion. In addition
we explore several sizes of open Large Language Models to generate synthetic
data and find that a medium-sized model suffices. Code and models are publicly
available for reproducibility.