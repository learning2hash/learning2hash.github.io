---
layout: publication
title: Finding People's Professions And Nationalities Using Distant Supervision -
  The FMI@SU "goosefoot" Team At The WSDM Cup 2017 Triple Scoring Task
authors: Valentin Zmiycharov, Dimitar Alexandrov, Preslav Nakov, Ivan Koychev, Yasen
  Kiprov
conference: Arxiv
year: 2017
bibkey: zmiycharov2017finding
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.08350'}]
tags: ["Evaluation"]
short_authors: Zmiycharov et al.
---
We describe the system that our FMI@SU student's team built for participating
in the Triple Scoring task at the WSDM Cup 2017. Given a triple from a
"type-like" relation, profession or nationality, the goal is to produce a
score, on a scale from 0 to 7, that measures the relevance of the statement
expressed by the triple: e.g., how well does the profession of an Actor fit for
Quentin Tarantino? We propose a distant supervision approach using information
crawled from Wikipedia, DeletionPedia, and DBpedia, together with task-specific
word embeddings, TF-IDF weights, and role occurrence order, which we combine in
a linear regression model. The official evaluation ranked our submission 1st on
Kendall's Tau, 7th on Average score difference, and 9th on Accuracy, out of 21
participating teams.