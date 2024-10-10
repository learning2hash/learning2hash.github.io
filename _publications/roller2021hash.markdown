---
layout: publication
title: Hash Layers For Large Sparse Models
authors: Stephen Roller, Sainbayar Sukhbaatar, Arthur Szlam, Jason Weston
conference: "Neural Information Processing Systems"
year: 2021
bibkey: roller2021hash
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2021/hash/92bf5e6240737e0326ea59846a83e076-Abstract.html"}
tags: ['Independent', 'NEURIPS']
---
We investigate the training of sparse layers that use different parameters for different inputs based on hashing in large Transformer models. Specifically we modify the feedforward layer to hash to different sets of weights depending on the current token over all tokens in the sequence. We show that this procedure either outperforms or is competitive with learning-to-route mixture-of-expert methods such as Switch Transformers and BASE Layers while requiring no routing parameters or extra terms in the objective function such as a load balancing loss and no sophisticated assignment algorithm. We study the performance of different hashing techniques hash sizes and input features and show that balanced and random hashes focused on the most local features work best compared to either learning clusters or using longer-range context. We show our approach works well both on large language modeling and dialogue tasks and on downstream fine-tuning tasks.
