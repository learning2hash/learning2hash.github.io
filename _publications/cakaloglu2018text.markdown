---
layout: publication
title: Text Embeddings For Retrieval From A Large Knowledge Base
authors: Cakaloglu Tolgahan, Szegedy Christian, Xu Xiaowei
conference: Arxiv
year: 2018
bibkey: cakaloglu2018text
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.10176'}]
tags: [Graph Based ANN, Text Retrieval, Evaluation, DATASETS]
---
Text embedding representing natural language documents in a semantic vector
space can be used for document retrieval using nearest neighbor lookup. In
order to study the feasibility of neural models specialized for retrieval in a
semantically meaningful way, we suggest the use of the Stanford Question
Answering Dataset (SQuAD) in an open-domain question answering context, where
the first task is to find paragraphs useful for answering a given question.
First, we compare the quality of various text-embedding methods on the
performance of retrieval and give an extensive empirical comparison on the
performance of various non-augmented base embedding with, and without IDF
weighting. Our main results are that by training deep residual neural models,
specifically for retrieval purposes, can yield significant gains when it is
used to augment existing embeddings. We also establish that deeper models are
superior to this task. The best base baseline embeddings augmented by our
learned neural approach improves the top-1 paragraph recall of the system by
14%.