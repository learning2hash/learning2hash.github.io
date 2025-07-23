---
layout: publication
title: 'Magicpig: LSH Sampling For Efficient LLM Generation'
authors: Chen Zhuoming, Sadhukhan Ranajoy, Ye Zihao, Zhou Yang, Zhang Jianyu, Nolte
  Niklas, Tian Yuandong, Douze Matthijs, Bottou Leon, Jia Zhihao, Chen Beidi
conference: Arxiv
year: 2024
bibkey: chen2024magicpig
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.16179'}]
tags: ["Efficiency", "Hashing Methods", "Locality Sensitive Hashing", "Scalability"]
short_authors: Chen et al.
---
Large language models (LLMs) with long context windows have gained
significant attention. However, the KV cache, stored to avoid re-computation,
becomes a bottleneck. Various dynamic sparse or TopK-based attention
approximation methods have been proposed to leverage the common insight that
attention is sparse. In this paper, we first show that TopK attention itself
suffers from quality degradation in certain downstream tasks because attention
is not always as sparse as expected. Rather than selecting the keys and values
with the highest attention scores, sampling with theoretical guarantees can
provide a better estimation for attention output. To make the sampling-based
approximation practical in LLM generation, we propose MagicPIG, a heterogeneous
system based on Locality Sensitive Hashing (LSH). MagicPIG significantly
reduces the workload of attention computation while preserving high accuracy
for diverse tasks. MagicPIG stores the LSH hash tables and runs the attention
computation on the CPU, which allows it to serve longer contexts and larger
batch sizes with high approximation accuracy. MagicPIG can improve decoding
throughput by up to \\(5\times\\) across various GPU hardware and achieve 54ms
decoding latency on a single RTX 4090 for Llama-3.1-8B-Instruct model with a
context of 96k tokens. The code is available at
https://github.com/Infini-AI-Lab/MagicPIG.