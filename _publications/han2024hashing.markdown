---
layout: publication
title: "Hashing based Contrastive Learning for Virtual Screening"
authors: Han Jin, Hong Yun, Li Wu-Jun
conference: Arxiv
year: 2024
bibkey: han2024hashing
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2407.19790"}
tags: ['ARXIV', 'Deep Learning']
---
Virtual screening (VS) is a critical step in computer-aided drug discovery, aiming to identify molecules that bind to a specific target receptor like protein. Traditional VS methods, such as docking, are often too time-consuming for screening large-scale molecular databases. Recent advances in deep learning have demonstrated that learning vector representations for both proteins and molecules using contrastive learning can outperform traditional docking methods. However, given that target databases often contain billions of molecules, real-valued vector representations adopted by existing methods can still incur significant memory and time costs in VS. To address this problem, in this paper we propose a hashing-based contrastive learning method, called DrugHash, for VS. DrugHash treats VS as a retrieval task that uses efficient binary hash codes for retrieval. In particular, DrugHash designs a simple yet effective hashing strategy to enable end-to-end learning of binary hash codes for both protein and molecule modalities, which can dramatically reduce the memory and time costs with higher accuracy compared with existing methods. Experimental results show that DrugHash can outperform existing methods to achieve state-of-the-art accuracy, with a memory saving of 32\$\times\$ and a speed improvement of 3.5\$\times\$.