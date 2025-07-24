---
layout: publication
title: Instance-level Image Retrieval Using Reranking Transformers
authors: Fuwen Tan, Jiangbo Yuan, Vicente Ordonez
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: tan2021instance
citations: 71
additional_links: [{name: Code, url: 'https://github.com/uvavision/RerankingTransformer'},
  {name: Paper, url: 'https://arxiv.org/abs/2103.12236'}]
tags: ["Datasets", "ICCV", "Image Retrieval", "Re-Ranking", "Supervised"]
short_authors: Fuwen Tan, Jiangbo Yuan, Vicente Ordonez
---
Instance-level image retrieval is the task of searching in a large database
for images that match an object in a query image. To address this task, systems
usually rely on a retrieval step that uses global image descriptors, and a
subsequent step that performs domain-specific refinements or reranking by
leveraging operations such as geometric verification based on local features.
In this work, we propose Reranking Transformers (RRTs) as a general model to
incorporate both local and global features to rerank the matching images in a
supervised fashion and thus replace the relatively expensive process of
geometric verification. RRTs are lightweight and can be easily parallelized so
that reranking a set of top matching results can be performed in a single
forward-pass. We perform extensive experiments on the Revisited Oxford and
Paris datasets, and the Google Landmarks v2 dataset, showing that RRTs
outperform previous reranking approaches while using much fewer local
descriptors. Moreover, we demonstrate that, unlike existing approaches, RRTs
can be optimized jointly with the feature extractor, which can lead to feature
representations tailored to downstream tasks and further accuracy improvements.
The code and trained models are publicly available at
https://github.com/uvavision/RerankingTransformer.