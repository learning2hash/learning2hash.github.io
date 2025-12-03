---
layout: publication
title: Unified Semantic And ID Representation Learning For Deep Recommenders
authors: Guanyu Lin, Zhigang Hua, Tao Feng, Shuang Yang, Bo Long, Jiaxuan You
conference: Arxiv
year: 2025
bibkey: lin2025unified
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.16474'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Recommender Systems", "Tools & Libraries"]
short_authors: Lin et al.
---
Effective recommendation is crucial for large-scale online platforms.
Traditional recommendation systems primarily rely on ID tokens to uniquely
identify items, which can effectively capture specific item relationships but
suffer from issues such as redundancy and poor performance in cold-start
scenarios. Recent approaches have explored using semantic tokens as an
alternative, yet they face challenges, including item duplication and
inconsistent performance gains, leaving the potential advantages of semantic
tokens inadequately examined. To address these limitations, we propose a
Unified Semantic and ID Representation Learning framework that leverages the
complementary strengths of both token types. In our framework, ID tokens
capture unique item attributes, while semantic tokens represent shared,
transferable characteristics. Additionally, we analyze the role of cosine
similarity and Euclidean distance in embedding search, revealing that cosine
similarity is more effective in decoupling accumulated embeddings, while
Euclidean distance excels in distinguishing unique items. Our framework
integrates cosine similarity in earlier layers and Euclidean distance in the
final layer to optimize representation learning. Experiments on three benchmark
datasets show that our method significantly outperforms state-of-the-art
baselines, with improvements ranging from 6% to 17% and a reduction in token
size by over 80%. These results demonstrate the effectiveness of combining ID
and semantic tokenization to enhance the generalization ability of recommender
systems.