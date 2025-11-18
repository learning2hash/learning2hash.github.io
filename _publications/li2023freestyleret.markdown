---
layout: publication
title: 'Freestyleret: Retrieving Images From Style-diversified Queries'
authors: Hao Li, Curise Jia, Peng Jin, Zesen Cheng, Kehan Li, Jialu Sui, Chang Liu,
  Li Yuan
conference: Lecture Notes in Computer Science
year: 2023
bibkey: li2023freestyleret
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.02428'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Tools & Libraries"]
short_authors: Li et al.
---
Image Retrieval aims to retrieve corresponding images based on a given query.
In application scenarios, users intend to express their retrieval intent
through various query styles. However, current retrieval tasks predominantly
focus on text-query retrieval exploration, leading to limited retrieval query
options and potential ambiguity or bias in user intention. In this paper, we
propose the Style-Diversified Query-Based Image Retrieval task, which enables
retrieval based on various query styles. To facilitate the novel setting, we
propose the first Diverse-Style Retrieval dataset, encompassing diverse query
styles including text, sketch, low-resolution, and art. We also propose a
light-weighted style-diversified retrieval framework. For various query style
inputs, we apply the Gram Matrix to extract the query's textural features and
cluster them into a style space with style-specific bases. Then we employ the
style-init prompt tuning module to enable the visual encoder to comprehend the
texture and style information of the query. Experiments demonstrate that our
model, employing the style-init prompt tuning strategy, outperforms existing
retrieval models on the style-diversified retrieval task. Moreover,
style-diversified queries~(sketch+text, art+text, etc) can be simultaneously
retrieved in our model. The auxiliary information from other queries enhances
the retrieval performance within the respective query.