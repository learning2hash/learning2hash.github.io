---
layout: publication
title: 'SORCE: Small Object Retrieval In Complex Environments'
authors: Chunxu Liu et al.
conference: "Arxiv"
year: 2025
citations: 0
bibkey: liu2025small
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2505.24441'}
tags: ['Cross-Modal', 'Deep', 'Quantisation', 'Retrieval Models', 'Applications']
---
Text-to-Image Retrieval (T2IR) is a highly valuable task that aims to match a given textual query to images in a gallery. Existing benchmarks primarily focus on textual queries describing overall image semantics or foreground salient objects, possibly overlooking inconspicuous small objects, especially in complex environments. Such small object retrieval is crucial, as in real-world applications, the targets of interest are not always prominent in the image. Thus, we introduce SORCE (Small Object Retrieval in Complex Environments), a new subfield of T2IR, focusing on retrieving small objects in complex images with textual queries. We propose a new benchmark, SORCE-1K, consisting of images with complex environments and textual queries describing less conspicuous small objects with minimal contextual cues from other salient objects. Preliminary analysis on SORCE-1K finds that existing T2IR methods struggle to capture small objects and encode all the semantics into a single embedding, leading to poor retrieval performance on SORCE-1K. Therefore, we propose to represent each image with multiple distinctive embeddings. We leverage Multimodal Large Language Models (MLLMs) to extract multiple embeddings for each image instructed by a set of Regional Prompts (ReP). Experimental results show that our multi-embedding approach through MLLM and ReP significantly outperforms existing T2IR methods on SORCE-1K. Our experiments validate the effectiveness of SORCE-1K for benchmarking SORCE performances, highlighting the potential of multi-embedding representation and text-customized MLLM features for addressing this task.
