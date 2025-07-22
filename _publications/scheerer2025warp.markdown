---
layout: publication
title: 'WARP: An Efficient Engine For Multi-vector Retrieval'
authors: Scheerer Jan Luca, Zaharia Matei, Potts Christopher, Alonso Gustavo, Khattab
  Omar
conference: Arxiv
year: 2025
bibkey: scheerer2025warp
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.17788'}]
tags: ["Efficiency"]
short_authors: Scheerer et al.
---
Multi-vector retrieval methods such as ColBERT and its recent variant, the ConteXtualized Token Retriever (XTR), offer high accuracy but face efficiency challenges at scale. To address this, we present WARP, a retrieval engine that substantially improves the efficiency of retrievers trained with the XTR objective through three key innovations: (1) WARP\\(_\text\{SELECT\}\\) for dynamic similarity imputation; (2) implicit decompression, avoiding costly vector reconstruction during retrieval; and (3) a two-stage reduction process for efficient score aggregation. Combined with highly-optimized C++ kernels, our system reduces end-to-end latency compared to XTR's reference implementation by 41x, and achieves a 3x speedup over the ColBERTv2/PLAID engine, while preserving retrieval quality.