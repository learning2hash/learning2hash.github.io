---
layout: publication
title: 'Logical Consistency Is Vital: Neural-symbolic Information Retrieval For Negative-constraint
  Queries'
authors: Ganlin Xu, Zhoujia Zhang, Wangyi Mei, Jiaqing Liang, Weijia Lu, Xiaodong
  Zhang, Zhifei Yang, Xiaofeng Ma, Yanghua Xiao, Deqing Yang
conference: 'Findings of the Association for Computational Linguistics: ACL 2025'
year: 2025
bibkey: xu2025logical
citations: 0
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2505.22299'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Re-Ranking"]
short_authors: Xu et al.
---
Information retrieval plays a crucial role in resource localization. Current dense retrievers retrieve the relevant documents within a corpus via embedding similarities, which compute similarities between dense vectors mainly depending on word co-occurrence between queries and documents, but overlook the real query intents.
  Thus, they often retrieve numerous irrelevant documents. Particularly in the scenarios of complex queries such as *negative-constraint queries*, their retrieval performance could be catastrophic. To address the issue, we propose a neuro-symbolic information retrieval method, namely \textbf\{NS-IR\}, that leverages first-order logic (FOL) to optimize the embeddings of naive natural language by considering the *logical consistency* between queries and documents. Specifically, we introduce two novel techniques, *logic alignment* and *connective constraint*, to rerank candidate documents, thereby enhancing retrieval relevance.
  Furthermore, we construct a new dataset \textbf\{NegConstraint\} including negative-constraint queries to evaluate our NS-IR's performance on such complex IR scenarios.
  Our extensive experiments demonstrate that NS-IR not only achieves superior zero-shot retrieval performance on web search and low-resource retrieval tasks, but also performs better on negative-constraint queries. Our scource code and dataset are available at https://github.com/xgl-git/NS-IR-main.