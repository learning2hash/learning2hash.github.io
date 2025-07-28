---
layout: publication
title: 'JAMES: Normalizing Job Titles With Multi-aspect Graph Embeddings And Reasoning'
authors: Michiharu Yamashita, Jia Tracy Shen, Thanh Tran, Hamoon Ekhtiari, Dongwon
  Lee
conference: 2023 IEEE 10th International Conference on Data Science and Advanced Analytics
  (DSAA)
year: 2023
bibkey: yamashita2022james
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.10739'}]
tags: []
short_authors: Yamashita et al.
---
In online job marketplaces, it is important to establish a well-defined job
title taxonomy for various downstream tasks (e.g., job recommendation, users'
career analysis, and turnover prediction). Job Title Normalization (JTN) is
such a cleaning step to classify user-created non-standard job titles into
normalized ones. However, solving the JTN problem is non-trivial with
challenges: (1) semantic similarity of different job titles, (2) non-normalized
user-created job titles, and (3) large-scale and long-tailed job titles in
real-world applications. To this end, we propose a novel solution, named JAMES,
that constructs three unique embeddings (i.e., graph, contextual, and
syntactic) of a target job title to effectively capture its various traits. We
further propose a multi-aspect co-attention mechanism to attentively combine
these embeddings, and employ neural logical reasoning representations to
collaboratively estimate similarities between messy job titles and normalized
job titles in a reasoning space. To evaluate JAMES, we conduct comprehensive
experiments against ten competing models on a large-scale real-world dataset
with over 350,000 job titles. Our experimental results show that JAMES
significantly outperforms the best baseline by 10.06% in Precision@10 and by
17.52% in NDCG@10, respectively.