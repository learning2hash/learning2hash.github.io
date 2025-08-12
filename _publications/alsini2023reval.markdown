---
layout: publication
title: '#REVAL: A Semantic Evaluation Framework For Hashtag Recommendation'
authors: Areej Alsini, Du Q. Huynh, Amitava Datta
conference: Arxiv
year: 2023
bibkey: alsini2023reval
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.18330'}]
tags: ["Evaluation", "Recommender Systems"]
short_authors: Areej Alsini, Du Q. Huynh, Amitava Datta
---
Automatic evaluation of hashtag recommendation models is a fundamental task
in many online social network systems. In the traditional evaluation method,
the recommended hashtags from an algorithm are firstly compared with the ground
truth hashtags for exact correspondences. The number of exact matches is then
used to calculate the hit rate, hit ratio, precision, recall, or F1-score. This
way of evaluating hashtag similarities is inadequate as it ignores the semantic
correlation between the recommended and ground truth hashtags. To tackle this
problem, we propose a novel semantic evaluation framework for hashtag
recommendation, called \#REval. This framework includes an internal module
referred to as BERTag, which automatically learns the hashtag embeddings. We
investigate on how the \#REval framework performs under different word embedding
methods and different numbers of synonyms and hashtags in the recommendation
using our proposed \#REval-hit-ratio measure. Our experiments of the proposed
framework on three large datasets show that \#REval gave more meaningful hashtag
synonyms for hashtag recommendation evaluation. Our analysis also highlights
the sensitivity of the framework to the word embedding technique, with \#REval
based on BERTag more superior over \#REval based on FastText and Word2Vec.