---
layout: publication
title: Large-scale Vandalism Detection With Linear Classifiers - The Conkerberry Vandalism
  Detector At WSDM Cup 2017
authors: Alexey Grigorev
conference: Arxiv
year: 2017
bibkey: grigorev2017large
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.06920'}]
tags: ["Evaluation", "Scalability"]
short_authors: Alexey Grigorev
---
Nowadays many artificial intelligence systems rely on knowledge bases for
enriching the information they process. Such Knowledge Bases are usually
difficult to obtain and therefore they are crowdsourced: they are available for
everyone on the internet to suggest edits and add new information.
Unfortunately, they are sometimes targeted by vandals who put inaccurate or
offensive information there. This is especially bad for the systems that use
these Knowledge Bases: for them it is important to use reliable information to
make correct inferences.
  One of such knowledge bases is Wikidata, and to fight vandals the organizers
of WSDM Cup 2017 challenged participants to build a model for detecting
mistrustful edits. In this paper we present the second place solution to the
cup: we show that it is possible to achieve competitive performance with simple
linear classification. With our approach we can achieve AU ROC of 0.938 on the
test data. Additionally, compared to other approaches, ours is significantly
faster. The solution is made available on GitHub.