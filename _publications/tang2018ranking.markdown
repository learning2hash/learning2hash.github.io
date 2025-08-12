---
layout: publication
title: 'Ranking Distillation: Learning Compact Ranking Models With High Performance
  For Recommender System'
authors: Jiaxi Tang, Ke Wang
conference: Arxiv
year: 2018
bibkey: tang2018ranking
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.07428'}]
tags: []
short_authors: Jiaxi Tang, Ke Wang
---
We propose a novel way to train ranking models, such as recommender systems,
that are both effective and efficient. Knowledge distillation (KD) was shown to
be successful in image recognition to achieve both effectiveness and
efficiency. We propose a KD technique for learning to rank problems, called
*ranking distillation (RD)*. Specifically, we train a smaller student
model to learn to rank documents/items from both the training data and the
supervision of a larger teacher model. The student model achieves a similar
ranking performance to that of the large teacher model, but its smaller model
size makes the online inference more efficient. RD is flexible because it is
orthogonal to the choices of ranking models for the teacher and student. We
address the challenges of RD for ranking problems. The experiments on public
data sets and state-of-the-art recommendation models showed that RD achieves
its design purposes: the student model learnt with RD has a model size less
than half of the teacher model while achieving a ranking performance similar to
the teacher model and much better than the student model learnt without RD.