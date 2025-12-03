---
layout: publication
title: 'Rare: Retrieval Augmented Retrieval With In-context Examples'
authors: Atula Tejaswi, Yoonsang Lee, Sujay Sanghavi, Eunsol Choi
conference: Arxiv
year: 2024
bibkey: tejaswi2024rare
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.20088'}]
tags: ["Datasets", "Evaluation"]
short_authors: Tejaswi et al.
---
We investigate whether in-context examples, widely used in decoder-only
language models (LLMs), can improve embedding model performance in retrieval
tasks. Unlike in LLMs, naively prepending in-context examples (query-document
pairs) to the target query at inference time does not work out of the box. We
introduce a simple approach to enable retrievers to use in-context examples.
Our approach, RARe, finetunes a pre-trained model with in-context examples
whose query is semantically similar to the target query. This can be applied to
adapt various base architectures (i.e., decoder-only language models, retriever
models) and consistently achieves performance gains of up to +2.72% nDCG across
various open-domain retrieval datasets (BeIR, RAR-b). In particular, we find
RARe exhibits stronger out-of-domain generalization compared to models using
queries without in-context examples, similar to what is seen for in-context
learning in LLMs. We further provide analysis on the design choices of
in-context example augmentation and lay the foundation for future work in this
space.