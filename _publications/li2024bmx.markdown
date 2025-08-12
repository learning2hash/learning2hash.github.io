---
layout: publication
title: 'BMX: Entropy-weighted Similarity And Semantic-enhanced Lexical Search'
authors: Xianming Li, Julius Lipp, Aamir Shakir, Rui Huang, Jing Li
conference: Arxiv
year: 2024
bibkey: li2024bmx
citations: 0
additional_links: [{name: Code, url: 'https://github.com/mixedbread-ai/baguetter'},
  {name: Paper, url: 'https://arxiv.org/abs/2408.06643'}]
tags: ["Evaluation"]
short_authors: Li et al.
---
BM25, a widely-used lexical search algorithm, remains crucial in information
retrieval despite the rise of pre-trained and large language models
(PLMs/LLMs). However, it neglects query-document similarity and lacks semantic
understanding, limiting its performance. We revisit BM25 and introduce BMX, a
novel extension of BM25 incorporating entropy-weighted similarity and semantic
enhancement techniques. Extensive experiments demonstrate that BMX consistently
outperforms traditional BM25 and surpasses PLM/LLM-based dense retrieval in
long-context and real-world retrieval benchmarks. This study bridges the gap
between classical lexical search and modern semantic approaches, offering a
promising direction for future information retrieval research. The reference
implementation of BMX can be found in Baguetter, which was created in the
context of this work. The code can be found here:
https://github.com/mixedbread-ai/baguetter.