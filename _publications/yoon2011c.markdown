---
layout: publication
title: 'C-rank: A Link-based Similarity Measure For Scientific Literature Databases'
authors: Seok-ho Yoon, Sang-wook Kim, Sunju Park
conference: Information Sciences
year: 2015
bibkey: yoon2011c
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1109.1059'}]
tags: ["Evaluation"]
short_authors: Seok-ho Yoon, Sang-wook Kim, Sunju Park
---
As the number of people who use scientific literature databases grows, the
demand for literature retrieval services has been steadily increased. One of
the most popular retrieval services is to find a set of papers similar to the
paper under consideration, which requires a measure that computes similarities
between papers. Scientific literature databases exhibit two interesting
characteristics that are different from general databases. First, the papers
cited by old papers are often not included in the database due to technical and
economic reasons. Second, since a paper references the papers published before
it, few papers cite recently-published papers. These two characteristics cause
all existing similarity measures to fail in at least one of the following
cases: (1) measuring the similarity between old, but similar papers, (2)
measuring the similarity between recent, but similar papers, and (3) measuring
the similarity between two similar papers: one old, the other recent. In this
paper, we propose a new link-based similarity measure called C-Rank, which uses
both in-link and out-link by disregarding the direction of references. In
addition, we discuss the most suitable normalization method for scientific
literature databases and propose an evaluation method for measuring the
accuracy of similarity measures. We have used a database with real-world papers
from DBLP and their reference information crawled from Libra for experiments
and compared the performance of C-Rank with those of existing similarity
measures. Experimental results show that C-Rank achieves a higher accuracy than
existing similarity measures.