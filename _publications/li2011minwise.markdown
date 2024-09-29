---
layout: publication
title: B45;bit Minwise Hashing For Large45;scale Linear SVM
authors: Li Ping, Moore Joshua, Konig Christian
conference: "Arxiv"
year: 2011
bibkey: li2011minwise
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1105.4385"}
tags: ['ARXIV', 'Supervised']
---
In this paper we propose to (seamlessly) integrate b45;bit minwise hashing with linear SVM to substantially improve the training (and testing) efficiency using much smaller memory with essentially no loss of accuracy. Theoretically we prove that the resemblance matrix the minwise hashing matrix and the b45;bit minwise hashing matrix are all positive definite matrices (kernels). Interestingly our proof for the positive definiteness of the b45;bit minwise hashing kernel naturally suggests a simple strategy to integrate b45;bit hashing with linear SVM. Our technique is particularly useful when the data can not fit in memory which is an increasingly critical issue in large45;scale machine learning. Our preliminary experimental results on a publicly available webspam dataset (350K samples and 16 million dimensions) verified the effectiveness of our algorithm. For example the training time was reduced to merely a few seconds. In addition our technique can be easily extended to many other linear and nonlinear machine learning applications such as logistic regression.
