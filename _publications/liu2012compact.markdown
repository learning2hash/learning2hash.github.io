---
layout: publication
title: Compact Hyperplane Hashing With Bilinear Functions
authors: Liu Wei Columbia University, Wang Jun Ibm T. J. Watson Research Center, Mu Yadong Columbia University, Kumar Sanjiv Google, Chang Shih-fu Columbia University
conference: "Arxiv"
year: 2012
bibkey: liu2012compact
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1206.4618"}
tags: ['ARXIV', 'Supervised']
---
Hyperplane hashing aims at rapidly searching nearest points to a hyperplane, and has shown practical impact in scaling up active learning with SVMs. Unfortunately, the existing randomized methods need long hash codes to achieve reasonable search accuracy and thus suffer from reduced search speed and large memory overhead. To this end, this paper proposes a novel hyperplane hashing technique which yields compact hash codes. The key idea is the bilinear form of the proposed hash functions, which leads to higher collision probability than the existing hyperplane hash functions when using random projections. To further increase the performance, we propose a learning based framework in which the bilinear functions are directly learned from the data. This results in short yet discriminative codes, and also boosts the search performance over the random projection based solutions. Large-scale active learning experiments carried out on two datasets with up to one million samples demonstrate the overall superiority of the proposed approach.
