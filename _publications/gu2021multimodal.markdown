---
layout: publication
title: Multimodal Representation For Neural Code Search
authors: Gu Jian, Chen Zimin, Monperrus Martin
conference: 2021 IEEE International Conference on Software Maintenance and Evolution
  (ICSME)
year: 2021
bibkey: gu2021multimodal
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.00992'}]
---
Semantic code search is about finding semantically relevant code snippets for
a given natural language query. In the state-of-the-art approaches, the
semantic similarity between code and query is quantified as the distance of
their representation in the shared vector space. In this paper, to improve the
vector space, we introduce tree-serialization methods on a simplified form of
AST and build the multimodal representation for the code data. We conduct
extensive experiments using a single corpus that is large-scale and
multi-language: CodeSearchNet. Our results show that both our tree-serialized
representations and multimodal learning model improve the performance of code
search. Last, we define intuitive quantification metrics oriented to the
completeness of semantic and syntactic information of the code data, to help
understand the experimental findings.