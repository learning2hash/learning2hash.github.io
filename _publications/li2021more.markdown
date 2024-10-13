---
layout: publication
title: More Robust Dense Retrieval With Contrastive Dual Learning
authors: Li Yizhi, Liu Zhenghao, Xiong Chenyan, Liu Zhiyuan
conference: "Arxiv"
year: 2021
bibkey: li2021more
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2107.07773"}
  - {name: "Code", url: "https://github.com/thunlp/DANCE"}
tags: ['ARXIV', 'Has Code', 'Self Supervised', 'Text Retrieval']
---
<p>Dense retrieval conducts text retrieval in the embedding space and
has shown many advantages compared to sparse retrieval. Existing dense
retrievers optimize representations of queries and documents with
contrastive training and map them to the embedding space. The embedding
space is optimized by aligning the matched query-document pairs and
pushing the negative documents away from the query. However, in such
training paradigm, the queries are only optimized to align to the
documents and are coarsely positioned, leading to an anisotropic query
embedding space. In this paper, we analyze the embedding space
distributions and propose an effective training paradigm, Contrastive
Dual Learning for Approximate Nearest Neighbor (DANCE) to learn
fine-grained query representations for dense retrieval. DANCE
incorporates an additional dual training object of query retrieval,
inspired by the classic information retrieval training axiom, query
likelihood. With contrastive learning, the dual training object of DANCE
learns more tailored representations for queries and documents to keep
the embedding space smooth and uniform, thriving on the ranking
performance of DANCE on the MS MARCO document retrieval task. Different
from ANCE that only optimized with the document retrieval task, DANCE
concentrates the query embeddings closer to document representations
while making the document distribution more discriminative. Such
concentrated query embedding distribution assigns more uniform negative
sampling probabilities to queries and helps to sufficiently optimize
query representations in the query retrieval task. Our codes are
released at https://github.com/thunlp/DANCE.</p>
