---
layout: publication
title: Spectral Clustering For Divide-and-conquer Graph Matching
authors: Vince Lyzinski, Daniel L. Sussman, Donniell E. Fishkind, Henry Pao, Li Chen,
  Joshua T. Vogelstein, Youngser Park, Carey E. Priebe
conference: Parallel Computing
year: 2015
bibkey: lyzinski2013spectral
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1310.1297'}]
tags: ["Graph Based ANN", "Scalability", "Unsupervised"]
short_authors: Lyzinski et al.
---
We present a parallelized bijective graph matching algorithm that leverages
seeds and is designed to match very large graphs. Our algorithm combines
spectral graph embedding with existing state-of-the-art seeded graph matching
procedures. We justify our approach by proving that modestly correlated, large
stochastic block model random graphs are correctly matched utilizing very few
seeds through our divide-and-conquer procedure. We also demonstrate the
effectiveness of our approach in matching very large graphs in simulated and
real data examples, showing up to a factor of 8 improvement in runtime with
minimal sacrifice in accuracy.