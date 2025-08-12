---
layout: publication
title: Bundle Optimization For Multi-aspect Embedding
authors: Qiong Zeng, Baoquan Chen, Yanir Kleiman, Daniel Cohen-Or, Yangyan Li
conference: Arxiv
year: 2017
bibkey: zeng2017bundle
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.09928'}]
tags: []
short_authors: Zeng et al.
---
Understanding semantic similarity among images is the core of a wide range of
computer vision applications. An important step towards this goal is to collect
and learn human perceptions. Interestingly, the semantic context of images is
often ambiguous as images can be perceived with emphasis on different aspects,
which may be contradictory to each other.
  In this paper, we present a method for learning the semantic similarity among
images, inferring their latent aspects and embedding them into multi-spaces
corresponding to their semantic aspects.
  We consider the multi-embedding problem as an optimization function that
evaluates the embedded distances with respect to the qualitative clustering
queries. The key idea of our approach is to collect and embed qualitative
measures that share the same aspects in bundles. To ensure similarity aspect
sharing among multiple measures, image classification queries are presented to,
and solved by users. The collected image clusters are then converted into
bundles of tuples, which are fed into our bundle optimization algorithm that
jointly infers the aspect similarity and multi-aspect embedding. Extensive
experimental results show that our approach significantly outperforms
state-of-the-art multi-embedding approaches on various datasets, and scales
well for large multi-aspect similarity measures.