---
layout: publication
title: 'The Medium Is Not The Message: Deconfounding Text Embeddings Via Linear Concept
  Erasure'
authors: Yu Fan, Yang Tian, Shauli Ravfogel, Mrinmaya Sachan, Elliott Ash, Alexander
  Hoyle
conference: Arxiv
year: 2025
bibkey: fan2025the
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2507.01234'}]
tags: ["Distance Metric Learning", "Evaluation"]
short_authors: Fan et al.
---
Embedding-based similarity metrics between text sequences can be influenced not just by the content dimensions we most care about, but can also be biased by spurious attributes like the text's source or language. These document confounders cause problems for many applications, but especially those that need to pool texts from different corpora. This paper shows that a debiasing algorithm that removes information about observed confounders from the encoder representations substantially reduces these biases at a minimal computational cost. Document similarity and clustering metrics improve across every embedding variant and task we evaluate -- often dramatically. Interestingly, performance on out-of-distribution benchmarks is not impacted, indicating that the embeddings are not otherwise degraded.