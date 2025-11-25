---
layout: publication
title: Learning Tuple Compatibility For Conditional Outfitrecommendation
authors: Xuewen Yang, Dongliang Xie, Xin Wang, Jiangbo Yuan, Wanying Ding, Pengyun
  Yan
conference: ACM Multimedia 2020
year: 2020
bibkey: yang2020learning
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.08189'}]
tags: ["Datasets", "Recommender Systems", "Similarity Search"]
short_authors: Yang et al.
---
Outfit recommendation requires the answers of some challenging outfit
compatibility questions such as 'Which pair of boots and school bag go well
with my jeans and sweater?'. It is more complicated than conventional
similarity search, and needs to consider not only visual aesthetics but also
the intrinsic fine-grained and multi-category nature of fashion items. Some
existing approaches solve the problem through sequential models or learning
pair-wise distances between items. However, most of them only consider coarse
category information in defining fashion compatibility while neglecting the
fine-grained category information often desired in practical applications. To
better define the fashion compatibility and more flexibly meet different needs,
we propose a novel problem of learning compatibility among multiple tuples
(each consisting of an item and category pair), and recommending fashion items
following the category choices from customers. Our contributions include: 1)
Designing a Mixed Category Attention Net (MCAN) which integrates both
fine-grained and coarse category information into recommendation and learns the
compatibility among fashion tuples. MCAN can explicitly and effectively
generate diverse and controllable recommendations based on need. 2)
Contributing a new dataset IQON, which follows eastern culture and can be used
to test the generalization of recommendation systems. Our extensive experiments
on a reference dataset Polyvore and our dataset IQON demonstrate that our
method significantly outperforms state-of-the-art recommendation methods.