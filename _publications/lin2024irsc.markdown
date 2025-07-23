---
layout: publication
title: 'IRSC: A Zero-shot Evaluation Benchmark For Information Retrieval Through Semantic
  Comprehension In Retrieval-augmented Generation Scenarios'
authors: Lin Hai, Zhan Shaoxiong, Su Junyou, Zheng Haitao, Wang Hui
conference: Arxiv
year: 2024
bibkey: lin2024irsc
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.15763'}]
tags: ["Datasets", "Evaluation", "Few-shot & Zero-shot", "Text Retrieval"]
short_authors: Lin et al.
---
In Retrieval-Augmented Generation (RAG) tasks using Large Language Models
(LLMs), the quality of retrieved information is critical to the final output.
This paper introduces the IRSC benchmark for evaluating the performance of
embedding models in multilingual RAG tasks. The benchmark encompasses five
retrieval tasks: query retrieval, title retrieval, part-of-paragraph retrieval,
keyword retrieval, and summary retrieval. Our research addresses the current
lack of comprehensive testing and effective comparison methods for embedding
models in RAG scenarios. We introduced new metrics: the Similarity of Semantic
Comprehension Index (SSCI) and the Retrieval Capability Contest Index (RCCI),
and evaluated models such as Snowflake-Arctic, BGE, GTE, and M3E. Our
contributions include: 1) the IRSC benchmark, 2) the SSCI and RCCI metrics, and
3) insights into the cross-lingual limitations of embedding models. The IRSC
benchmark aims to enhance the understanding and development of accurate
retrieval systems in RAG tasks. All code and datasets are available at:
https://github.com/Jasaxion/IRSC_Benchmark