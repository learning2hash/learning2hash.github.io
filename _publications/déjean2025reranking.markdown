---
layout: publication
title: Reranking With Compressed Document Representation
authors: "Herv\xE9 D\xE9jean, St\xE9phane Clinchant"
conference: Arxiv
year: 2025
bibkey: "d\xE9jean2025reranking"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.15394'}]
tags: ["Efficiency", "Re-Ranking"]
short_authors: "Herv\xE9 D\xE9jean, St\xE9phane Clinchant"
---
Reranking, the process of refining the output of a first-stage retriever, is often considered computationally expensive, especially with Large Language Models. Borrowing from recent advances in document compression for RAG, we reduce the input size by compressing documents into fixed-size embedding representations. We then teach a reranker to use compressed inputs by distillation. Although based on a billion-size model, our trained reranker using this compressed input can challenge smaller rerankers in terms of both effectiveness and efficiency, especially for long documents. Given that text compressors are still in their early development stages, we view this approach as promising.