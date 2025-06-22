---
layout: publication
title: Fast And Exact Nearest Neighbor Search In Hamming Space On Full-text Search
  Engines
authors: Cun Mu, Jun Zhao, Guang Yang, Binwei Yang, Zheng Yan
conference: Arxiv
year: 2019
citations: 4
bibkey: mu2019fast
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.08498'}]
tags: [ANN Search]
---
A growing interest has been witnessed recently from both academia and
industry in building nearest neighbor search (NNS) solutions on top of
full-text search engines. Compared with other NNS systems, such solutions are
capable of effectively reducing main memory consumption, coherently supporting
multi-model search and being immediately ready for production deployment. In
this paper, we continue the journey to explore specifically how to empower
full-text search engines with fast and exact NNS in Hamming space (i.e., the
set of binary codes). By revisiting three techniques (bit operation, subs-code
filtering and data preprocessing with permutation) in information retrieval
literature, we develop a novel engineering solution for full-text search
engines to efficiently accomplish this special but important NNS task. In the
experiment, we show that our proposed approach enables full-text search engines
to achieve significant speed-ups over its state-of-the-art term match approach
for NNS within binary codes.