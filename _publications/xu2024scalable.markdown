---
layout: publication
title: Scalable Density-based Clustering With Random Projections
authors: Haochuan Xu, Ninh Pham
conference: Arxiv
year: 2024
bibkey: xu2024scalable
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.15679'}]
tags: []
short_authors: Haochuan Xu, Ninh Pham
---
We present sDBSCAN, a scalable density-based clustering algorithm in high dimensions with cosine distance. Utilizing the neighborhood-preserving property of random projections, sDBSCAN can quickly identify core points and their neighborhoods, the primary hurdle of density-based clustering. Theoretically, sDBSCAN outputs a clustering structure similar to DBSCAN under mild conditions with high probability. To further facilitate sDBSCAN, we present sOPTICS, a scalable OPTICS for interactive exploration of the intrinsic clustering structure. We also extend sDBSCAN and sOPTICS to L2, L1, \(\chi^2\), and Jensen-Shannon distances via random kernel features. Empirically, sDBSCAN is significantly faster and provides higher accuracy than many other clustering algorithms on real-world million-point data sets. On these data sets, sDBSCAN and sOPTICS run in a few minutes, while the scikit-learn's counterparts demand several hours or cannot run due to memory constraints.