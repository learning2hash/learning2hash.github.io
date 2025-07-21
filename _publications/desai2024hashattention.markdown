---
layout: publication
title: 'Hashattention: Semantic Sparsity For Faster Inference'
authors: Desai et al.
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: desai2024hashattention
citations: 129
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.14468'}]
tags: ["CVPR"]
---
Leveraging long contexts is crucial for advanced AI systems, but attention computation poses a scalability challenge. While scaled dot-product attention (SDPA) exhibits token sparsity, i.e. only a few pivotal tokens significantly contribute to output, exploiting this sparsity remains challenging. Existing methods either suffer from quality degradation or require substantial additional resources. We show that identifying pivotal tokens is a Maximum Inner Product Search (MIPS) problem. However, existing MIPS solutions are not well-suited for SDPA, as they are not GPU-friendly and often underperform due to the separated query and key distributions. This paper introduces HashAttention, framing pivotal token identification as a recommendation problem. Given a query, HashAttention encodes keys and queries in Hamming space, capturing the required semantic similarity, using learned mapping functions. HashAttention efficiently identifies pivotal tokens for a given query using bitwise operations and computes attention using only these tokens, improving the overall attention efficiency. Trained on generic data, HashAttention reduces tokens used by up to \\(16\times\\) with minimal quality loss, requiring only 32 bits of auxiliary memory per token. Sparsity can be further improved to \\(32\times\\) through task-specific fine-tuning. On A100 GPU, at \\(32\times\\) sparsity, incorporating HashAttention reduces attention latency by up to \\(4.3\times\\) in GPT-FAST and \\(2.54\times\\) in FlashDecode, and achieves up to \\(3.12\times\\) higher throughput for GPT-FAST.