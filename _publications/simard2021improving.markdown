---
layout: publication
title: Improving Few-shot Learning With Auxiliary Self-supervised Pretext Tasks
authors: Nathaniel Simard, Guillaume Lagrange
conference: Arxiv
year: 2021
bibkey: simard2021improving
citations: 3
additional_links: [{name: Code, url: 'https://github.com/nathanielsimard/improving-fs-ssl'},
  {name: Paper, url: 'https://arxiv.org/abs/2101.09825'}]
tags: ["Few Shot & Zero Shot", "Self-Supervised"]
short_authors: Nathaniel Simard, Guillaume Lagrange
---
Recent work on few-shot learning \cite\{tian2020rethinking\} showed that
quality of learned representations plays an important role in few-shot
classification performance. On the other hand, the goal of self-supervised
learning is to recover useful semantic information of the data without the use
of class labels. In this work, we exploit the complementarity of both paradigms
via a multi-task framework where we leverage recent self-supervised methods as
auxiliary tasks. We found that combining multiple tasks is often beneficial,
and that solving them simultaneously can be done efficiently. Our results
suggest that self-supervised auxiliary tasks are effective data-dependent
regularizers for representation learning. Our code is available at:
https://github.com/nathanielsimard/improving-fs-ssl.