---
layout: publication
title: 'Dothash: Estimating Set Similarity Metrics For Link Prediction And Document
  Deduplication'
authors: "Igor Nunes, Mike Heddes, Pere Verg\xE9s, Danny Abraham, Alexander Veidenbaum,\
  \ Alexandru Nicolau, Tony Givargis"
conference: Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and
  Data Mining
year: 2023
bibkey: nunes2023dothash
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.17310'}]
tags: ["Distance Metric Learning", "Evaluation", "KDD", "Locality-Sensitive-Hashing", "Recommender Systems"]
short_authors: Nunes et al.
---
Metrics for set similarity are a core aspect of several data mining tasks. To
remove duplicate results in a Web search, for example, a common approach looks
at the Jaccard index between all pairs of pages. In social network analysis, a
much-celebrated metric is the Adamic-Adar index, widely used to compare node
neighborhood sets in the important problem of predicting links. However, with
the increasing amount of data to be processed, calculating the exact similarity
between all pairs can be intractable. The challenge of working at this scale
has motivated research into efficient estimators for set similarity metrics.
The two most popular estimators, MinHash and SimHash, are indeed used in
applications such as document deduplication and recommender systems where large
volumes of data need to be processed. Given the importance of these tasks, the
demand for advancing estimators is evident. We propose DotHash, an unbiased
estimator for the intersection size of two sets. DotHash can be used to
estimate the Jaccard index and, to the best of our knowledge, is the first
method that can also estimate the Adamic-Adar index and a family of related
metrics. We formally define this family of metrics, provide theoretical bounds
on the probability of estimate errors, and analyze its empirical performance.
Our experimental results indicate that DotHash is more accurate than the other
estimators in link prediction and detecting duplicate documents with the same
complexity and similar comparison time.