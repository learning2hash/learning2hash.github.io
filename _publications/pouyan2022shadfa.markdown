---
layout: publication
title: 'Shadfa 0.1: The Iranian Movie Knowledge Graph And Graph-embedding-based Recommender
  System'
authors: Rayhane Pouyan, Hadi Kalamati, Hannane Ebrahimian, Mohammad Karrabi, Mohammad-r.
  Akbarzadeh-t
conference: Arxiv
year: 2022
bibkey: pouyan2022shadfa
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.07822'}]
tags: ["Recommender Systems"]
short_authors: Pouyan et al.
---
Movies are a great source of entertainment. However, the problem arises when
one is trying to find the desired content within this vast amount of data which
is significantly increasing every year. Recommender systems can provide
appropriate algorithms to solve this problem. The content_based technique has
found popularity due to the lack of available user data in most cases.
Content_based recommender systems are based on the similarity of items'
demographic information; Term Frequency _ Inverse Document Frequency (TF_IDF)
and Knowledge Graph Embedding (KGE) are two approaches used to vectorize data
to calculate these similarities. In this paper, we propose a weighted
content_based movie RS by combining TF_IDF which is an appropriate approach for
embedding textual data such as plot/description, and KGE which is used to embed
named entities such as the director's name. The weights between features are
determined using a Genetic algorithm. Additionally, the Iranian movies dataset
is created by scraping data from movie_related websites. This dataset and the
structure of the FarsBase KG are used to create the MovieFarsBase KG which is a
component in the implementation process of the proposed content_based RS. Using
precision, recall, and F1 score metrics, this study shows that the proposed
approach outperforms the conventional approach that uses TF_IDF for embedding
all attributes.