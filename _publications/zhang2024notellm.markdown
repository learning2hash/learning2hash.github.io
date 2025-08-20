---
layout: publication
title: 'Notellm: A Retrievable Large Language Model For Note Recommendation'
authors: Chao Zhang, Shiwei Wu, Haoxin Zhang, Tong Xu, Yan Gao, Yao Hu, di Wu, Enhong
  Chen
conference: Companion Proceedings of the ACM Web Conference 2024
year: 2024
bibkey: zhang2024notellm
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.01744'}]
tags: [Recommender Systems, Self-Supervised, Tools & Libraries]
short_authors: Zhang et al.
---
People enjoy sharing "notes" including their experiences within online
communities. Therefore, recommending notes aligned with user interests has
become a crucial task. Existing online methods only input notes into BERT-based
models to generate note embeddings for assessing similarity. However, they may
underutilize some important cues, e.g., hashtags or categories, which represent
the key concepts of notes. Indeed, learning to generate hashtags/categories can
potentially enhance note embeddings, both of which compress key note
information into limited content. Besides, Large Language Models (LLMs) have
significantly outperformed BERT in understanding natural languages. It is
promising to introduce LLMs into note recommendation. In this paper, we propose
a novel unified framework called NoteLLM, which leverages LLMs to address the
item-to-item (I2I) note recommendation. Specifically, we utilize Note
Compression Prompt to compress a note into a single special token, and further
learn the potentially related notes' embeddings via a contrastive learning
approach. Moreover, we use NoteLLM to summarize the note and generate the
hashtag/category automatically through instruction tuning. Extensive
validations on real scenarios demonstrate the effectiveness of our proposed
method compared with the online baseline and show major improvements in the
recommendation system of Xiaohongshu.