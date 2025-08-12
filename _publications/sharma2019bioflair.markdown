---
layout: publication
title: 'Bioflair: Pretrained Pooled Contextualized Embeddings For Biomedical Sequence
  Labeling Tasks'
authors: Shreyas Sharma, Ron Daniel
conference: Arxiv
year: 2019
bibkey: sharma2019bioflair
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.05760'}]
tags: ["Evaluation"]
short_authors: Shreyas Sharma, Ron Daniel
---
Biomedical Named Entity Recognition (NER) is a challenging problem in
biomedical information processing due to the widespread ambiguity of out of
context terms and extensive lexical variations. Performance on bioNER
benchmarks continues to improve due to advances like BERT, GPT, and XLNet.
FLAIR (1) is an alternative embedding model which is less computationally
intensive than the others mentioned. We test FLAIR and its pretrained PubMed
embeddings (which we term BioFLAIR) on a variety of bio NER tasks and compare
those with results from BERT-type networks. We also investigate the effects of
a small amount of additional pretraining on PubMed content, and of combining
FLAIR and ELMO models. We find that with the provided embeddings, FLAIR
performs on-par with the BERT networks - even establishing a new state of the
art on one benchmark. Additional pretraining did not provide a clear benefit,
although this might change with even more pretraining being done. Stacking the
FLAIR embeddings with others typically does provide a boost in the benchmark
results.