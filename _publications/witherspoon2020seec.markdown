---
layout: publication
title: 'SEEC: Semantic Vector Federation Across Edge Computing Environments'
authors: Shalisha Witherspoon, Dean Steuer, Graham Bent, Nirmit Desai
conference: Arxiv
year: 2020
bibkey: witherspoon2020seec
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.13298'}]
tags: []
short_authors: Witherspoon et al.
---
Semantic vector embedding techniques have proven useful in learning semantic
representations of data across multiple domains. A key application enabled by
such techniques is the ability to measure semantic similarity between given
data samples and find data most similar to a given sample. State-of-the-art
embedding approaches assume all data is available on a single site. However, in
many business settings, data is distributed across multiple edge locations and
cannot be aggregated due to a variety of constraints. Hence, the applicability
of state-of-the-art embedding approaches is limited to freely shared datasets,
leaving out applications with sensitive or mission-critical data. This paper
addresses this gap by proposing novel unsupervised algorithms called
*SEEC* for learning and applying semantic vector embedding in a variety of
distributed settings. Specifically, for scenarios where multiple edge locations
can engage in joint learning, we adapt the recently proposed federated learning
techniques for semantic vector embedding. Where joint learning is not possible,
we propose novel semantic vector translation algorithms to enable semantic
query across multiple edge locations, each with its own semantic vector-space.
Experimental results on natural language as well as graph datasets show that
this may be a promising new direction.