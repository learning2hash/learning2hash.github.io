---
layout: publication
title: Tag Embedding Based Personalized Point Of Interest Recommendation System
authors: Suraj Agrawal, Dwaipayan Roy, Mandar Mitra
conference: Information Processing &amp; Management
year: 2020
bibkey: agrawal2020tag
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.06389'}]
tags: ["Datasets", "Recommender Systems"]
short_authors: Suraj Agrawal, Dwaipayan Roy, Mandar Mitra
---
Personalized Point of Interest recommendation is very helpful for satisfying
users' needs at new places. In this article, we propose a tag embedding based
method for Personalized Recommendation of Point Of Interest. We model the
relationship between tags corresponding to Point Of Interest. The model
provides representative embedding corresponds to a tag in a way that related
tags will be closer. We model Point of Interest-based on tag embedding and also
model the users (user profile) based on the Point Of Interest rated by them.
finally, we rank the user's candidate Point Of Interest based on cosine
similarity between user's embedding and Point of Interest's embedding. Further,
we find the parameters required to model user by discrete optimizing over
different measures (like ndcg@5, MRR, ...). We also analyze the result while
considering the same parameters for all users and individual parameters for
each user. Along with it we also analyze the effect on the result while
changing the dataset to model the relationship between tags. Our method also
minimizes the privacy leak issue. We used TREC Contextual Suggestion 2016 Phase
2 dataset and have significant improvement over all the measures on the state
of the art method. It improves ndcg@5 by 12.8%, p@5 by 4.3%, and MRR by 7.8%,
which shows the effectiveness of the method.