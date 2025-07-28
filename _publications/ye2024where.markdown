---
layout: publication
title: Where Am I? Cross-view Geo-localization With Natural Language Descriptions
authors: Junyan Ye, Honglin Lin, Leyan Ou, Dairong Chen, Zihao Wang, Qi Zhu, Conghui
  He, Weijia Li
conference: Arxiv
year: 2024
bibkey: ye2024where
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.17007'}]
tags: ["Image Retrieval", "Text Retrieval"]
short_authors: Ye et al.
---
Cross-view geo-localization identifies the locations of street-view images by
matching them with geo-tagged satellite images or OSM. However, most existing
studies focus on image-to-image retrieval, with fewer addressing text-guided
retrieval, a task vital for applications like pedestrian navigation and
emergency response. In this work, we introduce a novel task for cross-view
geo-localization with natural language descriptions, which aims to retrieve
corresponding satellite images or OSM database based on scene text
descriptions. To support this task, we construct the CVG-Text dataset by
collecting cross-view data from multiple cities and employing a scene text
generation approach that leverages the annotation capabilities of Large
Multimodal Models to produce high-quality scene text descriptions with
localization details. Additionally, we propose a novel text-based retrieval
localization method, CrossText2Loc, which improves recall by 10% and
demonstrates excellent long-text retrieval capabilities. In terms of
explainability, it not only provides similarity scores but also offers
retrieval reasons. More information can be found at
https://yejy53.github.io/CVG-Text/ .