---
layout: publication
title: Pattern Spotting In Historical Documents Using Convolutional Models
authors: "Ignacio \xDAbeda, Jose M. Saavedra, St\xE9phane Nicolas, Caroline Petitjean,\
  \ Laurent Heutte"
conference: Proceedings of the 5th International Workshop on Historical Document Imaging
  and Processing
year: 2019
bibkey: "\xFAbeda2019pattern"
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.08580'}]
tags: []
short_authors: "\xDAbeda et al."
---
Pattern spotting consists of searching in a collection of historical document
images for occurrences of a graphical object using an image query. Contrary to
object detection, no prior information nor predefined class is given about the
query so training a model of the object is not feasible. In this paper, a
convolutional neural network approach is proposed to tackle this problem. We
use RetinaNet as a feature extractor to obtain multiscale embeddings of the
regions of the documents and also for the queries. Experiments conducted on the
DocExplore dataset show that our proposal is better at locating patterns and
requires less storage for indexing images than the state-of-the-art system, but
fails at retrieving some pages containing multiple instances of the query.