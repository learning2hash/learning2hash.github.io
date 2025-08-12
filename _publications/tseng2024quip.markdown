---
layout: publication
title: 'Quip#: Even Better LLM Quantization With Hadamard Incoherence And Lattice
  Codebooks'
authors: Albert Tseng, Jerry Chee, Qingyao Sun, Volodymyr Kuleshov, Christopher de
  Sa
conference: Arxiv
year: 2024
bibkey: tseng2024quip
citations: 0
additional_links: [{name: Code, url: 'https://github.com/Cornell-RelaxML/quip-sharp'},
  {name: Paper, url: 'https://arxiv.org/abs/2402.04396'}]
tags: ["Quantization"]
short_authors: Tseng et al.
---
Post-training quantization (PTQ) reduces the memory footprint of LLMs by
quantizing their weights to low-precision. In this work, we introduce QuIP\#, a
weight-only PTQ method that achieves state-of-the-art results in extreme
compression regimes (\(\le\) 4 bits per weight) using three novel techniques.
First, QuIP\# improves QuIP's (Chee et al., 2023) incoherence processing by
using the randomized Hadamard transform, which is faster and has better
theoretical properties. Second, QuIP\# uses vector quantization to take
advantage of the ball-shaped sub-Gaussian distribution that incoherent weights
possess: specifically, we introduce a set of hardware-efficient codebooks based
on the highly symmetric \(E_8\) lattice, which achieves the optimal 8-dimension
unit ball packing. Third, QuIP\# uses fine-tuning to improve fidelity to the
original model. Our experiments show that QuIP\# outperforms existing PTQ
methods, enables new behaviors in PTQ scaling, and supports fast inference. Our
code can be found at https://github.com/Cornell-RelaxML/quip-sharp.