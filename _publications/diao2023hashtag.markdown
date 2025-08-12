---
layout: publication
title: Hashtag-guided Low-resource Tweet Classification
authors: Shizhe Diao, Sedrick Scott Keh, Liangming Pan, Zhiliang Tian, Yan Song, Tong
  Zhang
conference: Proceedings of the ACM Web Conference 2023
year: 2023
bibkey: diao2023hashtag
citations: 5
additional_links: [{name: Code, url: 'https://github.com/shizhediao/HashTation'},
  {name: Paper, url: 'https://arxiv.org/abs/2302.10143'}]
tags: []
short_authors: Diao et al.
---
Social media classification tasks (e.g., tweet sentiment analysis, tweet
stance detection) are challenging because social media posts are typically
short, informal, and ambiguous. Thus, training on tweets is challenging and
demands large-scale human-annotated labels, which are time-consuming and costly
to obtain. In this paper, we find that providing hashtags to social media
tweets can help alleviate this issue because hashtags can enrich short and
ambiguous tweets in terms of various information, such as topic, sentiment, and
stance. This motivates us to propose a novel Hashtag-guided Tweet
Classification model (HashTation), which automatically generates meaningful
hashtags for the input tweet to provide useful auxiliary signals for tweet
classification. To generate high-quality and insightful hashtags, our hashtag
generation model retrieves and encodes the post-level and entity-level
information across the whole corpus. Experiments show that HashTation achieves
significant improvements on seven low-resource tweet classification tasks, in
which only a limited amount of training data is provided, showing that
automatically enriching tweets with model-generated hashtags could
significantly reduce the demand for large-scale human-labeled data. Further
analysis demonstrates that HashTation is able to generate high-quality hashtags
that are consistent with the tweets and their labels. The code is available at
https://github.com/shizhediao/HashTation.