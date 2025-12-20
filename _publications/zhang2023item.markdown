---
layout: publication
title: Item Cold Start Recommendation Via Adversarial Variational Auto-encoder Warm-up
authors: Shenzheng Zhang, Qi Tan, Xinzhi Zheng, Yi Ren, Xu Zhao
conference: Arxiv
year: 2023
bibkey: zhang2023item
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.14395'}]
tags: ["Datasets", "Evaluation", "Recommender Systems", "Robustness", "Scalability"]
short_authors: Zhang et al.
---
The gap between the randomly initialized item ID embedding and the
well-trained warm item ID embedding makes the cold items hard to suit the
recommendation system, which is trained on the data of historical warm items.
To alleviate the performance decline of new items recommendation, the
distribution of the new item ID embedding should be close to that of the
historical warm items. To achieve this goal, we propose an Adversarial
Variational Auto-encoder Warm-up model (AVAEW) to generate warm-up item ID
embedding for cold items. Specifically, we develop a conditional variational
auto-encoder model to leverage the side information of items for generating the
warm-up item ID embedding. Particularly, we introduce an adversarial module to
enforce the alignment between warm-up item ID embedding distribution and
historical item ID embedding distribution. We demonstrate the effectiveness and
compatibility of the proposed method by extensive offline experiments on public
datasets and online A/B tests on a real-world large-scale news recommendation
platform.