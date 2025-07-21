---
layout: publication
title: Learning to Hash with a Dimension Analysis-based Quantizer for Image Retrieval
authors: Kwok Yuan
conference: IEEE Transactions on Multimedia
year: 2020
bibkey: kwok2025learning
citations: 10
additional_links: [{name: Paper, url: 'https://ieeexplore.ieee.org/document/9238437'}]
tags: ["Hashing-Methods", "Image-Retrieval"]
---
The last few years have witnessed the rise of the big data era in which approximate nearest neighbor search is a fundamental problem in many applications, such as large-scale image retrieval. Recently, many research results have demonstrated that hashing can achieve promising performance due to its appealing storage and search efficiency. Since complex optimization problems for loss functions are difficult to solve, most hashing methods decompose the hash code learning problem into two steps: projection and quantization. In the quantization step, binary codes are widely used because ranking them by the Hamming distance is very efficient. However, the massive information loss produced by the quantization step should be reduced in applications where high search accuracy is required, such as in image retrieval. Since many two-step hashing methods produce uneven projected dimensions in the projection step, in this paper, we propose a novel dimension analysis-based quantization (DAQ) on two-step hashing methods for image retrieval. We first perform an importance analysis of the projected dimensions and select a subset of them that are more informative than others, and then we divide the selected projected dimensions into several regions with our quantizer. Every region is quantized with its corresponding codebook. Finally, the similarity between two hash codes is estimated by the Manhattan distance between their corresponding codebooks, which is also efficient. We conduct experiments on three public benchmarks containing up to one million descriptors and show that the proposed DAQ method consistently leads to significant accuracy improvements over state-of-the-art quantization methods.