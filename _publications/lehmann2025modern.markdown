---
layout: publication
title: 'Modern Minimal Perfect Hashing: A Survey'
authors: Lehmann et al.
conference: IEEE GLOBECOM 2008 - 2008 IEEE Global Telecommunications Conference
year: 2025
bibkey: lehmann2025modern
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.06536'}]
tags: [Survey Paper, Hashing Methods, Evaluation, Efficiency And Optimization]
---
Given a set \\(S\\) of \\(n\\) keys, a perfect hash function for \\(S\\) maps the keys in \\(S\\) to the first \\(m \geq n\\) integers without collisions. It may return an arbitrary result for any key not in \\(S\\) and is called minimal if \\(m = n\\). The most important parameters are its space consumption, construction time, and query time. Years of research now enable modern perfect hash functions to be extremely fast to query, very space-efficient, and scale to billions of keys. Different approaches give different trade-offs between these aspects. For example, the smallest constructions get within 0.1% of the space lower bound of \\(log_2(e)\\) bits per key. Others are particularly fast to query, requiring only one memory access. Perfect hashing has many applications, for example to avoid collision resolution in static hash tables, and is used in databases, bioinformatics, and stringology.
  Since the last comprehensive survey in 1997, significant progress has been made. This survey covers the latest developments and provides a starting point for getting familiar with the topic. Additionally, our extensive experimental evaluation can serve as a guide to select a perfect hash function for use in applications.