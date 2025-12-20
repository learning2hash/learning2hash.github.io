---
layout: publication
title: 'I Know Why You Like This Movie: Interpretable Efficient Multimodal Recommender'
authors: "Barbara Rychalska, Dominika Basaj, Jacek D\u0105browski, Micha\u0142 Daniluk"
conference: Arxiv
year: 2020
bibkey: rychalska2020i
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.09979'}]
tags: ["Datasets", "Hashing Methods", "Recommender Systems"]
short_authors: Rychalska et al.
---
Recently, the Efficient Manifold Density Estimator (EMDE) model has been
introduced. The model exploits Local Sensitive Hashing and Count-Min Sketch
algorithms, combining them with a neural network to achieve state-of-the-art
results on multiple recommender datasets. However, this model ingests a
compressed joint representation of all input items for each user/session, so
calculating attributions for separate items via gradient-based methods seems
not applicable. We prove that interpreting this model in a white-box setting is
possible thanks to the properties of EMDE item retrieval method. By exploiting
multimodal flexibility of this model, we obtain meaningful results showing the
influence of multiple modalities: text, categorical features, and images, on
movie recommendation output.