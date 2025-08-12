---
layout: publication
title: Boosting Named Entity Recognition With Neural Character Embeddings
authors: "Cicero Nogueira Dos Santos, Victor Guimar\xE3es"
conference: Proceedings of the Fifth Named Entity Workshop
year: 2015
bibkey: santos2015boosting
citations: 236
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1505.05008'}]
tags: ["NAACL"]
short_authors: "Cicero Nogueira Dos Santos, Victor Guimar\xE3es"
---
Most state-of-the-art named entity recognition (NER) systems rely on
handcrafted features and on the output of other NLP tasks such as
part-of-speech (POS) tagging and text chunking. In this work we propose a
language-independent NER system that uses automatically learned features only.
Our approach is based on the CharWNN deep neural network, which uses word-level
and character-level representations (embeddings) to perform sequential
classification. We perform an extensive number of experiments using two
annotated corpora in two different languages: HAREM I corpus, which contains
texts in Portuguese; and the SPA CoNLL-2002 corpus, which contains texts in
Spanish. Our experimental results shade light on the contribution of neural
character embeddings for NER. Moreover, we demonstrate that the same neural
network which has been successfully applied to POS tagging can also achieve
state-of-the-art results for language-independet NER, using the same
hyperparameters, and without any handcrafted features. For the HAREM I corpus,
CharWNN outperforms the state-of-the-art system by 7.9 points in the F1-score
for the total scenario (ten NE classes), and by 7.2 points in the F1 for the
selective scenario (five NE classes).