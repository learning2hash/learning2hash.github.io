---
layout: publication
title: Exploring The Meaningfulness Of Nearest Neighbor Search In High-dimensional
  Space
authors: Chen Zhonghan, Zhang Ruiyuan, Zhao Xi, Cheng Xiaojun, Zhou Xiaofang
conference: Lecture Notes in Computer Science
year: 2024
bibkey: chen2024exploring
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.05752'}]
tags: ["Datasets", "Efficiency", "Scalability", "Similarity Search"]
short_authors: Chen et al.
---
Dense high dimensional vectors are becoming increasingly vital in fields such
as computer vision, machine learning, and large language models (LLMs), serving
as standard representations for multimodal data. Now the dimensionality of
these vector can exceed several thousands easily. Despite the nearest neighbor
search (NNS) over these dense high dimensional vectors have been widely used
for retrieval augmented generation (RAG) and many other applications, the
effectiveness of NNS in such a high-dimensional space remains uncertain, given
the possible challenge caused by the "curse of dimensionality." To address
above question, in this paper, we conduct extensive NNS studies with different
distance functions, such as \\(L_1\\) distance, \\(L_2\\) distance and
angular-distance, across diverse embedding datasets, of varied types,
dimensionality and modality. Our aim is to investigate factors influencing the
meaningfulness of NNS. Our experiments reveal that high-dimensional text
embeddings exhibit increased resilience as dimensionality rises to higher
levels when compared to random vectors. This resilience suggests that text
embeddings are less affected to the "curse of dimensionality," resulting in
more meaningful NNS outcomes for practical use. Additionally, the choice of
distance function has minimal impact on the relevance of NNS. Our study shows
the effectiveness of the embedding-based data representation method and can
offer opportunity for further optimization of dense vector-related
applications.