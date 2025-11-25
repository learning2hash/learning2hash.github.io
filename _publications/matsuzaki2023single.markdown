---
layout: publication
title: Single-shot Global Localization Via Graph-theoretic Correspondence Matching
authors: Shigemichi Matsuzaki, Kenji Koide, Shuji Oishi, Masashi Yokozuka, Atsuhiko
  Banno
conference: Arxiv
year: 2023
bibkey: matsuzaki2023single
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.03641'}]
tags: ["Graph Based ANN"]
short_authors: Matsuzaki et al.
---
This paper describes a method of global localization based on graph-theoretic
association of instances between a query and the prior map. The proposed
framework employs correspondence matching based on the maximum clique problem
(MCP). The framework is potentially applicable to other map and/or query
modalities thanks to the graph-based abstraction of the problem, while many of
existing global localization methods rely on a query and the dataset in the
same modality. We implement it with a semantically labeled 3D point cloud map,
and a semantic segmentation image as a query. Leveraging the graph-theoretic
framework, the proposed method realizes global localization exploiting only the
map and the query. The method shows promising results on multiple large-scale
simulated maps of urban scenes.