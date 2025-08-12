---
layout: publication
title: 'Hikonv: High Throughput Quantized Convolution With Novel Bit-wise Management
  And Computation'
authors: Xinheng Liu, Yao Chen, Prakhar Ganesh, Junhao Pan, Jinjun Xiong, Deming Chen
conference: 2022 27th Asia and South Pacific Design Automation Conference (ASP-DAC)
year: 2022
bibkey: liu2021hikonv
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.13972'}]
tags: ["Efficiency", "Quantization"]
short_authors: Liu et al.
---
Quantization for Convolutional Neural Network (CNN) has shown significant
progress with the intention of reducing the cost of computation and storage
with low-bitwidth data inputs. There are, however, no systematic studies on how
an existing full-bitwidth processing unit, such as CPUs and DSPs, can be better
utilized to carry out significantly higher computation throughput for
convolution under various quantized bitwidths. In this study, we propose
HiKonv, a unified solution that maximizes the compute throughput of a given
underlying processing unit to process low-bitwidth quantized data inputs
through novel bit-wise parallel computation. We establish theoretical
performance bounds using a full-bitwidth multiplier for highly parallelized
low-bitwidth convolution, and demonstrate new breakthroughs for
high-performance computing in this critical domain. For example, a single
32-bit processing unit can deliver 128 binarized convolution operations
(multiplications and additions) under one CPU instruction, and a single 27x18
DSP core can deliver eight convolution operations with 4-bit inputs in one
cycle. We demonstrate the effectiveness of HiKonv on CPU and FPGA for both
convolutional layers or a complete DNN model. For a convolutional layer
quantized to 4-bit, HiKonv achieves a 3.17x latency improvement over the
baseline implementation using C++ on CPU. Compared to the DAC-SDC 2020 champion
model for FPGA, HiKonv achieves a 2.37x throughput improvement and 2.61x DSP
efficiency improvement, respectively.