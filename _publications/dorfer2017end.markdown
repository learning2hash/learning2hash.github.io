---
layout: publication
title: End-to-end Cross-modality Retrieval With CCA Projections And Pairwise Ranking
  Loss
authors: "Matthias Dorfer, Jan Schl\xFCter, Andreu Vall, Filip Korzeniowski, Gerhard\
  \ Widmer"
conference: International Journal of Multimedia Information Retrieval
year: 2018
bibkey: dorfer2017end
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.06979'}]
tags: ["Few Shot & Zero Shot", "Text Retrieval"]
short_authors: Dorfer et al.
---
Cross-modality retrieval encompasses retrieval tasks where the fetched items
are of a different type than the search query, e.g., retrieving pictures
relevant to a given text query. The state-of-the-art approach to cross-modality
retrieval relies on learning a joint embedding space of the two modalities,
where items from either modality are retrieved using nearest-neighbor search.
In this work, we introduce a neural network layer based on Canonical
Correlation Analysis (CCA) that learns better embedding spaces by analytically
computing projections that maximize correlation. In contrast to previous
approaches, the CCA Layer (CCAL) allows us to combine existing objectives for
embedding space learning, such as pairwise ranking losses, with the optimal
projections of CCA. We show the effectiveness of our approach for
cross-modality retrieval on three different scenarios (text-to-image,
audio-sheet-music and zero-shot retrieval), surpassing both Deep CCA and a
multi-view network using freely learned projections optimized by a pairwise
ranking loss, especially when little training data is available (the code for
all three methods is released at: https://github.com/CPJKU/cca_layer).