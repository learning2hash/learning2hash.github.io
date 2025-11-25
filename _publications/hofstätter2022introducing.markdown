---
layout: publication
title: 'Introducing Neural Bag Of Whole-words With Colberter: Contextualized Late
  Interactions Using Enhanced Reduction'
authors: "Sebastian Hofst\xE4tter, Omar Khattab, Sophia Althammer, Mete Sertkan, Allan\
  \ Hanbury"
conference: Arxiv
year: 2022
bibkey: "hofst\xE4tter2022introducing"
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.13088'}]
tags: ["Efficiency", "Robustness", "Text Retrieval"]
short_authors: "Hofst\xE4tter et al."
---
Recent progress in neural information retrieval has demonstrated large gains
in effectiveness, while often sacrificing the efficiency and interpretability
of the neural model compared to classical approaches. This paper proposes
ColBERTer, a neural retrieval model using contextualized late interaction
(ColBERT) with enhanced reduction. Along the effectiveness Pareto frontier,
ColBERTer's reductions dramatically lower ColBERT's storage requirements while
simultaneously improving the interpretability of its token-matching scores. To
this end, ColBERTer fuses single-vector retrieval, multi-vector refinement, and
optional lexical matching components into one model. For its multi-vector
component, ColBERTer reduces the number of stored vectors per document by
learning unique whole-word representations for the terms in each document and
learning to identify and remove word representations that are not essential to
effective scoring. We employ an explicit multi-task, multi-stage training to
facilitate using very small vector dimensions. Results on the MS MARCO and
TREC-DL collection show that ColBERTer can reduce the storage footprint by up
to 2.5x, while maintaining effectiveness. With just one dimension per token in
its smallest setting, ColBERTer achieves index storage parity with the
plaintext size, with very strong effectiveness results. Finally, we demonstrate
ColBERTer's robustness on seven high-quality out-of-domain collections,
yielding statistically significant gains over traditional retrieval baselines.