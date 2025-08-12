---
layout: publication
title: 'Onesweep: A Faster Least Significant Digit Radix Sort For Gpus'
authors: Andy Adinets, Duane Merrill
conference: Arxiv
year: 2022
bibkey: adinets2022onesweep
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.01784'}]
tags: ["Efficiency"]
short_authors: Andy Adinets, Duane Merrill
---
We present Onesweep, a least-significant digit (LSD) radix sorting algorithm
for large GPU sorting problems residing in global memory. Our parallel
algorithm employs a method of single-pass prefix sum that only requires ~2n
global read/write operations for each digit-binning iteration. This exhibits a
significant reduction in last-level memory traffic versus contemporary GPU
radix sorting implementations, where each iteration of digit binning requires
two passes through the dataset totaling ~3n global memory operations.
  On the NVIDIA A100 GPU, our approach achieves 29.4 GKey/s when sorting 256M
random 32-bit keys. Compared to CUB, the current state-of-the-art GPU LSD radix
sort, our approach provides a speedup of ~1.5x. For 32-bit keys with varied
distributions, our approach provides more consistent performance compared to
HRS, the current state-of-the-art GPU MSD radix sort, and outperforms it in
almost all cases.