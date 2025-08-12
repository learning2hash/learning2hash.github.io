---
layout: publication
title: 'Who Is Killed By Police: Introducing Supervised Attention For Hierarchical
  Lstms'
authors: Minh Nguyen, Thien Huu Nguyen
conference: Arxiv
year: 2018
bibkey: nguyen2018who
citations: 34
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.03409'}]
tags: ["Supervised"]
short_authors: Minh Nguyen, Thien Huu Nguyen
---
Finding names of people killed by police has become increasingly important as
police shootings get more and more public attention (police killing detection).
Unfortunately, there has been not much work in the literature addressing this
problem. The early work in this field \cite\{keith2017identifying\} proposed a
distant supervision framework based on Expectation Maximization (EM) to deal
with the multiple appearances of the names in documents. However, such EM-based
framework cannot take full advantages of deep learning models, necessitating
the use of hand-designed features to improve the detection performance. In this
work, we present a novel deep learning method to solve the problem of police
killing recognition. The proposed method relies on hierarchical LSTMs to model
the multiple sentences that contain the person names of interests, and
introduce supervised attention mechanisms based on semantical word lists and
dependency trees to upweight the important contextual words. Our experiments
demonstrate the benefits of the proposed model and yield the state-of-the-art
performance for police killing detection.