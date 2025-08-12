---
layout: publication
title: 'MUVERA: Multi-vector Retrieval Via Fixed Dimensional Encodings'
authors: Laxman Dhulipala, Majid Hadian, Rajesh Jayaram, Jason Lee, Vahab Mirrokni
conference: Arxiv
year: 2024
bibkey: dhulipala2024muvera
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.19504'}]
tags: ["Similarity Search"]
short_authors: Dhulipala et al.
---
Neural embedding models have become a fundamental component of modern
information retrieval (IR) pipelines. These models produce a single embedding
\(x \in \mathbb\{R\}^d\) per data-point, allowing for fast retrieval via highly
optimized maximum inner product search (MIPS) algorithms. Recently, beginning
with the landmark ColBERT paper, multi-vector models, which produce a set of
embedding per data point, have achieved markedly superior performance for IR
tasks. Unfortunately, using these models for IR is computationally expensive
due to the increased complexity of multi-vector retrieval and scoring.
  In this paper, we introduce MUVERA (MUlti-VEctor Retrieval Algorithm), a
retrieval mechanism which reduces multi-vector similarity search to
single-vector similarity search. This enables the usage of off-the-shelf MIPS
solvers for multi-vector retrieval. MUVERA asymmetrically generates Fixed
Dimensional Encodings (FDEs) of queries and documents, which are vectors whose
inner product approximates multi-vector similarity. We prove that FDEs give
high-quality \(\epsilon\)-approximations, thus providing the first single-vector
proxy for multi-vector similarity with theoretical guarantees. Empirically, we
find that FDEs achieve the same recall as prior state-of-the-art heuristics
while retrieving 2-5\(\times\) fewer candidates. Compared to prior state of the
art implementations, MUVERA achieves consistently good end-to-end recall and
latency across a diverse set of the BEIR retrieval datasets, achieving an
average of 10\(%\) improved recall with \(90%\) lower latency.