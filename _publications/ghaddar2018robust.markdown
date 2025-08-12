---
layout: publication
title: Robust Lexical Features For Improved Neural Network Named-entity Recognition
authors: Abbas Ghaddar, Philippe Langlais
conference: Arxiv
year: 2018
bibkey: ghaddar2018robust
citations: 51
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1806.03489'}]
tags: []
short_authors: Abbas Ghaddar, Philippe Langlais
---
Neural network approaches to Named-Entity Recognition reduce the need for
carefully hand-crafted features. While some features do remain in
state-of-the-art systems, lexical features have been mostly discarded, with the
exception of gazetteers. In this work, we show that this is unfair: lexical
features are actually quite useful. We propose to embed words and entity types
into a low-dimensional vector space we train from annotated data produced by
distant supervision thanks to Wikipedia. From this, we compute - offline - a
feature vector representing each word. When used with a vanilla recurrent
neural network model, this representation yields substantial improvements. We
establish a new state-of-the-art F1 score of 87.95 on ONTONOTES 5.0, while
matching state-of-the-art performance with a F1 score of 91.73 on the
over-studied CONLL-2003 dataset.