---
layout: publication
title: 'Hikonv: Maximizing The Throughput Of Quantized Convolution With Novel Bit-wise
  Management And Computation'
authors: Yao Chen, Junhao Pan, Xinheng Liu, Jinjun Xiong, Deming Chen
conference: Arxiv
year: 2022
bibkey: chen2022hikonv
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.00763'}]
tags: ["Efficiency", "Quantization"]
short_authors: Chen et al.
---
Quantization for CNN has shown significant progress with the intention of
reducing the cost of computation and storage with low-bitwidth data
representations. There are, however, no systematic studies on how an existing
full-bitwidth processing unit, such as ALU in CPUs and DSP in FPGAs, can be
better utilized to deliver significantly higher computation throughput for
convolution under various quantized bitwidths. In this study, we propose
HiKonv, a unified solution that maximizes the throughput of convolution on a
given underlying processing unit with low-bitwidth quantized data inputs
through novel bit-wise management and parallel computation. We establish
theoretical framework and performance models using a full-bitwidth multiplier
for highly parallelized low-bitwidth convolution, and demonstrate new
breakthroughs for high-performance computing in this critical domain. For
example, a single 32-bit processing unit in CPU can deliver 128 binarized
convolution operations (multiplications and additions) and 13 4-bit convolution
operations with a single multiplication instruction, and a single 27x18
multiplier in the FPGA DSP can deliver 60, 8 or 2 convolution operations with
1, 4 or 8-bit inputs in one clock cycle. We demonstrate the effectiveness of
HiKonv on both CPU and FPGA. On CPU, HiKonv outperforms the baseline
implementation with 1 to 8-bit inputs and provides up to 7.6x and 1.4x
performance improvements for 1-D convolution, and performs 2.74x and 3.19x over
the baseline implementation for 4-bit signed and unsigned data inputs for 2-D
convolution. On FPGA, HiKonv solution enables a single DSP to process multiple
convolutions with a shorter processing latency. For binarized input, each DSP
with HiKonv is equivalent up to 76.6 LUTs. Compared to the DAC-SDC 2020
champion model, HiKonv achieves a 2.37x throughput improvement and 2.61x DSP
efficiency improvement, respectively.