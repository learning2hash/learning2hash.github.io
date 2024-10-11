---
layout: publication
title: How Should We Evaluate Supervised Hashing
authors: Sablayrolles Alexandre, Douze Matthijs, Jégou Hervé, Usunier Nicolas
conference: "Arxiv"
year: 2016
bibkey: sablayrolles2016how
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1609.06753"}
tags: ['ARXIV', 'Supervised']
---
Hashing produces compact representations for documents, to perform tasks like classification or retrieval based on these short codes. When hashing is supervised, the codes are trained using labels on the training data. This paper first shows that the evaluation protocols used in the literature for supervised hashing are not satisfactory: we show that a trivial solution that encodes the output of a classifier significantly outperforms existing supervised or semi-supervised methods, while using much shorter codes. We then propose two alternative protocols for supervised hashing: one based on retrieval on a disjoint set of classes, and another based on transfer learning to new classes. We provide two baseline methods for image-related tasks to assess the performance of (semi-)supervised hashing: without coding and with unsupervised codes. These baselines give a lower- and upper-bound on the performance of a supervised hashing scheme.
