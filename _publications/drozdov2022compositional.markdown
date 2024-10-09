---
layout: publication
title: Compositional Semantic Parsing With Large Language Models
authors: Andrew Drozdov, Nathanael Schärli, Ekin Akyürek, Nathan Scales, Xinying Song, Xinyun Chen, Olivier Bousquet, Denny Zhou
conference: "Arxiv"
year: 2022
bibkey: drozdov2022compositional
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2209.15003v2"}
tags: ['ARXIV', 'Supervised']
---
Humans can reason compositionally when presented with new tasks. Previous research shows that appropriate prompting techniques enable large language models (LLMs) to solve artificial compositional generalization tasks such as SCAN. In this work we identify additional challenges in more realistic semantic parsing tasks with larger vocabulary and refine these prompting techniques to address them. Our best method is based on least-to-most prompting it decomposes the problem using prompting-based syntactic parsing then uses this decomposition to select appropriate exemplars and to sequentially generate the semantic parse. This method allows us to set a new state of the art for CFQ while requiring only 137; of the training data used by traditional approaches. Due to the general nature of our approach we expect similar efforts will lead to new results in other tasks and domains especially for knowledge-intensive applications.
