---
layout: publication
title: 'Im2win: An Efficient Convolution Paradigm On GPU'
authors: Shuai Lu, Jun Chu, Luanzheng Guo, Xu T. Liu
conference: Arxiv
year: 2023
bibkey: lu2023im2win
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.14316'}]
tags: ["Memory Efficiency"]
short_authors: Lu et al.
---
Convolution is the most time-consuming operation in deep neural network
operations, so its performance is critical to the overall performance of the
neural network. The commonly used methods for convolution on GPU include the
general matrix multiplication (GEMM)-based convolution and the direct
convolution. GEMM-based convolution relies on the im2col algorithm, which
results in a large memory footprint and reduced performance. Direct convolution
does not have the large memory footprint problem, but the performance is not on
par with GEMM-based approach because of the discontinuous memory access. This
paper proposes a window-order-based convolution paradigm on GPU, called im2win,
which not only reduces memory footprint but also offers continuous memory
accesses, resulting in improved performance. Furthermore, we apply a range of
optimization techniques on the convolution CUDA kernel, including shared
memory, tiling, micro-kernel, double buffer, and prefetching. We compare our
implementation with the direct convolution, and PyTorch's GEMM-based
convolution with cuBLAS and six cuDNN-based convolution implementations, with
twelve state-of-the-art DNN benchmarks. The experimental results show that our
implementation 1) uses less memory footprint by 23.1% and achieves 3.5\(\times\)
TFLOPS compared with cuBLAS, 2) uses less memory footprint by 32.8% and
achieves up to 1.8\(\times\) TFLOPS compared with the best performant
convolutions in cuDNN, and 3) achieves up to 155\(\times\) TFLOPS compared with
the direct convolution. We further perform an ablation study on the applied
optimization techniques and find that the micro-kernel has the greatest
positive impact on performance.