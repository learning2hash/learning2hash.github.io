---
layout: publication
title: Fast And Effective Biomedical Entity Linking Using A Dual Encoder
authors: Rajarshi Bhowmik, Karl Stratos, Gerard de Melo
conference: Arxiv
year: 2021
bibkey: bhowmik2021fast
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.05028'}]
tags: []
short_authors: Rajarshi Bhowmik, Karl Stratos, Gerard de Melo
---
Biomedical entity linking is the task of identifying mentions of biomedical
concepts in text documents and mapping them to canonical entities in a target
thesaurus. Recent advancements in entity linking using BERT-based models follow
a retrieve and rerank paradigm, where the candidate entities are first selected
using a retriever model, and then the retrieved candidates are ranked by a
reranker model. While this paradigm produces state-of-the-art results, they are
slow both at training and test time as they can process only one mention at a
time. To mitigate these issues, we propose a BERT-based dual encoder model that
resolves multiple mentions in a document in one shot. We show that our proposed
model is multiple times faster than existing BERT-based models while being
competitive in accuracy for biomedical entity linking. Additionally, we modify
our dual encoder model for end-to-end biomedical entity linking that performs
both mention span detection and entity disambiguation and out-performs two
recently proposed models.