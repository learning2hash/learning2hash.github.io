---
layout: publication
title: Deep Asymmetric Hashing With Dual Semantic Regression And Class Structure Quantization
authors: Lu Jianglin, Wang Hailing, Zhou Jie, Yan Mengfan, Wen Jiajun
conference: "Arxiv"
year: 2021
bibkey: lu2021deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2110.12478"}
tags: ['ARXIV', 'Graph', 'Image Retrieval', 'Quantisation', 'Supervised']
---
Recently deep hashing methods have been widely used in image retrieval task. Most existing deep hashing approaches adopt one45;to45;one quantization to reduce information loss. However such class45;unrelated quantization cannot give discriminative feedback for network training. In addition these methods only utilize single label to integrate supervision information of data for hashing function learning which may result in inferior network generalization performance and relatively low45;quality hash codes since the inter45;class information of data is totally ignored. In this paper we propose a dual semantic asymmetric hashing (DSAH) method which generates discriminative hash codes under three45;fold constraints. Firstly DSAH utilizes class prior to conduct class structure quantization so as to transmit class information during the quantization process. Secondly a simple yet effective label mechanism is designed to characterize both the intra45;class compactness and inter45;class separability of data thereby achieving semantic45;sensitive binary code learning. Finally a meaningful pairwise similarity preserving loss is devised to minimize the distances between class45;related network outputs based on an affinity graph. With these three main components high45;quality hash codes can be generated through network. Extensive experiments conducted on various datasets demonstrate the superiority of DSAH in comparison with state45;of45;the45;art deep hashing methods.
