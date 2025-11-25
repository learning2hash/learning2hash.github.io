---
layout: publication
title: Efficient And Discriminative Image Feature Extraction For Universal Image Retrieval
authors: "Morris Florek, David Tschirschwitz, Bj\xF6rn Barz, Volker Rodehorst"
conference: Arxiv
year: 2024
bibkey: florek2024efficient
citations: 0
additional_links: [{name: Code, url: 'https://github.com/morrisfl/UniFEx'}, {name: Paper,
    url: 'https://arxiv.org/abs/2409.13513'}]
tags: ["Datasets", "Distance Metric Learning", "Efficiency", "Image Retrieval"]
short_authors: Florek et al.
---
Current image retrieval systems often face domain specificity and
generalization issues. This study aims to overcome these limitations by
developing a computationally efficient training framework for a universal
feature extractor that provides strong semantic image representations across
various domains. To this end, we curated a multi-domain training dataset,
called M4D-35k, which allows for resource-efficient training. Additionally, we
conduct an extensive evaluation and comparison of various state-of-the-art
visual-semantic foundation models and margin-based metric learning loss
functions regarding their suitability for efficient universal feature
extraction. Despite constrained computational resources, we achieve near
state-of-the-art results on the Google Universal Image Embedding Challenge,
with a mMP@5 of 0.721. This places our method at the second rank on the
leaderboard, just 0.7 percentage points behind the best performing method.
However, our model has 32% fewer overall parameters and 289 times fewer
trainable parameters. Compared to methods with similar computational
requirements, we outperform the previous state of the art by 3.3 percentage
points. We release our code and M4D-35k training set annotations at
https://github.com/morrisfl/UniFEx.