---
layout: publication
title: A Generic Inverted Index Framework For Similarity Search On The GPU - Technical Report
authors: Zhou Jingbo, Guo Qi, Jagadish H. V., Krčál Luboš, Liu Siyuan, Luan Wenhao, Tung Anthony K. H., Yang Yueji, Zheng Yuxin
conference: "Arxiv"
year: 2016
bibkey: zhou2016generic
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1603.08390"}
tags: ['ARXIV', 'Independent', 'LSH']
---
We propose a novel generic inverted index framework on the GPU (called GENIE), aiming to reduce the programming complexity of the GPU for parallel similarity search of different data types. Not every data type and similarity measure are supported by GENIE, but many popular ones are. We present the system design of GENIE, and demonstrate similarity search with GENIE on several data types along with a theoretical analysis of search results. A new concept of locality sensitive hashing (LSH) named \{\{ '\{\{' \}\}\tau\{\{ '\}\}' \}\}-ANN search, and a novel data structure c-PQ on the GPU are also proposed for achieving this purpose. Extensive experiments on different real-life datasets demonstrate the efficiency and effectiveness of our framework. The implemented system has been released as open source.
