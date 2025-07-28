---
layout: publication
title: 'GLEN: Generative Retrieval Via Lexical Index Learning'
authors: Sunkyung Lee, Minjin Choi, Jongwuk Lee
conference: Proceedings of the 2023 Conference on Empirical Methods in Natural Language
  Processing
year: 2023
bibkey: lee2023glen
citations: 3
additional_links: [{name: Code, url: 'https://github.com/skleee/GLEN'}, {name: Paper,
    url: 'https://arxiv.org/abs/2311.03057'}]
tags: ["EMNLP", "Text Retrieval", "Vector Indexing"]
short_authors: Sunkyung Lee, Minjin Choi, Jongwuk Lee
---
Generative retrieval shed light on a new paradigm of document retrieval, aiming to directly generate the identifier of a relevant document for a query. While it takes advantage of bypassing the construction of auxiliary index structures, existing studies face two significant challenges: (i) the discrepancy between the knowledge of pre-trained language models and identifiers and (ii) the gap between training and inference that poses difficulty in learning to rank. To overcome these challenges, we propose a novel generative retrieval method, namely Generative retrieval via LExical iNdex learning (GLEN). For training, GLEN effectively exploits a dynamic lexical identifier using a two-phase index learning strategy, enabling it to learn meaningful lexical identifiers and relevance signals between queries and documents. For inference, GLEN utilizes collision-free inference, using identifier weights to rank documents without additional overhead. Experimental results prove that GLEN achieves state-of-the-art or competitive performance against existing generative retrieval methods on various benchmark datasets, e.g., NQ320k, MS MARCO, and BEIR. The code is available at https://github.com/skleee/GLEN.