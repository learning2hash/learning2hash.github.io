---
layout: publication
title: 'Music Recommendations In Hyperbolic Space: An Application Of Empirical Bayes
  And Hierarchical Poincar\''e Embeddings'
authors: Tim Schmeier, Sam Garrett, Joseph Chisari, Brett Vintch
conference: Thirteenth ACM Conference on Recommender Systems (RecSys 19) September
  16--20 2019 Copenhagen Denmark
year: 2019
bibkey: schmeier2019music
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.12378'}]
tags: []
short_authors: Schmeier et al.
---
Matrix Factorization (MF) is a common method for generating recommendations,
where the proximity of entities like users or items in the embedded space
indicates their similarity to one another. Though almost all applications
implicitly use a Euclidean embedding space to represent two entity types,
recent work has suggested that a hyperbolic Poincar\'e ball may be more well
suited to representing multiple entity types, and in particular, hierarchies.
We describe a novel method to embed a hierarchy of related music entities in
hyperbolic space. We also describe how a parametric empirical Bayes approach
can be used to estimate link reliability between entities in the hierarchy.
Applying these methods together to build personalized playlists for users in a
digital music service yielded a large and statistically significant increase in
performance during an A/B test, as compared to the Euclidean model.