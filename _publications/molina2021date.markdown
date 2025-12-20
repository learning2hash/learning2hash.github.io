---
layout: publication
title: 'Date Estimation In The Wild Of Scanned Historical Photos: An Image Retrieval
  Approach'
authors: "Adri\xE0 Molina, Pau Riba, Lluis Gomez, Oriol Ramos-Terrades, Josep Llad\xF3\
  s"
conference: Lecture Notes in Computer Science
year: 2021
bibkey: molina2021date
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.05618'}]
tags: ["Evaluation", "Image Retrieval"]
short_authors: Molina et al.
---
This paper presents a novel method for date estimation of historical
photographs from archival sources. The main contribution is to formulate the
date estimation as a retrieval task, where given a query, the retrieved images
are ranked in terms of the estimated date similarity. The closer are their
embedded representations the closer are their dates. Contrary to the
traditional models that design a neural network that learns a classifier or a
regressor, we propose a learning objective based on the nDCG ranking metric. We
have experimentally evaluated the performance of the method in two different
tasks: date estimation and date-sensitive image retrieval, using the DEW public
database, overcoming the baseline methods.