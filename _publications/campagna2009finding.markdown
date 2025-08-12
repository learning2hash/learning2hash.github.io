---
layout: publication
title: Finding Associations And Computing Similarity Via Biased Pair Sampling
authors: Andrea Campagna, Rasmus Pagh
conference: Knowledge and Information Systems
year: 2011
bibkey: campagna2009finding
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/0910.0112'}]
tags: ["Efficiency"]
short_authors: Andrea Campagna, Rasmus Pagh
---
This version is ***superseded*** by a full version that can be found at
http://www.itu.dk/people/pagh/papers/mining-jour.pdf, which contains stronger
theoretical results and fixes a mistake in the reporting of experiments.
  Abstract: Sampling-based methods have previously been proposed for the
problem of finding interesting associations in data, even for low-support
items. While these methods do not guarantee precise results, they can be vastly
more efficient than approaches that rely on exact counting. However, for many
similarity measures no such methods have been known. In this paper we show how
a wide variety of measures can be supported by a simple biased sampling method.
The method also extends to find high-confidence association rules. We
demonstrate theoretically that our method is superior to exact methods when the
threshold for "interesting similarity/confidence" is above the average pairwise
similarity/confidence, and the average support is not too low. Our method is
particularly good when transactions contain many items. We confirm in
experiments on standard association mining benchmarks that this gives a
significant speedup on real data sets (sometimes much larger than the
theoretical guarantees). Reductions in computation time of over an order of
magnitude, and significant savings in space, are observed.