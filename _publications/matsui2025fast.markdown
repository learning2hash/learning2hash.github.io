---
layout: publication
title: 'Lotusfilter: Fast Diverse Nearest Neighbor Search Via A Learned Cutoff Table'
authors: Yusuke Matsui
conference: "Arxiv"
year: 2025
citations: 0
bibkey: matsui2025fast
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2506.04790'}
  - {name: "Code", url: 'https://github.com/matsui528/lotf'}
tags: ['ANN Search', 'Has Code', 'Applications', 'Approximate Nearest Neighbor Search']
---
Approximate nearest neighbor search (ANNS) is an essential building block for applications like RAG but can sometimes yield results that are overly similar to each other. In certain scenarios, search results should be similar to the query and yet diverse. We propose LotusFilter, a post-processing module to diversify ANNS results. We precompute a cutoff table summarizing vectors that are close to each other. During the filtering, LotusFilter greedily looks up the table to delete redundant vectors from the candidates. We demonstrated that the LotusFilter operates fast (0.02 [ms/query]) in settings resembling real-world RAG applications, utilizing features such as OpenAI embeddings. Our code is publicly available at https://github.com/matsui528/lotf.
