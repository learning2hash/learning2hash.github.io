---
layout: publication
title: Local Propagation For Few-shot Learning
authors: Yann Lifchitz, Yannis Avrithis, Sylvaine Picard
conference: 2020 25th International Conference on Pattern Recognition (ICPR)
year: 2021
bibkey: lifchitz2021local
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.01480'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Yann Lifchitz, Yannis Avrithis, Sylvaine Picard
---
The challenge in few-shot learning is that available data is not enough to
capture the underlying distribution. To mitigate this, two emerging directions
are (a) using local image representations, essentially multiplying the amount
of data by a constant factor, and (b) using more unlabeled data, for instance
by transductive inference, jointly on a number of queries. In this work, we
bring these two ideas together, introducing *local propagation*. We treat
local image features as independent examples, we build a graph on them and we
use it to propagate both the features themselves and the labels, known and
unknown. Interestingly, since there is a number of features per image, even a
single query gives rise to transductive inference. As a result, we provide a
universally safe choice for few-shot inference under both non-transductive and
transductive settings, improving accuracy over corresponding methods. This is
in contrast to existing solutions, where one needs to choose the method
depending on the quantity of available data.