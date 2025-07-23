---
layout: publication
title: 'Laprador: Unsupervised Pretrained Dense Retriever For Zero-shot Text Retrieval'
authors: Xu Canwen, Guo Daya, Duan Nan, Mcauley Julian
conference: 'Findings of the Association for Computational Linguistics: ACL 2022'
year: 2022
bibkey: xu2022laprador
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.06169'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "Text Retrieval", "Unsupervised"]
short_authors: Xu et al.
---
In this paper, we propose LaPraDoR, a pretrained dual-tower dense retriever
that does not require any supervised data for training. Specifically, we first
present Iterative Contrastive Learning (ICoL) that iteratively trains the query
and document encoders with a cache mechanism. ICoL not only enlarges the number
of negative instances but also keeps representations of cached examples in the
same hidden space. We then propose Lexicon-Enhanced Dense Retrieval (LEDR) as a
simple yet effective way to enhance dense retrieval with lexical matching. We
evaluate LaPraDoR on the recently proposed BEIR benchmark, including 18
datasets of 9 zero-shot text retrieval tasks. Experimental results show that
LaPraDoR achieves state-of-the-art performance compared with supervised dense
retrieval models, and further analysis reveals the effectiveness of our
training strategy and objectives. Compared to re-ranking, our lexicon-enhanced
approach can be run in milliseconds (22.5x faster) while achieving superior
performance.