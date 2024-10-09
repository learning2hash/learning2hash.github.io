---
layout: publication
title: Quip 2-bit Quantization Of Large Language Models With Guarantees
authors: Jerry Chee, Yaohui Cai, Volodymyr Kuleshov, Christopher De Sa
conference: "Arxiv"
year: 2023
bibkey: chee2023quip
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2307.13304v2"}
  - {name: "Code", url: "https://github.com/Cornell-RelaxML/QuIP"}
tags: ['ARXIV', 'Has Code', 'Independent', 'Quantisation']
---
This work studies post-training parameter quantization in large language models (LLMs). We introduce quantization with incoherence processing (QuIP) a new method based on the insight that quantization benefits from () weight and Hessian matrices i.e. from the weights being even in magnitude and the directions in which it is important to round them accurately being unaligned with the coordinate axes. QuIP consists of two steps (1) an adaptive rounding procedure minimizing a quadratic proxy objective; (2) efficient pre- and post-processing that ensures weight and Hessian incoherence via multiplication by random orthogonal matrices. We complement QuIP with the first theoretical analysis for an LLM-scale quantization algorithm and show that our theory also applies to an existing method OPTQ. Empirically we find that our incoherence preprocessing improves several existing quantization algorithms and yields the first LLM quantization methods that produce viable results using only two bits per weight. Our code can be found at https://github.com/Cornell-RelaxML/QuIP.
