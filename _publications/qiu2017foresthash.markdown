---
layout: publication
title: Foresthash Semantic Hashing With Shallow Random Forests And Tiny Convolutional Networks
authors: Qiu Qiang, Lezama Jose, Bronstein Alex, Sapiro Guillermo
conference: "Arxiv"
year: 2017
bibkey: qiu2017foresthash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1711.08364"}
tags: ['ARXIV', 'CNN', 'Image Retrieval', 'Independent']
---
Hash codes are efficient data representations for coping with the ever growing amounts of data. In this paper we introduce a random forest semantic hashing scheme that embeds tiny convolutional neural networks (CNN) into shallow random forests with near45;optimal information45;theoretic code aggregation among trees. We start with a simple hashing scheme where random trees in a forest act as hashing functions by setting 1 for the visited tree leaf and 0 for the rest. We show that traditional random forests fail to generate hashes that preserve the underlying similarity between the trees rendering the random forests approach to hashing challenging. To address this we propose to first randomly group arriving classes at each tree split node into two groups obtaining a significantly simplified two45;class classification problem which can be handled using a light45;weight CNN weak learner. Such random class grouping scheme enables code uniqueness by enforcing each class to share its code with different classes in different trees. A non45;conventional low45;rank loss is further adopted for the CNN weak learners to encourage code consistency by minimizing intra45;class variations and maximizing inter45;class distance for the two random class groups. Finally we introduce an information45;theoretic approach for aggregating codes of individual trees into a single hash code producing a near45;optimal unique hash for each class. The proposed approach significantly outperforms state45;of45;the45;art hashing methods for image retrieval tasks on large45;scale public datasets while performing at the level of other state45;of45;the45;art image classification techniques while utilizing a more compact and efficient scalable representation. This work proposes a principled and robust procedure to train and deploy in parallel an ensemble of light45;weight CNNs instead of simply going deeper.
