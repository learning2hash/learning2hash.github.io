---
layout: publication
title: Improving Dual-encoder Training Through Dynamic Indexes For Negative Mining
authors: Nicholas Monath, Manzil Zaheer, Kelsey Allen, Andrew McCallum
conference: Arxiv
year: 2023
bibkey: monath2023improving
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.15311'}]
tags: [Datasets]
short_authors: Monath et al.
---
Dual encoder models are ubiquitous in modern classification and retrieval.
Crucial for training such dual encoders is an accurate estimation of gradients
from the partition function of the softmax over the large output space; this
requires finding negative targets that contribute most significantly ("hard
negatives"). Since dual encoder model parameters change during training, the
use of traditional static nearest neighbor indexes can be sub-optimal. These
static indexes (1) periodically require expensive re-building of the index,
which in turn requires (2) expensive re-encoding of all targets using updated
model parameters. This paper addresses both of these challenges. First, we
introduce an algorithm that uses a tree structure to approximate the softmax
with provable bounds and that dynamically maintains the tree. Second, we
approximate the effect of a gradient update on target encodings with an
efficient Nystrom low-rank approximation. In our empirical study on datasets
with over twenty million targets, our approach cuts error by half in relation
to oracle brute-force negative mining. Furthermore, our method surpasses prior
state-of-the-art while using 150x less accelerator memory.