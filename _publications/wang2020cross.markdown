---
layout: publication
title: 'Cross-modal Food Retrieval: Learning A Joint Embedding Of Food Images And
  Recipes With Semantic Consistency And Attention Mechanism'
authors: Hao Wang, Doyen Sahoo, Chenghao Liu, Ke Shu, Palakorn Achananuparp, Ee-Peng
  Lim, Steven C. H. Hoi
conference: Arxiv
year: 2020
bibkey: wang2020cross
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.03955'}]
tags: ["Datasets", "Evaluation", "Multimodal Retrieval", "Scalability"]
short_authors: Wang et al.
---
Food retrieval is an important task to perform analysis of food-related
information, where we are interested in retrieving relevant information about
the queried food item such as ingredients, cooking instructions, etc. In this
paper, we investigate cross-modal retrieval between food images and cooking
recipes. The goal is to learn an embedding of images and recipes in a common
feature space, such that the corresponding image-recipe embeddings lie close to
one another. Two major challenges in addressing this problem are 1) large
intra-variance and small inter-variance across cross-modal food data; and 2)
difficulties in obtaining discriminative recipe representations. To address
these two problems, we propose Semantic-Consistent and Attention-based Networks
(SCAN), which regularize the embeddings of the two modalities through aligning
output semantic probabilities. Besides, we exploit a self-attention mechanism
to improve the embedding of recipes. We evaluate the performance of the
proposed method on the large-scale Recipe1M dataset, and show that we can
outperform several state-of-the-art cross-modal retrieval strategies for food
images and cooking recipes by a significant margin.