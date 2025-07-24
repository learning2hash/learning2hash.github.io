---
layout: publication
title: Deep Learning To Ternary Hash Codes By Continuation
authors: Mingrui Chen, Weiyu Li, Weizhi Lu
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2022
bibkey: chen2022deep
citations: 122
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.07987'}]
tags: ["Compact Codes", "Hashing Methods", "Image Retrieval", "Quantization"]
short_authors: Mingrui Chen, Weiyu Li, Weizhi Lu
---
Recently, it has been observed that \{0,1,-1\}-ternary codes which are simply
generated from deep features by hard thresholding, tend to outperform
\{-1,1\}-binary codes in image retrieval. To obtain better ternary codes, we for
the first time propose to jointly learn the features with the codes by
appending a smoothed function to the networks. During training, the function
could evolve into a non-smoothed ternary function by a continuation method. The
method circumvents the difficulty of directly training discrete functions and
reduces the quantization errors of ternary codes. Experiments show that the
generated codes indeed could achieve higher retrieval accuracy.