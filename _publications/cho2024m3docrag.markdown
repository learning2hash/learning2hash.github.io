---
layout: publication
title: 'M3docrag: Multi-modal Retrieval Is What You Need For Multi-page Multi-document
  Understanding'
authors: Jaemin Cho, Debanjan Mahata, Ozan Irsoy, Yujie He, Mohit Bansal
conference: Arxiv
year: 2024
bibkey: cho2024m3docrag
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.04952'}]
tags: ["Datasets", "Evaluation", "Tools & Libraries"]
short_authors: Cho et al.
---
Document visual question answering (DocVQA) pipelines that answer questions
from documents have broad applications. Existing methods focus on handling
single-page documents with multi-modal language models (MLMs), or rely on
text-based retrieval-augmented generation (RAG) that uses text extraction tools
such as optical character recognition (OCR). However, there are difficulties in
applying these methods in real-world scenarios: (a) questions often require
information across different pages or documents, where MLMs cannot handle many
long documents; (b) documents often have important information in visual
elements such as figures, but text extraction tools ignore them. We introduce
M3DocRAG, a novel multi-modal RAG framework that flexibly accommodates various
document contexts (closed-domain and open-domain), question hops (single-hop
and multi-hop), and evidence modalities (text, chart, figure, etc.). M3DocRAG
finds relevant documents and answers questions using a multi-modal retriever
and an MLM, so that it can efficiently handle single or many documents while
preserving visual information. Since previous DocVQA datasets ask questions in
the context of a specific document, we also present M3DocVQA, a new benchmark
for evaluating open-domain DocVQA over 3,000+ PDF documents with 40,000+ pages.
In three benchmarks (M3DocVQA/MMLongBench-Doc/MP-DocVQA), empirical results
show that M3DocRAG with ColPali and Qwen2-VL 7B achieves superior performance
than many strong baselines, including state-of-the-art performance in
MP-DocVQA. We provide comprehensive analyses of different indexing, MLMs, and
retrieval models. Lastly, we qualitatively show that M3DocRAG can successfully
handle various scenarios, such as when relevant information exists across
multiple pages and when answer evidence only exists in images.