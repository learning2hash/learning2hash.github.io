---
layout: publication
title: 'Coret: Improved Retriever For Code Editing'
authors: Fabio Fehr, Prabhu Teja Sivaprasad, Luca Franceschi, Giovanni Zappella
conference: 'Proceedings of the 63rd Annual Meeting of the Association for Computational
  Linguistics (Volume 2: Short Papers)'
year: 2025
bibkey: fehr2025coret
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.24715'}]
tags: ["Datasets", "Evaluation"]
short_authors: Fehr et al.
---
In this paper, we introduce CoRet, a dense retrieval model designed for code-editing tasks that integrates code semantics, repository structure, and call graph dependencies. The model focuses on retrieving relevant portions of a code repository based on natural language queries such as requests to implement new features or fix bugs. These retrieved code chunks can then be presented to a user or to a second code-editing model or agent. To train CoRet, we propose a loss function explicitly designed for repository-level retrieval. On SWE-bench and Long Code Arena's bug localisation datasets, we show that our model substantially improves retrieval recall by at least 15 percentage points over existing models, and ablate the design choices to show their importance in achieving these results.