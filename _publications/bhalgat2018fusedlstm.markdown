---
layout: publication
title: 'Fusedlstm: Fusing Frame-level And Video-level Features For Content-based Video
  Relevance Prediction'
authors: Yash Bhalgat
conference: Arxiv
year: 2018
bibkey: bhalgat2018fusedlstm
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.00136'}]
tags: ["Distance Metric Learning", "Evaluation"]
short_authors: Yash Bhalgat
---
This paper describes two of my best performing approaches on the
Content-based Video Relevance Prediction challenge. In the FusedLSTM based
approach, the inception-pool3 and the C3D-pool5 features are combined using an
LSTM and a dense layer to form embeddings with the objective to minimize the
triplet loss function. In the second approach, an Online Kernel Similarity
Learning method is proposed to learn a non-linear similarity measure to adhere
the relevance training data. The last section gives a complete comparison of
all the approaches implemented during this challenge, including the one
presented in the baseline paper.