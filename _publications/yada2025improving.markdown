---
layout: publication
title: Improving Visual Recommendation On E-commerce Platforms Using Vision-language
  Models
authors: Yuki Yada, Sho Akiyama, Ryo Watanabe, Yuta Ueno, Yusuke Shido, Andre Rusli
conference: Proceedings of the Nineteenth ACM Conference on Recommender Systems
year: 2025
bibkey: yada2025improving
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2510.13359'}]
tags: ["Distance Metric Learning", "Evaluation", "Recommender Systems", "Scalability", "Text Retrieval"]
short_authors: Yada et al.
---
On large-scale e-commerce platforms with tens of millions of active monthly users, recommending visually similar products is essential for enabling users to efficiently discover items that align with their preferences. This study presents the application of a vision-language model (VLM) -- which has demonstrated strong performance in image recognition and image-text retrieval tasks -- to product recommendations on Mercari, a major consumer-to-consumer marketplace used by more than 20 million monthly users in Japan. Specifically, we fine-tuned SigLIP, a VLM employing a sigmoid-based contrastive loss, using one million product image-title pairs from Mercari collected over a three-month period, and developed an image encoder for generating item embeddings used in the recommendation system. Our evaluation comprised an offline analysis of historical interaction logs and an online A/B test in a production environment. In offline analysis, the model achieved a 9.1% improvement in nDCG@5 compared with the baseline. In the online A/B test, the click-through rate improved by 50% whereas the conversion rate improved by 14% compared with the existing model. These results demonstrate the effectiveness of VLM-based encoders for e-commerce product recommendations and provide practical insights into the development of visual similarity-based recommendation systems.