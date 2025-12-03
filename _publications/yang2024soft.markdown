---
layout: publication
title: Soft-prompting With Graph-of-thought For Multi-modal Representation Learning
authors: Juncheng Yang, Zuchao Li, Shuai Xie, Wei Yu, Shijun Li, Bo Du
conference: Arxiv
year: 2024
bibkey: yang2024soft
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.04538'}]
tags: ["Evaluation", "Image Retrieval"]
short_authors: Yang et al.
---
The chain-of-thought technique has been received well in multi-modal tasks.
It is a step-by-step linear reasoning process that adjusts the length of the
chain to improve the performance of generated prompts. However, human thought
processes are predominantly non-linear, as they encompass multiple aspects
simultaneously and employ dynamic adjustment and updating mechanisms.
Therefore, we propose a novel Aggregation-Graph-of-Thought (AGoT) mechanism for
soft-prompt tuning in multi-modal representation learning. The proposed AGoT
models the human thought process not only as a chain but also models each step
as a reasoning aggregation graph to cope with the overlooked multiple aspects
of thinking in single-step reasoning. This turns the entire reasoning process
into prompt aggregation and prompt flow operations. Experiments show that our
multi-modal model enhanced with AGoT soft-prompting achieves good results in
several tasks such as text-image retrieval, visual question answering, and
image recognition. In addition, we demonstrate that it has good domain
generalization performance due to better reasoning.