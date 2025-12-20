---
layout: publication
title: 'Polar Ducks And Where To Find Them: Enhancing Entity Linking With Duck Typing
  And Polar Box Embeddings'
authors: "Mattia Atzeni, Mikhail Plekhanov, Fr\xE9d\xE9ric A. Dreyer, Nora Kassner,\
  \ Simone Merello, Louis Martin, Nicola Cancedda"
conference: Proceedings of the 2023 Conference on Empirical Methods in Natural Language
  Processing
year: 2023
bibkey: atzeni2023polar
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.12027'}]
tags: ["EMNLP", "Evaluation", "Scalability"]
short_authors: Atzeni et al.
---
Entity linking methods based on dense retrieval are an efficient and widely
used solution in large-scale applications, but they fall short of the
performance of generative models, as they are sensitive to the structure of the
embedding space. In order to address this issue, this paper introduces DUCK, an
approach to infusing structural information in the space of entity
representations, using prior knowledge of entity types. Inspired by duck typing
in programming languages, we propose to define the type of an entity based on
the relations that it has with other entities in a knowledge graph. Then,
porting the concept of box embeddings to spherical polar coordinates, we
propose to represent relations as boxes on the hypersphere. We optimize the
model to cluster entities of similar type by placing them inside the boxes
corresponding to their relations. Our experiments show that our method sets new
state-of-the-art results on standard entity-disambiguation benchmarks, it
improves the performance of the model by up to 7.9 F1 points, outperforms other
type-aware approaches, and matches the results of generative models with 18
times more parameters.