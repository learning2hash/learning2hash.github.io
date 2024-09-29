---
layout: publication
title: Attributes Grouping And Mining Hashing For Fine45;grained Image Retrieval
authors: Lu Xin, Chen Shikun, Cao Yichao, Zhou Xin, Lu Xiaobo
conference: "Proceedings of the"
year: 2023
bibkey: lu2023attributes
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2311.06067"}
tags: ['AAAI', 'Image Retrieval', 'Independent']
---
In recent years hashing methods have been popular in the large45;scale media search for low storage and strong representation capabilities. To describe objects with similar overall appearance but subtle differences more and more studies focus on hashing45;based fine45;grained image retrieval. Existing hashing networks usually generate both local and global features through attention guidance on the same deep activation tensor which limits the diversity of feature representations. To handle this limitation we substitute convolutional descriptors for attention45;guided features and propose an Attributes Grouping and Mining Hashing (AGMH) which groups and embeds the category45;specific visual attributes in multiple descriptors to generate a comprehensive feature representation for efficient fine45;grained image retrieval. Specifically an Attention Dispersion Loss (ADL) is designed to force the descriptors to attend to various local regions and capture diverse subtle details. Moreover we propose a Stepwise Interactive External Attention (SIEA) to mine critical attributes in each descriptor and construct correlations between fine45;grained attributes and objects. The attention mechanism is dedicated to learning discrete attributes which will not cost additional computations in hash codes generation. Finally the compact binary codes are learned by preserving pairwise similarities. Experimental results demonstrate that AGMH consistently yields the best performance against state45;of45;the45;art methods on fine45;grained benchmark datasets.
