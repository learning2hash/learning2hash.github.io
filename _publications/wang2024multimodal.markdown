---
layout: publication
title: 'Multimodal Needle In A Haystack: Benchmarking Long-context Capability Of Multimodal
  Large Language Models'
authors: Hengyi Wang, Haizhou Shi, Shiwei Tan, Weiyi Qin, Wenyuan Wang, Tunyu Zhang,
  Akshay Nambi, Tanuja Ganu, Hao Wang
conference: Arxiv
year: 2024
bibkey: wang2024multimodal
citations: 1
additional_links: [{name: Code, url: 'https://github.com/Wang-ML-Lab/multimodal-needle-in-a-haystack'},
  {name: Paper, url: 'https://arxiv.org/abs/2406.11230'}]
tags: ["Evaluation"]
short_authors: Wang et al.
---
Multimodal Large Language Models (MLLMs) have shown significant promise in
various applications, leading to broad interest from researchers and
practitioners alike. However, a comprehensive evaluation of their long-context
capabilities remains underexplored. To address these gaps, we introduce the
MultiModal Needle-in-a-haystack (MMNeedle) benchmark, specifically designed to
assess the long-context capabilities of MLLMs. Besides multi-image input, we
employ image stitching to further increase the input context length, and
develop a protocol to automatically generate labels for sub-image level
retrieval. Essentially, MMNeedle evaluates MLLMs by stress-testing their
capability to locate a target sub-image (needle) within a set of images
(haystack) based on textual instructions and descriptions of image contents.
This setup necessitates an advanced understanding of extensive visual contexts
and effective information retrieval within long-context image inputs. With this
benchmark, we evaluate state-of-the-art MLLMs, encompassing both API-based and
open-source models. The findings reveal that GPT-4o consistently surpasses
other models in long-context scenarios, but suffers from hallucination problems
in negative samples, i.e., when needles are not in the haystacks. Our
comprehensive long-context evaluation of MLLMs also sheds lights on the
considerable performance gap between API-based and open-source models. All the
code, data, and instructions required to reproduce the main results are
available at https://github.com/Wang-ML-Lab/multimodal-needle-in-a-haystack.