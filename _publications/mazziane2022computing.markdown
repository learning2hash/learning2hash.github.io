---
layout: publication
title: Computing The Hit Rate Of Similarity Caching
authors: Younes Ben Mazziane, Sara Alouf, Giovanni Neglia, Daniel Sadoc Menasche
conference: GLOBECOM 2022 - 2022 IEEE Global Communications Conference
year: 2022
bibkey: mazziane2022computing
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.03174'}]
tags: []
short_authors: Mazziane et al.
---
Similarity caching allows requests for an item \(i\) to be served by a
similar item \(i'\). Applications include recommendation systems, multimedia
retrieval, and machine learning. Recently, many similarity caching policies
have been proposed, but still we do not know how to compute the hit rate even
for the simplest policies, like SIM-LRU and RND-LRU that are straightforward
modifications of classical caching algorithms. This paper proposes the first
algorithm to compute the hit rate of similarity caching policies under the
independent reference model for the request process. In particular, our work
shows how to extend the popular TTL approximation from classic caching to
similarity caching. The algorithm is evaluated on both synthetic and real world
traces.