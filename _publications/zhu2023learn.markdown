---
layout: publication
title: 'Learn To Not Link: Exploring NIL Prediction In Entity Linking'
authors: Fangwei Zhu, Jifan Yu, Hailong Jin, Juanzi Li, Lei Hou, Zhifang Sui
conference: 'Findings of the Association for Computational Linguistics: ACL 2023'
year: 2023
bibkey: zhu2023learn
citations: 2
additional_links: [{name: Code, url: 'https://github.com/solitaryzero/NIL_EL'}, {
    name: Paper, url: 'https://arxiv.org/abs/2305.15725'}]
tags: []
short_authors: Zhu et al.
---
Entity linking models have achieved significant success via utilizing
pretrained language models to capture semantic features. However, the NIL
prediction problem, which aims to identify mentions without a corresponding
entity in the knowledge base, has received insufficient attention. We
categorize mentions linking to NIL into Missing Entity and Non-Entity Phrase,
and propose an entity linking dataset NEL that focuses on the NIL prediction
problem. NEL takes ambiguous entities as seeds, collects relevant mention
context in the Wikipedia corpus, and ensures the presence of mentions linking
to NIL by human annotation and entity masking. We conduct a series of
experiments with the widely used bi-encoder and cross-encoder entity linking
models, results show that both types of NIL mentions in training data have a
significant influence on the accuracy of NIL prediction. Our code and dataset
can be accessed at https://github.com/solitaryzero/NIL_EL