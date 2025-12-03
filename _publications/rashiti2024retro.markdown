---
layout: publication
title: 'Retro-li: Small-scale Retrieval Augmented Generation Supporting Noisy Similarity
  Searches And Domain Shift Generalization'
authors: Gentiana Rashiti, Geethan Karunaratne, Mrinmaya Sachan, Abu Sebastian, Abbas
  Rahimi
conference: Frontiers in Artificial Intelligence and Applications
year: 2024
bibkey: rashiti2024retro
citations: 0
additional_links: [{name: Code, url: 'https://github.com/IBM/Retrieval-Enhanced-Transformer-Little'},
  {name: Paper, url: 'https://arxiv.org/abs/2410.00004'}]
tags: ["Evaluation", "Similarity Search"]
short_authors: Rashiti et al.
---
The retrieval augmented generation (RAG) system such as Retro has been shown
to improve language modeling capabilities and reduce toxicity and
hallucinations by retrieving from a database of non-parametric memory
containing trillions of entries. We introduce Retro-li that shows retrieval can
also help using a small-scale database, but it demands more accurate and better
neighbors when searching in a smaller hence sparser non-parametric memory. This
can be met by using a proper semantic similarity search. We further propose
adding a regularization to the non-parametric memory for the first time: it
significantly reduces perplexity when the neighbor search operations are noisy
during inference, and it improves generalization when a domain shift occurs. We
also show that Retro-li's non-parametric memory can potentially be implemented
on analog in-memory computing hardware, exhibiting O(1) search time while
causing noise in retrieving neighbors, with minimal (<1%) performance loss. Our
code is available at:
https://github.com/IBM/Retrieval-Enhanced-Transformer-Little.