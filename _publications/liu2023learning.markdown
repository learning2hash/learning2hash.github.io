---
layout: publication
title: 'Learning Category Trees For Id-based Recommendation: Exploring The Power Of
  Differentiable Vector Quantization'
authors: Qijiong Liu, Lu Fan, Jiaren Xiao, Jieming Zhu, Xiao-ming Wu
conference: Proceedings of the ACM Web Conference 2024
year: 2024
bibkey: liu2023learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.16761'}]
tags: ["Quantization", "Recommender Systems"]
short_authors: Liu et al.
---
Category information plays a crucial role in enhancing the quality and
personalization of recommender systems. Nevertheless, the availability of item
category information is not consistently present, particularly in the context
of ID-based recommendations. In this work, we propose a novel approach to
automatically learn and generate entity (i.e., user or item) category trees for
ID-based recommendation. Specifically, we devise a differentiable vector
quantization framework for automatic category tree generation, namely CAGE,
which enables the simultaneous learning and refinement of categorical code
representations and entity embeddings in an end-to-end manner, starting from
the randomly initialized states. With its high adaptability, CAGE can be easily
integrated into both sequential and non-sequential recommender systems. We
validate the effectiveness of CAGE on various recommendation tasks including
list completion, collaborative filtering, and click-through rate prediction,
across different recommendation models. We release the code and data for others
to reproduce the reported results.