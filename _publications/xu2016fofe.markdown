---
layout: publication
title: A Fofe-based Local Detection Approach For Named Entity Recognition And Mention
  Detection
authors: Mingbin Xu, Hui Jiang
conference: Arxiv
year: 2016
bibkey: xu2016fofe
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.00801'}]
tags: []
short_authors: Mingbin Xu, Hui Jiang
---
In this paper, we study a novel approach for named entity recognition (NER)
and mention detection in natural language processing. Instead of treating NER
as a sequence labelling problem, we propose a new local detection approach,
which rely on the recent fixed-size ordinally forgetting encoding (FOFE) method
to fully encode each sentence fragment and its left/right contexts into a
fixed-size representation. Afterwards, a simple feedforward neural network is
used to reject or predict entity label for each individual fragment. The
proposed method has been evaluated in several popular NER and mention detection
tasks, including the CoNLL 2003 NER task and TAC-KBP2015 and TAC-KBP2016
Tri-lingual Entity Discovery and Linking (EDL) tasks. Our methods have yielded
pretty strong performance in all of these examined tasks. This local detection
approach has shown many advantages over the traditional sequence labelling
methods.