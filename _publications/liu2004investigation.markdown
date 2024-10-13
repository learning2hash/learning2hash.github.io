---
layout: publication
title: An Investigation Of Practical Approximate Nearest Neighbor Algorithms
authors: Ting Liu, Andrew Moore, Ke Yang, Alexander Gray
conference: "Neural Information Processing Systems"
year: 2004
bibkey: liu2004investigation
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2004/hash/1102a326d5f7c9e04fc3c89d0ede88c9-Abstract.html"}
tags: ['Independent', 'LSH', 'NEURIPS']
---
This paper concerns approximate nearest neighbor searching algorithms,          which have become increasingly important, especially in high dimen-          sional perception areas such as computer vision, with dozens of publica-          tions in recent years. Much of this enthusiasm is due to a successful new          approximate nearest neighbor approach called Locality Sensitive Hash-          ing (LSH). In this paper we ask the question: can earlier spatial data          structure approaches to exact nearest neighbor, such as metric trees, be          altered to provide approximate answers to proximity queries and if so,          how? We introduce a new kind of metric tree that allows overlap: certain          datapoints may appear in both the children of a parent. We also intro-          duce new approximate k-NN search algorithms on this structure. We          show why these structures should be able to exploit the same random-          projection-based approximations that LSH enjoys, but with a simpler al-          gorithm and perhaps with greater efficiency. We then provide a detailed          empirical evaluation on five large, high dimensional datasets which show          up to 31-fold accelerations over LSH. This result holds true throughout          the spectrum of approximation levels.
