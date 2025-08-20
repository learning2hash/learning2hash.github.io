---
layout: publication
title: 'Pic: A Phrase-in-context Dataset For Phrase Understanding And Semantic Search'
authors: Thang M. Pham, Seunghyun Yoon, Trung Bui, Anh Nguyen
conference: Proceedings of the 17th Conference of the European Chapter of the Association
  for Computational Linguistics
year: 2023
bibkey: pham2022pic
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.09068'}]
tags: [Datasets, EACL, ACL, Evaluation]
short_authors: Pham et al.
---
While contextualized word embeddings have been a de-facto standard, learning
contextualized phrase embeddings is less explored and being hindered by the
lack of a human-annotated benchmark that tests machine understanding of phrase
semantics given a context sentence or paragraph (instead of phrases alone). To
fill this gap, we propose PiC -- a dataset of ~28K of noun phrases accompanied
by their contextual Wikipedia pages and a suite of three tasks for training and
evaluating phrase embeddings. Training on PiC improves ranking models' accuracy
and remarkably pushes span-selection (SS) models (i.e., predicting the start
and end index of the target phrase) near-human accuracy, which is 95% Exact
Match (EM) on semantic search given a query phrase and a passage.
Interestingly, we find evidence that such impressive performance is because the
SS models learn to better capture the common meaning of a phrase regardless of
its actual context. SotA models perform poorly in distinguishing two senses of
the same phrase in two contexts (~60% EM) and in estimating the similarity
between two different phrases in the same context (~70% EM).