---
layout: publication
title: On Semantic Similarity In Video Retrieval
authors: Michael Wray, Hazel Doughty, Dima Damen
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: wray2021on
citations: 45
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.10095'}]
tags: ["CVPR", "Datasets", "Evaluation", "Scalability", "Video Retrieval"]
short_authors: Michael Wray, Hazel Doughty, Dima Damen
---
Current video retrieval efforts all found their evaluation on an
instance-based assumption, that only a single caption is relevant to a query
video and vice versa. We demonstrate that this assumption results in
performance comparisons often not indicative of models' retrieval capabilities.
We propose a move to semantic similarity video retrieval, where (i) multiple
videos/captions can be deemed equally relevant, and their relative ranking does
not affect a method's reported performance and (ii) retrieved videos/captions
are ranked by their similarity to a query. We propose several proxies to
estimate semantic similarities in large-scale retrieval datasets, without
additional annotations. Our analysis is performed on three commonly used video
retrieval datasets (MSR-VTT, YouCook2 and EPIC-KITCHENS).