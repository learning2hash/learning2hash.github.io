---
layout: publication
title: Dataset Protection Via Watermarked Canaries In Retrieval-augmented Llms
authors: Yepeng Liu, Xuandong Zhao, Dawn Song, Yuheng Bu
conference: Arxiv
year: 2025
bibkey: liu2025dataset
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.10673'}]
tags: ["Datasets"]
short_authors: Liu et al.
---
Retrieval-Augmented Generation (RAG) has become an effective method for
enhancing large language models (LLMs) with up-to-date knowledge. However, it
poses a significant risk of IP infringement, as IP datasets may be incorporated
into the knowledge database by malicious Retrieval-Augmented LLMs (RA-LLMs)
without authorization. To protect the rights of the dataset owner, an effective
dataset membership inference algorithm for RA-LLMs is needed. In this work, we
introduce a novel approach to safeguard the ownership of text datasets and
effectively detect unauthorized use by the RA-LLMs. Our approach preserves the
original data completely unchanged while protecting it by inserting
specifically designed canary documents into the IP dataset. These canary
documents are created with synthetic content and embedded watermarks to ensure
uniqueness, stealthiness, and statistical provability. During the detection
process, unauthorized usage is identified by querying the canary documents and
analyzing the responses of RA-LLMs for statistical evidence of the embedded
watermark. Our experimental results demonstrate high query efficiency,
detectability, and stealthiness, along with minimal perturbation to the
original dataset, all without compromising the performance of the RAG system.