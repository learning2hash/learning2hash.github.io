---
layout: publication
title: Revisiting The Role Of Similarity And Dissimilarity In Best Counter Argument
  Retrieval
authors: Hongguang Shi, Shuirong Cao, Cam-Tu Nguyen
conference: Arxiv
year: 2023
bibkey: shi2023revisiting
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.08807'}]
tags: ["Distance Metric Learning"]
short_authors: Hongguang Shi, Shuirong Cao, Cam-Tu Nguyen
---
This paper studies the task of best counter-argument retrieval given an input
argument. Following the definition that the best counter-argument addresses the
same aspects as the input argument while having the opposite stance, we aim to
develop an efficient and effective model for scoring counter-arguments based on
similarity and dissimilarity metrics. We first conduct an experimental study on
the effectiveness of available scoring methods, including traditional
Learning-To-Rank (LTR) and recent neural scoring models. We then propose
Bipolar-encoder, a novel BERT-based model to learn an optimal representation
for simultaneous similarity and dissimilarity. Experimental results show that
our proposed method can achieve the accuracy@1 of 49.04%, which significantly
outperforms other baselines by a large margin. When combined with an
appropriate caching technique, Bipolar-encoder is comparably efficient at
prediction time.