---
layout: publication
title: DVHN A Deep Hashing Framework For Large-scale Vehicle Re-identification
authors: Chen Yongbiao, Zhang Sheng, Liu Fangxin, Wu Chenggang, Guo Kaicheng, Qi Zhengwei
conference: "Arxiv"
year: 2021
bibkey: chen2021dvhn
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2112.04937"}
tags: ['ARXIV', 'Supervised']
---
In this paper, we make the very first attempt to investigate the integration of deep hash learning with vehicle re-identification. We propose a deep hash-based vehicle re-identification framework, dubbed DVHN, which substantially reduces memory usage and promotes retrieval efficiency while reserving nearest neighbor search accuracy. Concretely,~DVHN directly learns discrete compact binary hash codes for each image by jointly optimizing the feature learning network and the hash code generating module. Specifically, we directly constrain the output from the convolutional neural network to be discrete binary codes and ensure the learned binary codes are optimal for classification. To optimize the deep discrete hashing framework, we further propose an alternating minimization method for learning binary similarity-preserved hashing codes. Extensive experiments on two widely-studied vehicle re-identification datasets- \textbf\{VehicleID\} and \textbf\{VeRi\}-~have demonstrated the superiority of our method against the state-of-the-art deep hash methods. \textbf\{DVHN\} of $2048$ bits can achieve 13.94\&#37; and 10.21\&#37; accuracy improvement in terms of \textbf\{mAP\} and \textbf\{Rank@1\} for \textbf\{VehicleID (800)\} dataset. For \textbf\{VeRi\}, we achieve 35.45\&#37; and 32.72\&#37; performance gains for \textbf\{Rank@1\} and \textbf\{mAP\}, respectively.
