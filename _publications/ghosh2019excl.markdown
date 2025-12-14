---
layout: publication
title: 'Excl: Extractive Clip Localization Using Natural Language Descriptions'
authors: Soham Ghosh, Anuva Agarwal, Zarana Parekh, Alexander Hauptmann
conference: Arxiv
year: 2019
bibkey: ghosh2019excl
citations: 78
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.02755'}]
tags: [Evaluation, Datasets]
short_authors: Ghosh et al.
---
The task of retrieving clips within videos based on a given natural language
query requires cross-modal reasoning over multiple frames. Prior approaches
such as sliding window classifiers are inefficient, while text-clip similarity
driven ranking-based approaches such as segment proposal networks are far more
complicated. In order to select the most relevant video clip corresponding to
the given text description, we propose a novel extractive approach that
predicts the start and end frames by leveraging cross-modal interactions
between the text and video - this removes the need to retrieve and re-rank
multiple proposal segments. Using recurrent networks we encode the two
modalities into a joint representation which is then used in different variants
of start-end frame predictor networks. Through extensive experimentation and
ablative analysis, we demonstrate that our simple and elegant approach
significantly outperforms state of the art on two datasets and has comparable
performance on a third.