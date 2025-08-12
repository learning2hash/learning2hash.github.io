---
layout: publication
title: Generative Imagination Elevates Machine Translation
authors: Quanyu Long, Mingxuan Wang, Lei Li
conference: 'Proceedings of the 2021 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies'
year: 2021
bibkey: long2020generative
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.09654'}]
tags: ["NAACL"]
short_authors: Quanyu Long, Mingxuan Wang, Lei Li
---
There are common semantics shared across text and images. Given a sentence in
a source language, whether depicting the visual scene helps translation into a
target language? Existing multimodal neural machine translation methods (MNMT)
require triplets of bilingual sentence - image for training and tuples of
source sentence - image for inference. In this paper, we propose ImagiT, a
novel machine translation method via visual imagination. ImagiT first learns to
generate visual representation from the source sentence, and then utilizes both
source sentence and the "imagined representation" to produce a target
translation. Unlike previous methods, it only needs the source sentence at the
inference time. Experiments demonstrate that ImagiT benefits from visual
imagination and significantly outperforms the text-only neural machine
translation baselines. Further analysis reveals that the imagination process in
ImagiT helps fill in missing information when performing the degradation
strategy.