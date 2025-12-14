---
layout: publication
title: Unsupervised Bitext Mining And Translation Via Self-trained Contextual Embeddings
authors: Phillip Keung, Julian Salazar, Yichao Lu, Noah A. Smith
conference: Transactions of the Association for Computational Linguistics
year: 2020
bibkey: keung2020unsupervised
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.07761'}]
tags: [Evaluation, Supervised, Datasets, Unsupervised, TACL, ACL]
short_authors: Keung et al.
---
We describe an unsupervised method to create pseudo-parallel corpora for
machine translation (MT) from unaligned text. We use multilingual BERT to
create source and target sentence embeddings for nearest-neighbor search and
adapt the model via self-training. We validate our technique by extracting
parallel sentence pairs on the BUCC 2017 bitext mining task and observe up to a
24.5 point increase (absolute) in F1 scores over previous unsupervised methods.
We then improve an XLM-based unsupervised neural MT system pre-trained on
Wikipedia by supplementing it with pseudo-parallel text mined from the same
corpus, boosting unsupervised translation performance by up to 3.5 BLEU on the
WMT'14 French-English and WMT'16 German-English tasks and outperforming the
previous state-of-the-art. Finally, we enrich the IWSLT'15 English-Vietnamese
corpus with pseudo-parallel Wikipedia sentence pairs, yielding a 1.2 BLEU
improvement on the low-resource MT task. We demonstrate that unsupervised
bitext mining is an effective way of augmenting MT datasets and complements
existing techniques like initializing with pre-trained contextual embeddings.