---
layout: publication
title: Speeding Up Word Mover's Distance And Its Variants Via Properties Of Distances
  Between Embeddings
authors: Matheus Werner, Eduardo Laber
conference: Arxiv
year: 2019
bibkey: werner2019speeding
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.00509'}]
tags: ["Datasets", "Distance Metric Learning", "Efficiency", "Scalability"]
short_authors: Matheus Werner, Eduardo Laber
---
The Word Mover's Distance (WMD) proposed by Kusner et al. is a distance
between documents that takes advantage of semantic relations among words that
are captured by their embeddings. This distance proved to be quite effective,
obtaining state-of-art error rates for classification tasks, but is also
impracticable for large collections/documents due to its computational
complexity. For circumventing this problem, variants of WMD have been proposed.
Among them, Relaxed Word Mover's Distance (RWMD) is one of the most successful
due to its simplicity, effectiveness, and also because of its fast
implementations.
  Relying on assumptions that are supported by empirical properties of the
distances between embeddings, we propose an approach to speed up both WMD and
RWMD. Experiments over 10 datasets suggest that our approach leads to a
significant speed-up in document classification tasks while maintaining the
same error rates.