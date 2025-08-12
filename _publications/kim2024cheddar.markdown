---
layout: publication
title: 'Cheddar: A Swift Fully Homomorphic Encryption Library For CUDA Gpus'
authors: Jongmin Kim, Wonseok Choi, Jung Ho Ahn
conference: Arxiv
year: 2024
bibkey: kim2024cheddar
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.13055'}]
tags: ["Tools & Libraries"]
short_authors: Jongmin Kim, Wonseok Choi, Jung Ho Ahn
---
Fully homomorphic encryption (FHE) is a cryptographic technology capable of
resolving security and privacy problems in cloud computing by encrypting data
in use. However, FHE introduces tremendous computational overhead for
processing encrypted data, causing FHE workloads to become 2-6 orders of
magnitude slower than their unencrypted counterparts. To mitigate the overhead,
we propose Cheddar, an FHE library for CUDA GPUs, which demonstrates
significantly faster performance compared to prior GPU implementations. We
develop optimized functionalities at various implementation levels ranging from
efficient low-level primitives to streamlined high-level operational sequences.
Especially, we improve major FHE operations, including number-theoretic
transform and base conversion, based on efficient kernel designs using a small
word size of 32 bits. By these means, Cheddar demonstrates 2.9 to 25.6 times
higher performance for representative FHE workloads compared to prior GPU
implementations.