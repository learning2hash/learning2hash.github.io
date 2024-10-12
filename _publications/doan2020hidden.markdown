---
layout: publication
title: HM4 Hidden Markov Model With Memory Management For Visual Place Recognition
authors: Doan Anh-dzung, Latif Yasir, Chin Tat-jun, Reid Ian
conference: "Arxiv"
year: 2020
bibkey: doan2020hidden
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2011.00450"}
tags: ['ARXIV', 'LSH', 'Supervised']
---
Visual place recognition needs to be robust against appearance variability due to natural and man-made causes. Training data collection should thus be an ongoing process to allow continuous appearance changes to be recorded. However, this creates an unboundedly-growing database that poses time and memory scalability challenges for place recognition methods. To tackle the scalability issue for visual place recognition in autonomous driving, we develop a Hidden Markov Model approach with a two-tiered memory management. Our algorithm, dubbed HM\(^4\), exploits temporal look-ahead to transfer promising candidate images between passive storage and active memory when needed. The inference process takes into account both promising images and a coarse representations of the full database. We show that this allows constant time and space inference for a fixed coverage area. The coarse representations can also be updated incrementally to absorb new data. To further reduce the memory requirements, we derive a compact image representation inspired by Locality Sensitive Hashing (LSH). Through experiments on real world data, we demonstrate the excellent scalability and accuracy of the approach under appearance changes and provide comparisons against state-of-the-art techniques.
