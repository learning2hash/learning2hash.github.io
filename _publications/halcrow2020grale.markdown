---
layout: publication
title: 'Grale: Designing Networks For Graph Learning'
authors: "Jonathan Halcrow, Alexandru Mo\u015Foi, Sam Ruth, Bryan Perozzi"
conference: 'KDD ''20: The 26th ACM SIGKDD Conference on Knowledge Discovery and Data
  Mining'
year: 2020
bibkey: halcrow2020grale
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.12002'}]
tags: ["Datasets", "Hashing Methods", "KDD", "Locality-Sensitive-Hashing", "Supervised"]
short_authors: Halcrow et al.
---
How can we find the right graph for semi-supervised learning? In real world
applications, the choice of which edges to use for computation is the first
step in any graph learning process. Interestingly, there are often many types
of similarity available to choose as the edges between nodes, and the choice of
edges can drastically affect the performance of downstream semi-supervised
learning systems. However, despite the importance of graph design, most of the
literature assumes that the graph is static. In this work, we present Grale, a
scalable method we have developed to address the problem of graph design for
graphs with billions of nodes. Grale operates by fusing together different
measures of(potentially weak) similarity to create a graph which exhibits high
task-specific homophily between its nodes. Grale is designed for running on
large datasets. We have deployed Grale in more than 20 different industrial
settings at Google, including datasets which have tens of billions of nodes,
and hundreds of trillions of potential edges to score. By employing locality
sensitive hashing techniques,we greatly reduce the number of pairs that need to
be scored, allowing us to learn a task specific model and build the associated
nearest neighbor graph for such datasets in hours, rather than the days or even
weeks that might be required otherwise. We illustrate this through a case study
where we examine the application of Grale to an abuse classification problem on
YouTube with hundreds of million of items. In this application, we find that
Grale detects a large number of malicious actors on top of hard-coded rules and
content classifiers, increasing the total recall by 89% over those approaches
alone.