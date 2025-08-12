---
layout: publication
title: Efficient Lock-free Durable Sets
authors: Yoav Zuriel, Michal Friedman, Gali Sheffi, Nachshon Cohen, Erez Petrank
conference: Proceedings of the ACM on Programming Languages
year: 2019
bibkey: zuriel2019efficient
citations: 48
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.02852'}]
tags: []
short_authors: Zuriel et al.
---
Non-volatile memory is expected to co-exist or replace DRAM in upcoming
architectures. Durable concurrent data structures for non-volatile memories are
essential building blocks for constructing adequate software for use with these
architectures. In this paper, we propose a new approach for durable concurrent
sets and use this approach to build the most efficient durable hash tables
available today. Evaluation shows a performance improvement factor of up to
3.3x over existing technology.