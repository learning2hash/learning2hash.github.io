---
layout: publication
title: Passage Retrieval For Outside-knowledge Visual Question Answering
authors: Chen Qu, Hamed Zamani, Liu Yang, W. Bruce Croft, Erik Learned-Miller
conference: Proceedings of the 44th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2021
bibkey: qu2021passage
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.03938'}]
tags: ["Evaluation", "Image Retrieval", "Multimodal Retrieval", "SIGIR"]
short_authors: Qu et al.
---
In this work, we address multi-modal information needs that contain text
questions and images by focusing on passage retrieval for outside-knowledge
visual question answering. This task requires access to outside knowledge,
which in our case we define to be a large unstructured passage collection. We
first conduct sparse retrieval with BM25 and study expanding the question with
object names and image captions. We verify that visual clues play an important
role and captions tend to be more informative than object names in sparse
retrieval. We then construct a dual-encoder dense retriever, with the query
encoder being LXMERT, a multi-modal pre-trained transformer. We further show
that dense retrieval significantly outperforms sparse retrieval that uses
object expansion. Moreover, dense retrieval matches the performance of sparse
retrieval that leverages human-generated captions.