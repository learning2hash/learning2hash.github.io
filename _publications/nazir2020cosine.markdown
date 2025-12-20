---
layout: publication
title: Cosine Similarity Of Multimodal Content Vectors For TV Programmes
authors: Saba Nazir, Taner Cagali, Chris Newell, Mehrnoosh Sadrzadeh
conference: Arxiv
year: 2020
bibkey: nazir2020cosine
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.11129'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Recommender Systems"]
short_authors: Nazir et al.
---
Multimodal information originates from a variety of sources: audiovisual
files, textual descriptions, and metadata. We show how one can represent the
content encoded by each individual source using vectors, how to combine the
vectors via middle and late fusion techniques, and how to compute the semantic
similarities between the contents. Our vectorial representations are built from
spectral features and Bags of Audio Words, for audio, LSI topics and Doc2vec
embeddings for subtitles, and the categorical features, for metadata. We
implement our model on a dataset of BBC TV programmes and evaluate the fused
representations to provide recommendations. The late fused similarity matrices
significantly improve the precision and diversity of recommendations.