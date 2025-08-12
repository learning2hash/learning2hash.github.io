---
layout: publication
title: 'Easyconvpooling: Random Pooling With Easy Convolution For Accelerating Training
  And Testing'
authors: Jianzhong Sheng, Chuanbo Chen, Chenchen Fu, Chun Jason Xue
conference: Arxiv
year: 2018
bibkey: sheng2018easyconvpooling
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.01729'}]
tags: ["Efficiency"]
short_authors: Sheng et al.
---
Convolution operations dominate the overall execution time of Convolutional
Neural Networks (CNNs). This paper proposes an easy yet efficient technique for
both Convolutional Neural Network training and testing. The conventional
convolution and pooling operations are replaced by Easy Convolution and Random
Pooling (ECP). In ECP, we randomly select one pixel out of four and only
conduct convolution operations of the selected pixel. As a result, only a
quarter of the conventional convolution computations are needed. Experiments
demonstrate that the proposed EasyConvPooling can achieve 1.45x speedup on
training time and 1.64x on testing time. What's more, a speedup of 5.09x on
pure Easy Convolution operations is obtained compared to conventional
convolution operations.