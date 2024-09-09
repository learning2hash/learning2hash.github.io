---
layout: publication
title: "Online Hashing"
authors: Huang Long-Kai, Yang Qiang, Zheng Wei-Shi
conference: "Arxiv"
year: 2017
bibkey: huang2017online
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1704.01897"}
tags: ['ARXIV', 'TIP']
---
Although hash function learning algorithms have achieved great success in recent
years, most existing hash models are off-line, which are not suitable for
processing sequential or online data. To address this problem, this work
proposes an online hash model to accommodate data coming in stream for online
learning. Specifically, a new loss function is proposed to measure the
similarity loss between a pair of data samples in hamming space. Then, a
structured hash model is derived and optimized in a passive-aggressive way.
Theoretical analysis on the upper bound of the cumulative loss for the proposed
online hash model is provided. Furthermore, we extend our online hashing from a
single-model to a multi-model online hashing that trains multiple models so as
to retain diverse online hashing models in order to avoid biased update. The
competitive efficiency and effectiveness of the proposed online hash models are
verified through extensive experiments on several large-scale datasets as
compared to related hashing methods.
