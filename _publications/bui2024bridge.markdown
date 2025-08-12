---
layout: publication
title: 'BRIDGE: Bundle Recommendation Via Instruction-driven Generation'
authors: Tuan-Nghia Bui, Huy-Son Nguyen, Cam-van Nguyen Thi, Hoang-Quynh Le, Duc-Trong
  Le
conference: Arxiv
year: 2024
bibkey: bui2024bridge
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.18092'}]
tags: ["Recommender Systems"]
short_authors: Bui et al.
---
Bundle recommendation aims to suggest a set of interconnected items to users.
However, diverse interaction types and sparse interaction matrices often pose
challenges for previous approaches in accurately predicting user-bundle
adoptions. Inspired by the distant supervision strategy and generative
paradigm, we propose BRIDGE, a novel framework for bundle recommendation. It
consists of two main components namely the correlation-based item clustering
and the pseudo bundle generation modules. Inspired by the distant supervision
approach, the former is to generate more auxiliary information, e.g.,
instructive item clusters, for training without using external data. This
information is subsequently aggregated with collaborative signals from user
historical interactions to create pseudo `ideal' bundles. This capability
allows BRIDGE to explore all aspects of bundles, rather than being limited to
existing real-world bundles. It effectively bridging the gap between user
imagination and predefined bundles, hence improving the bundle recommendation
performance. Experimental results validate the superiority of our models over
state-of-the-art ranking-based methods across five benchmark datasets.