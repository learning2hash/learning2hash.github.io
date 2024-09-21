---
layout: publication
title: An ensemble diversity approach to supervised binary hashing
authors: Miguel A. Carreira-perpinan, Ramin Raziperchikolaei
conference: "Neural Information Processing Systems"
year: 2016
bibkey: a2016ensemble
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2016/hash/67f7fb873eaf29526a11a9b7ac33bfac-Abstract.html"}
tags: ['Image Retrieval', 'NEURIPS', 'Supervised']
---
Binary hashing is a well-known approach for fast approximate nearest-neighbor search in information retrieval. Much work has focused on affinity-based objective functions involving the hash functions or binary codes. These objective functions encode neighborhood information between data points and are often inspired by manifold learning algorithms. They ensure that the hash functions differ from each other through constraints or penalty terms that encourage codes to be orthogonal or dissimilar across bits but this couples the binary variables and complicates the already difficult optimization. We propose a much simpler approach we train each hash function (or bit) independently from each other but introduce diversity among them using techniques from classifier ensembles. Surprisingly we find that not only is this faster and trivially parallelizable but it also improves over the more complex coupled objective function and achieves state-of-the-art precision and recall in experiments with image retrieval.
