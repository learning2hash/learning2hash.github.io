---
layout: publication
title: Llm-assisted Vector Similarity Search
authors: Riyadh Md, Li Muqi, Lie Felix Haryanto, Loh Jia Long, Mi Haotian, Bohra Sayam
conference: Arxiv
year: 2024
bibkey: riyadh2024llm
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.18819'}]
tags: ["Efficiency", "Similarity-Search", "Datasets"]
short_authors: Riyadh et al.
---
As data retrieval demands become increasingly complex, traditional search
methods often fall short in addressing nuanced and conceptual queries. Vector
similarity search has emerged as a promising technique for finding semantically
similar information efficiently. However, its effectiveness diminishes when
handling intricate queries with contextual nuances. This paper explores a
hybrid approach combining vector similarity search with Large Language Models
(LLMs) to enhance search accuracy and relevance. The proposed two-step solution
first employs vector similarity search to shortlist potential matches, followed
by an LLM for context-aware ranking of the results. Experiments on structured
datasets demonstrate that while vector similarity search alone performs well
for straightforward queries, the LLM-assisted approach excels in processing
complex queries involving constraints, negations, or conceptual requirements.
By leveraging the natural language understanding capabilities of LLMs, this
method improves the accuracy of search results for complex tasks without
sacrificing efficiency. We also discuss real-world applications and propose
directions for future research to refine and scale this technique for diverse
datasets and use cases.
  Original article:
https://engineering.grab.com/llm-assisted-vector-similarity-search