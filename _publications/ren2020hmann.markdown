---
layout: publication
title: HM-ANN Efficient Billion-Point Nearest Neighbor Search on Heterogeneous Memory
authors: Jie Ren, Minjia Zhang, Dong Li
conference: "Neural Information Processing Systems"
year: 2020
bibkey: ren2020hmann
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2020/hash/788d986905533aba051261497ecffcbb-Abstract.html"}
tags: ['GAN', 'Graph', 'NEURIPS', 'Quantisation']
---
The state-of-the-art approximate nearest neighbor search (ANNS) algorithms face a fundamental tradeoff between query latency and accuracy because of small main memory capacity To store indices in main memory for short query latency the ANNS algorithms have to limit dataset size or use a quantization scheme which hurts search accuracy. The emergence of heterogeneous memory (HM) brings a solution to significantly increase memory capacity and break the above tradeoff Using HM billions of data points can be placed in the main memory on a single machine without using any data compression. However HM consists of both fast (but small) memory and slow (but large) memory and using HM inappropriately slows down query significantly. In this work we present a novel graph-based similarity search algorithm called HM-ANN which takes both memory and data heterogeneity into consideration and enables billion-scale similarity search on a single node without using compression. On two billion-sized datasets BIGANN and DEEP1B HM-ANN outperforms state-of-the-art compression-based solutions such as LC and IMI+OPQ in recall-vs-latency by a large margin obtaining 46 higher recall under the same search latency. We also extend existing graph-based methods such as HNSW and NSG with two strong baseline implementations on HM. At billion-point scale HM-ANN is 2X and 5.8X faster than our HNSWand NSG baselines respectively to reach the same accuracy.
