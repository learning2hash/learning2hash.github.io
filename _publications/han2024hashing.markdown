---
layout: publication
title: Hashing Based Contrastive Learning For Virtual Screening
authors: Han Jin, Hong Yun, Li Wu-jun
conference: "Arxiv"
year: 2024
bibkey: han2024hashing
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2407.19790"}
tags: ['ARXIV', 'Deep Learning', 'Self Supervised']
---
Virtual screening (VS) is a critical step in computer45;aided drug discovery aiming to identify molecules that bind to a specific target receptor like protein. Traditional VS methods such as docking are often too time45;consuming for screening large45;scale molecular databases. Recent advances in deep learning have demonstrated that learning vector representations for both proteins and molecules using contrastive learning can outperform traditional docking methods. However given that target databases often contain billions of molecules real45;valued vector representations adopted by existing methods can still incur significant memory and time costs in VS. To address this problem in this paper we propose a hashing45;based contrastive learning method called DrugHash for VS. DrugHash treats VS as a retrieval task that uses efficient binary hash codes for retrieval. In particular DrugHash designs a simple yet effective hashing strategy to enable end45;to45;end learning of binary hash codes for both protein and molecule modalities which can dramatically reduce the memory and time costs with higher accuracy compared with existing methods. Experimental results show that DrugHash can outperform existing methods to achieve state45;of45;the45;art accuracy with a memory saving of 32× and a speed improvement of 3.5×.
