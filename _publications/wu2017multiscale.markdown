---
layout: publication
title: Multiscale Quantization For Fast Similarity Search
authors: Xiang Wu, Ruiqi Guo, Ananda Theertha Suresh, Sanjiv Kumar, Daniel N. Holtmann-rice, David Simcha, Felix Yu
conference: "Neural Information Processing Systems"
year: 2017
bibkey: wu2017multiscale
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2017/hash/b6617980ce90f637e68c3ebe8b9be745-Abstract.html"}
tags: ['NEURIPS', 'Quantisation']
---
We propose a multiscale quantization approach for fast similarity search on large high-dimensional datasets. The key insight of the approach is that quantization methods in particular product quantization perform poorly when there is large variance in the norms of the data points. This is a common scenario for real- world datasets especially when doing product quantization of residuals obtained from coarse vector quantization. To address this issue we propose a multiscale formulation where we learn a separate scalar quantizer of the residual norm scales. All parameters are learned jointly in a stochastic gradient descent framework to minimize the overall quantization error. We provide theoretical motivation for the proposed technique and conduct comprehensive experiments on two large-scale public datasets demonstrating substantial improvements in recall over existing state-of-the-art methods.
