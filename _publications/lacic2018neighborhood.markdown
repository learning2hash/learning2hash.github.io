---
layout: publication
title: 'Neighborhood Troubles: On The Value Of User Pre-filtering To Speed Up And
  Enhance Recommendations'
authors: Emanuel Lacic, Dominik Kowald, Elisabeth Lex
conference: Arxiv
year: 2018
bibkey: lacic2018neighborhood
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.06417'}]
tags: ["Recommender Systems"]
short_authors: Emanuel Lacic, Dominik Kowald, Elisabeth Lex
---
In this paper, we present work-in-progress on applying user pre-filtering to
speed up and enhance recommendations based on Collaborative Filtering. We
propose to pre-filter users in order to extract a smaller set of candidate
neighbors, who exhibit a high number of overlapping entities and to compute the
final user similarities based on this set. To realize this, we exploit features
of the high-performance search engine Apache Solr and integrate them into a
scalable recommender system. We have evaluated our approach on a dataset
gathered from Foursquare and our evaluation results suggest that our proposed
user pre-filtering step can help to achieve both a better runtime performance
as well as an increase in overall recommendation accuracy.