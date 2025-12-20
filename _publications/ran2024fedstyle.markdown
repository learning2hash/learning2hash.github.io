---
layout: publication
title: 'Fedstyle: Style-based Federated Learning Crowdsourcing Framework For Art Commissions'
authors: Changjuan Ran, Yeting Guo, Fang Liu, Shenglan Cui, Yunfan Ye
conference: 2024 IEEE International Conference on Multimedia and Expo (ICME)
year: 2024
bibkey: ran2024fedstyle
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.16336'}]
tags: ["Datasets", "Self-Supervised", "Tools & Libraries"]
short_authors: Ran et al.
---
The unique artistic style is crucial to artists' occupational
competitiveness, yet prevailing Art Commission Platforms rarely support
style-based retrieval. Meanwhile, the fast-growing generative AI techniques
aggravate artists' concerns about releasing personal artworks to public
platforms. To achieve artistic style-based retrieval without exposing personal
artworks, we propose FedStyle, a style-based federated learning crowdsourcing
framework. It allows artists to train local style models and share model
parameters rather than artworks for collaboration. However, most artists
possess a unique artistic style, resulting in severe model drift among them.
FedStyle addresses such extreme data heterogeneity by having artists learn
their abstract style representations and align with the server, rather than
merely aggregating model parameters lacking semantics. Besides, we introduce
contrastive learning to meticulously construct the style representation space,
pulling artworks with similar styles closer and keeping different ones apart in
the embedding space. Extensive experiments on the proposed datasets demonstrate
the superiority of FedStyle.