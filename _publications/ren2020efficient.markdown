---
layout: publication
title: HM45;ANN Efficient Billion45;point Nearest Neighbor Search On Heterogeneous Memory
authors: Jie Ren, Minjia Zhang, Dong Li
conference: "Neural Information Processing Systems"
year: 2020
bibkey: ren2020efficient
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2020/hash/788d986905533aba051261497ecffcbb-Abstract.html"}
tags: ['Cross Modal', 'Graph', 'NEURIPS', 'Quantisation']
---
The state45;of45;the45;art approximate nearest neighbor search (ANNS) algorithms face a fundamental tradeoff between query latency and accuracy because of small main memory capacity To store indices in main memory for short query latency the ANNS algorithms have to limit dataset size or use a quantization scheme which hurts search accuracy. The emergence of heterogeneous memory (HM) brings a solution to significantly increase memory capacity and break the above tradeoff Using HM billions of data points can be placed in the main memory on a single machine without using any data compression. However HM consists of both fast (but small) memory and slow (but large) memory and using HM inappropriately slows down query significantly. In this work we present a novel graph45;based similarity search algorithm called HM45;ANN which takes both memory and data heterogeneity into consideration and enables billion45;scale similarity search on a single node without using compression. On two billion45;sized datasets BIGANN and DEEP1B HM45;ANN outperforms state45;of45;the45;art compression45;based solutions such as Lamp;C and IMI+OPQ in recall45;vs45;latency by a large margin obtaining 4637; higher recall under the same search latency. We also extend existing graph45;based methods such as HNSW and NSG with two strong baseline implementations on HM. At billion45;point scale HM45;ANN is 2X and 5.8X faster than our HNSWand NSG baselines respectively to reach the same accuracy.
