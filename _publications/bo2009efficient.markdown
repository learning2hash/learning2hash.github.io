---
layout: publication
title: Efficient Match Kernel Between Sets Of Features For Visual Recognition
authors: Liefeng Bo, Cristian Sminchisescu
conference: "Neural Information Processing Systems"
year: 2009
bibkey: bo2009efficient
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2009/hash/4daa3db355ef2b0e64b472968cb70f0d-Abstract.html"}
tags: ['NEURIPS', 'Quantisation']
---
In visual recognition the images are frequently modeled as sets of local features (bags). We show that bag of words a common method to handle such cases can be viewed as a special match kernel which counts 1 if two local features fall into the same regions partitioned by visual words and 0 otherwise. Despite its simplicity this quantization is too coarse. It is therefore appealing to design match kernels that more accurately measure the similarity between local features. However it is impractical to use such kernels on large datasets due to their significant computational cost. To address this problem we propose an efficient match kernel (EMK) which maps local features to a low dimensional feature space average the resulting feature vectors to form a set-level feature then apply a linear classifier. The local feature maps are learned so that their inner products preserve to the best possible the values of the specified kernel function. EMK is linear both in the number of images and in the number of local features. We demonstrate that EMK is extremely efficient and achieves the current state of the art performance on three difficult real world datasets Scene-15 Caltech-101 and Caltech-256.
