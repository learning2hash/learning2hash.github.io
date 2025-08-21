---
layout: publication
title: 'QLESS: A Quantized Approach For Data Valuation And Selection In Large Language
  Model Fine-tuning'
authors: Moses Ananta, Muhammad Farid Adilazuarda, Zayd Muhammad Kawakibi Zuhri, Ayu
  Purwarianti, Alham Fikri Aji
conference: Arxiv
year: 2025
bibkey: ananta2025qless
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.01703'}]
tags: ["Datasets", "Evaluation", "Locality-Sensitive-Hashing", "Memory Efficiency", "Quantization", "Similarity Search", "Tools & Libraries"]
short_authors: Ananta et al.
---
Fine-tuning large language models (LLMs) is often constrained by the
computational costs of processing massive datasets. We propose \textbf\{QLESS\}
(Quantized Low-rank Gradient Similarity Search), which integrates gradient
quantization with the LESS framework to enable memory-efficient data valuation
and selection. QLESS employs a two-step compression process: first, it obtains
low-dimensional gradient representations through LoRA-based random projection;
then, it quantizes these gradients to low-bitwidth representations. Experiments
on multiple LLM architectures (LLaMA, Mistral, Qwen) and benchmarks (MMLU, BBH,
TyDiQA) show that QLESS achieves comparable data selection performance to LESS
while reducing memory usage by up to 16x. Even 1-bit gradient quantization
preserves data valuation quality. These findings underscore QLESS as a
practical, scalable approach to identifying informative examples within strict
memory constraints.