---
layout: publication
title: 'Extended Few-shot Learning: Exploiting Existing Resources For Novel Tasks'
authors: Reza Esfandiarpoor, Amy Pu, Mohsen Hajabdollahi, Stephen H. Bach
conference: Arxiv
year: 2020
bibkey: esfandiarpoor2020extended
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.07176'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Esfandiarpoor et al.
---
In many practical few-shot learning problems, even though labeled examples
are scarce, there are abundant auxiliary datasets that potentially contain
useful information. We propose the problem of extended few-shot learning to
study these scenarios. We then introduce a framework to address the challenges
of efficiently selecting and effectively using auxiliary data in few-shot image
classification. Given a large auxiliary dataset and a notion of semantic
similarity among classes, we automatically select pseudo shots, which are
labeled examples from other classes related to the target task. We show that
naive approaches, such as (1) modeling these additional examples the same as
the target task examples or (2) using them to learn features via transfer
learning, only increase accuracy by a modest amount. Instead, we propose a
masking module that adjusts the features of auxiliary data to be more similar
to those of the target classes. We show that this masking module performs
better than naively modeling the support examples and transfer learning by 4.68
and 6.03 percentage points, respectively.