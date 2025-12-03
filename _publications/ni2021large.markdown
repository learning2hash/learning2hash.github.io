---
layout: publication
title: Large Dual Encoders Are Generalizable Retrievers
authors: "Jianmo Ni, Chen Qu, Jing Lu, Zhuyun Dai, Gustavo Hern\xE1ndez \xC1brego,\
  \ Ji Ma, Vincent Y. Zhao, Yi Luan, Keith B. Hall, Ming-Wei Chang, Yinfei Yang"
conference: Arxiv
year: 2021
bibkey: ni2021large
citations: 5
additional_links: [{name: Code, url: 'https://tfhub.dev/google/collections/gtr/1'},
  {name: Paper, url: 'https://arxiv.org/abs/2112.07899'}]
tags: ["Datasets", "Evaluation", "Supervised"]
short_authors: Ni et al.
---
It has been shown that dual encoders trained on one domain often fail to
generalize to other domains for retrieval tasks. One widespread belief is that
the bottleneck layer of a dual encoder, where the final score is simply a
dot-product between a query vector and a passage vector, is too limited to make
dual encoders an effective retrieval model for out-of-domain generalization. In
this paper, we challenge this belief by scaling up the size of the dual encoder
model \{\em while keeping the bottleneck embedding size fixed.\} With multi-stage
training, surprisingly, scaling up the model size brings significant
improvement on a variety of retrieval tasks, especially for out-of-domain
generalization. Experimental results show that our dual encoders,
\textbf\{G\}eneralizable \textbf\{T\}5-based dense \textbf\{R\}etrievers (GTR),
outperform %ColBERT~\cite\{khattab2020colbert\} and existing sparse and dense
retrievers on the BEIR dataset~\cite\{thakur2021beir\} significantly. Most
surprisingly, our ablation study finds that GTR is very data efficient, as it
only needs 10% of MS Marco supervised data to achieve the best out-of-domain
performance. All the GTR models are released at
https://tfhub.dev/google/collections/gtr/1.