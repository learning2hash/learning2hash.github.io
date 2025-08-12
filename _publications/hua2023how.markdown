---
layout: publication
title: How To Index Item Ids For Recommendation Foundation Models
authors: Wenyue Hua, Shuyuan Xu, Yingqiang Ge, Yongfeng Zhang
conference: Proceedings of the Annual International ACM SIGIR Conference on Research
  and Development in Information Retrieval in the Asia Pacific Region
year: 2023
bibkey: hua2023how
citations: 22
additional_links: [{name: Code, url: 'https://github.com/Wenyueh/LLM-RecSys-ID'},
  {name: Paper, url: 'https://arxiv.org/abs/2305.06569'}]
tags: ["Recommender Systems", "SIGIR"]
short_authors: Hua et al.
---
Recommendation foundation model utilizes large language models (LLM) for
recommendation by converting recommendation tasks into natural language tasks.
It enables generative recommendation which directly generates the item(s) to
recommend rather than calculating a ranking score for each and every candidate
item as in traditional recommendation models, simplifying the recommendation
pipeline from multi-stage filtering to single-stage filtering. To avoid
generating excessively long text and hallucinated recommendations when deciding
which item(s) to recommend, creating LLM-compatible item IDs to uniquely
identify each item is essential for recommendation foundation models. In this
study, we systematically examine the item ID creation and indexing problem for
recommendation foundation models, using P5 as an example of the backbone LLM.
To emphasize the importance of item indexing, we first discuss the issues of
several trivial item indexing methods, such as random indexing, title indexing,
and independent indexing. We then propose four simple yet effective solutions,
including sequential indexing, collaborative indexing, semantic (content-based)
indexing, and hybrid indexing. Our study highlights the significant influence
of item indexing methods on the performance of LLM-based recommendation, and
our results on real-world datasets validate the effectiveness of our proposed
solutions. The research also demonstrates how recent advances on language
modeling and traditional IR principles such as indexing can help each other for
better learning and inference. Source code and data are available at
https://github.com/Wenyueh/LLM-RecSys-ID.