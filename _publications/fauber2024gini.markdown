---
layout: publication
title: Gini Coefficient As A Unified Metric For Evaluating Many-versus-many Similarity
  In Vector Spaces
authors: Ben Fauber
conference: Arxiv
year: 2024
bibkey: fauber2024gini
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.07983'}]
tags: ["Evaluation"]
short_authors: Ben Fauber
---
We demonstrate that Gini coefficients can be used as unified metrics to
evaluate many-versus-many (all-to-all) similarity in vector spaces. Our
analysis of various image datasets shows that images with the highest Gini
coefficients tend to be the most similar to one another, while images with the
lowest Gini coefficients are the least similar. We also show that this
relationship holds true for vectorized text embeddings from various corpuses,
highlighting the consistency of our method and its broad applicability across
different types of data. Additionally, we demonstrate that selecting machine
learning training samples that closely match the distribution of the testing
dataset is far more important than ensuring data diversity. Selection of
exemplary and iconic training samples with higher Gini coefficients leads to
significantly better model performance compared to simply having a diverse
training set with lower Gini coefficients. Thus, Gini coefficients can serve as
effective criteria for selecting machine learning training samples, with our
selection method outperforming random sampling methods in very sparse
information settings.