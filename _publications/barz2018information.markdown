---
layout: publication
title: Information-theoretic Active Learning For Content-based Image Retrieval
authors: "Bj\xF6rn Barz, Christoph K\xE4ding, Joachim Denzler"
conference: Lecture Notes in Computer Science
year: 2019
bibkey: barz2018information
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.02337'}]
tags: ["Image Retrieval"]
short_authors: "Bj\xF6rn Barz, Christoph K\xE4ding, Joachim Denzler"
---
We propose Information-Theoretic Active Learning (ITAL), a novel batch-mode
active learning method for binary classification, and apply it for acquiring
meaningful user feedback in the context of content-based image retrieval.
Instead of combining different heuristics such as uncertainty, diversity, or
density, our method is based on maximizing the mutual information between the
predicted relevance of the images and the expected user feedback regarding the
selected batch. We propose suitable approximations to this computationally
demanding problem and also integrate an explicit model of user behavior that
accounts for possible incorrect labels and unnameable instances. Furthermore,
our approach does not only take the structure of the data but also the expected
model output change caused by the user feedback into account. In contrast to
other methods, ITAL turns out to be highly flexible and provides
state-of-the-art performance across various datasets, such as MIRFLICKR and
ImageNet.