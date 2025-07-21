---
layout: publication
title: 'Node2bits: Compact Time- And Attribute-aware Node Representations For User
  Stitching'
authors: Jin et al.
conference: Lecture Notes in Computer Science
year: 2020
bibkey: jin2020node2bits
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.08572'}]
---
Identity stitching, the task of identifying and matching various online
references (e.g., sessions over different devices and timespans) to the same
user in real-world web services, is crucial for personalization and
recommendations. However, traditional user stitching approaches, such as
grouping or blocking, require quadratic pairwise comparisons between a massive
number of user activities, thus posing both computational and storage
challenges. Recent works, which are often application-specific, heuristically
seek to reduce the amount of comparisons, but they suffer from low precision
and recall. To solve the problem in an application-independent way, we take a
heterogeneous network-based approach in which users (nodes) interact with
content (e.g., sessions, websites), and may have attributes (e.g., location).
We propose node2bits, an efficient framework that represents multi-dimensional
features of node contexts with binary hashcodes. node2bits leverages
feature-based temporal walks to encapsulate short- and long-term interactions
between nodes in heterogeneous web networks, and adopts SimHash to obtain
compact, binary representations and avoid the quadratic complexity for
similarity search. Extensive experiments on large-scale real networks show that
node2bits outperforms traditional techniques and existing works that generate
real-valued embeddings by up to 5.16% in F1 score on user stitching, while
taking only up to 1.56% as much storage.