---
layout: publication
title: Fast Supervised Discrete Hashing
authors: Gui Jie, Liu Tongliang, Sun Zhenan, Tao Dacheng, Tan Tieniu
conference: "Arxiv"
year: 2019
bibkey: gui2019fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1904.03556"}
tags: ['ARXIV', 'Supervised']
---
Learning45;based hashing algorithms are hot topics because they can greatly increase the scale at which existing methods operate. In this paper we propose a new learning45;based hashing method called fast supervised discrete hashing (FSDH) based on supervised discrete hashing (SDH). Regressing the training examples (or hash code) to the corresponding class labels is widely used in ordinary least squares regression. Rather than adopting this method FSDH uses a very simple yet effective regression of the class labels of training examples to the corresponding hash code to accelerate the algorithm. To the best of our knowledge this strategy has not previously been used for hashing. Traditional SDH decomposes the optimization into three sub45;problems with the most critical sub45;problem 45; discrete optimization for binary hash codes 45; solved using iterative discrete cyclic coordinate descent (DCC) which is time45;consuming. However FSDH has a closed45;form solution and only requires a single rather than iterative hash code45;solving step which is highly efficient. Furthermore FSDH is usually faster than SDH for solving the projection matrix for least squares regression making FSDH generally faster than SDH. For example our results show that FSDH is about 1245;times faster than SDH when the number of hashing bits is 128 on the CIFAR45;10 data base and FSDH is about 15145;times faster than FastHash when the number of hashing bits is 64 on the MNIST data45;base. Our experimental results show that FSDH is not only fast but also outperforms other comparative methods.
