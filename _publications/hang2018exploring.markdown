---
layout: publication
title: Exploring Student Check-in Behavior For Improved Point-of-interest Prediction
authors: Mengyue Hang, Ian Pytlarz, Jennifer Neville
conference: Proceedings of the 24th ACM SIGKDD International Conference on Knowledge
  Discovery &amp; Data Mining
year: 2018
bibkey: hang2018exploring
citations: 54
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.06912'}]
tags: [Evaluation, KDD, Graph-based ANN, Datasets]
short_authors: Mengyue Hang, Ian Pytlarz, Jennifer Neville
---
With the availability of vast amounts of user visitation history on
location-based social networks (LBSN), the problem of Point-of-Interest (POI)
prediction has been extensively studied. However, much of the research has been
conducted solely on voluntary checkin datasets collected from social apps such
as Foursquare or Yelp. While these data contain rich information about
recreational activities (e.g., restaurants, nightlife, and entertainment),
information about more prosaic aspects of people's lives is sparse. This not
only limits our understanding of users' daily routines, but more importantly
the modeling assumptions developed based on characteristics of recreation-based
data may not be suitable for richer check-in data. In this work, we present an
analysis of education "check-in" data using WiFi access logs collected at
Purdue University. We propose a heterogeneous graph-based method to encode the
correlations between users, POIs, and activities, and then jointly learn
embeddings for the vertices. We evaluate our method compared to previous
state-of-the-art POI prediction methods, and show that the assumptions made by
previous methods significantly degrade performance on our data with dense(r)
activity signals. We also show how our learned embeddings could be used to
identify similar students (e.g., for friend suggestions).