---
layout: publication
title: 'Hstu-blair: Lightweight Contrastive Text Embedding For Generative Recommender'
authors: Yijun Liu
conference: Arxiv
year: 2025
bibkey: liu2025hstu
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.10545'}]
tags: ["Datasets", "Evaluation", "Recommender Systems", "Tools & Libraries"]
short_authors: Yijun Liu
---
Recent advances in recommender systems have underscored the complementary strengths of generative modeling and pretrained language models. We propose HSTU-BLaIR, a hybrid framework that augments the Hierarchical Sequential Transduction Unit (HSTU)-based generative recommender with BLaIR, a lightweight contrastive text embedding model. This integration enriches item representations with semantic signals from textual metadata while preserving HSTU's powerful sequence modeling capabilities.
  We evaluate HSTU-BLaIR on two e-commerce datasets: three subsets from the Amazon Reviews 2023 dataset and the Steam dataset. We compare its performance against both the original HSTU-based recommender and a variant augmented with embeddings from OpenAI's state-of-the-art \texttt\{text-embedding-3-large\} model. Despite the latter being trained on a substantially larger corpus with significantly more parameters, our lightweight BLaIR-enhanced approach -- pretrained on domain-specific data -- achieves better performance in nearly all cases. Specifically, HSTU-BLaIR outperforms the OpenAI embedding-based variant on all but one metric, where it is marginally lower, and matches it on another. These findings highlight the effectiveness of contrastive text embeddings in compute-efficient recommendation settings.