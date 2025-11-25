---
layout: publication
title: Do You Like What I Like? Similarity Estimation In Proximity-based Mobile Social
  Networks
authors: Felix Beierle
conference: 2018 17th IEEE International Conference On Trust, Security And Privacy
  In Computing And Communications/ 12th IEEE International Conference On Big Data
  Science And Engineering (TrustCom/BigDataSE)
year: 2018
bibkey: beierle2018do
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.07651'}]
tags: ["Hashing Methods", "Privacy & Security", "Similarity Search"]
short_authors: Felix Beierle
---
While existing social networking services tend to connect people who know
each other, people show a desire to also connect to yet unknown people in
physical proximity. Existing research shows that people tend to connect to
similar people. Utilizing technology in order to stimulate human interaction
between strangers, we consider the scenario of two strangers meeting. On the
example of similarity in musical taste, we develop a solution for the problem
of similarity estimation in proximity-based mobile social networks. We show
that a single exchange of a probabilistic data structure between two devices
can closely estimate the similarity of two users - without the need to contact
a third-party server.We introduce metrics for fast and space-efficient
approximation of the Dice coefficient of two multisets - based on the
comparison of two Counting Bloom Filters or two Count-Min Sketches. Our
analysis shows that utilizing a single hash function minimizes the error when
comparing these probabilistic data structures. The size that should be chosen
for the data structure depends on the expected average number of unique input
elements. Using real user data, we show that a Counting Bloom Filter with a
single hash function and a length of 128 is sufficient to accurately estimate
the similarity between two multisets representing the musical tastes of two
users. Our approach is generalizable for any other similarity estimation of
frequencies represented as multisets.