---
layout: publication
title: DVHN A Deep Hashing Framework For Large45;scale Vehicle Re45;identification
authors: Chen Yongbiao, Zhang Sheng, Liu Fangxin, Wu Chenggang, Guo Kaicheng, Qi Zhengwei
conference: "Arxiv"
year: 2021
bibkey: chen2021dvhn
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2112.04937"}
tags: ['ARXIV', 'Supervised']
---
In this paper we make the very first attempt to investigate the integration of deep hash learning with vehicle re45;identification. We propose a deep hash45;based vehicle re45;identification framework dubbed DVHN which substantially reduces memory usage and promotes retrieval efficiency while reserving nearest neighbor search accuracy. Concretely~DVHN directly learns discrete compact binary hash codes for each image by jointly optimizing the feature learning network and the hash code generating module. Specifically we directly constrain the output from the convolutional neural network to be discrete binary codes and ensure the learned binary codes are optimal for classification. To optimize the deep discrete hashing framework we further propose an alternating minimization method for learning binary similarity45;preserved hashing codes. Extensive experiments on two widely45;studied vehicle re45;identification datasets45; textbf123;VehicleID125; and textbf123;VeRi125;45;~have demonstrated the superiority of our method against the state45;of45;the45;art deep hash methods. textbf123;DVHN125; of 2048 bits can achieve 13.9437; and 10.2137; accuracy improvement in terms of textbf123;mAP125; and textbf123;Rank35;64;1125; for textbf123;VehicleID (800)125; dataset. For textbf123;VeRi125; we achieve 35.4537; and 32.7237; performance gains for textbf123;Rank35;64;1125; and textbf123;mAP125; respectively.
