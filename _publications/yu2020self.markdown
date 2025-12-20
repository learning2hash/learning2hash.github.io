---
layout: publication
title: Self-supervised Asymmetric Deep Hashing With Margin-scalable Constraint
authors: Zhengyang Yu, Song Wu, Zhihao Dou, Erwin M. Bakker
conference: Arxiv
year: 2020
bibkey: yu2020self
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.03820'}]
tags: ["Distance Metric Learning", "Efficiency", "Hashing Methods", "Self-Supervised", "Supervised"]
short_authors: Yu et al.
---
Due to its effectivity and efficiency, deep hashing approaches are widely
used for large-scale visual search. However, it is still challenging to produce
compact and discriminative hash codes for images associated with multiple
semantics for two main reasons, 1) similarity constraints designed in most of
the existing methods are based upon an oversimplified similarity
assignment(i.e., 0 for instance pairs sharing no label, 1 for instance pairs
sharing at least 1 label), 2) the exploration in multi-semantic relevance are
insufficient or even neglected in many of the existing methods. These problems
significantly limit the discrimination of generated hash codes. In this paper,
we propose a novel self-supervised asymmetric deep hashing method with a
margin-scalable constraint(SADH) approach to cope with these problems. SADH
implements a self-supervised network to sufficiently preserve semantic
information in a semantic feature dictionary and a semantic code dictionary for
the semantics of the given dataset, which efficiently and precisely guides a
feature learning network to preserve multilabel semantic information using an
asymmetric learning strategy. By further exploiting semantic dictionaries, a
new margin-scalable constraint is employed for both precise similarity
searching and robust hash code generation. Extensive empirical research on four
popular benchmarks validates the proposed method and shows it outperforms
several state-of-the-art approaches.