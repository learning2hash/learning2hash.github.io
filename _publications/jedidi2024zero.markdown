---
layout: publication
title: Zero-shot Dense Retrieval With Embeddings From Relevance Feedback
authors: Nour Jedidi, Yung-sung Chuang, Leslie Shing, James Glass
conference: Arxiv
year: 2024
bibkey: jedidi2024zero
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.21242'}]
tags: ["Datasets", "Few Shot & Zero Shot"]
short_authors: Jedidi et al.
---
Building effective dense retrieval systems remains difficult when relevance
supervision is not available. Recent work has looked to overcome this challenge
by using a Large Language Model (LLM) to generate hypothetical documents that
can be used to find the closest real document. However, this approach relies
solely on the LLM to have domain-specific knowledge relevant to the query,
which may not be practical. Furthermore, generating hypothetical documents can
be inefficient as it requires the LLM to generate a large number of tokens for
each query. To address these challenges, we introduce Real Document Embeddings
from Relevance Feedback (ReDE-RF). Inspired by relevance feedback, ReDE-RF
proposes to re-frame hypothetical document generation as a relevance estimation
task, using an LLM to select which documents should be used for nearest
neighbor search. Through this re-framing, the LLM no longer needs
domain-specific knowledge but only needs to judge what is relevant.
Additionally, relevance estimation only requires the LLM to output a single
token, thereby improving search latency. Our experiments show that ReDE-RF
consistently surpasses state-of-the-art zero-shot dense retrieval methods
across a wide range of low-resource retrieval datasets while also making
significant improvements in latency per-query.