---
layout: publication
title: A Note On Efficient Privacy-preserving Similarity Search For Encrypted Vectors
authors: Dongfang Zhao
conference: Arxiv
year: 2025
bibkey: zhao2025a
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.14291'}]
tags: ["Efficiency", "Recommender Systems", "Similarity Search"]
short_authors: Dongfang Zhao
---
Traditional approaches to vector similarity search over encrypted data rely
on fully homomorphic encryption (FHE) to enable computation without decryption.
However, the substantial computational overhead of FHE makes it impractical for
large-scale real-time applications. This work explores a more efficient
alternative: using additively homomorphic encryption (AHE) for
privacy-preserving similarity search. We consider scenarios where either the
query vector or the database vectors remain encrypted, a setting that
frequently arises in applications such as confidential recommender systems and
secure federated learning. While AHE only supports addition and scalar
multiplication, we show that it is sufficient to compute inner product
similarity--one of the most widely used similarity measures in vector
retrieval. Compared to FHE-based solutions, our approach significantly reduces
computational overhead by avoiding ciphertext-ciphertext multiplications and
bootstrapping, while still preserving correctness and privacy. We present an
efficient algorithm for encrypted similarity search under AHE and analyze its
error growth and security implications. Our method provides a scalable and
practical solution for privacy-preserving vector search in real-world machine
learning applications.