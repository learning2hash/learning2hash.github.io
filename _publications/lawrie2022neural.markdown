---
layout: publication
title: Neural Approaches To Multilingual Information Retrieval
authors: Dawn Lawrie, Eugene Yang, Douglas W. Oard, James Mayfield
conference: Arxiv
year: 2022
bibkey: lawrie2022neural
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.01335'}]
tags: ["Evaluation"]
short_authors: Lawrie et al.
---
Providing access to information across languages has been a goal of
Information Retrieval (IR) for decades. While progress has been made on Cross
Language IR (CLIR) where queries are expressed in one language and documents in
another, the multilingual (MLIR) task to create a single ranked list of
documents across many languages is considerably more challenging. This paper
investigates whether advances in neural document translation and pretrained
multilingual neural language models enable improvements in the state of the art
over earlier MLIR techniques. The results show that although combining neural
document translation with neural ranking yields the best Mean Average Precision
(MAP), 98% of that MAP score can be achieved with an 84% reduction in indexing
time by using a pretrained XLM-R multilingual language model to index documents
in their native language, and that 2% difference in effectiveness is not
statistically significant. Key to achieving these results for MLIR is to
fine-tune XLM-R using mixed-language batches from neural translations of MS
MARCO passages.