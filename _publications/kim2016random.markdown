---
layout: publication
title: Random Forest DBSCAN For USPTO Inventor Name Disambiguation
authors: Kunho Kim, Madian Khabsa, C. Lee Giles
conference: Arxiv
year: 2016
bibkey: kim2016random
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.01792'}]
tags: ["Tools & Libraries"]
short_authors: Kunho Kim, Madian Khabsa, C. Lee Giles
---
Name disambiguation and the subsequent name conflation are essential for the
correct processing of person name queries in a digital library or other
database. It distinguishes each unique person from all other records in the
database. We study inventor name disambiguation for a patent database using
methods and features from earlier work on author name disambiguation and
propose a feature set appropriate for a patent database. A random forest was
selected for the pairwise linking classifier since they outperform Naive Bayes,
Logistic Regression, Support Vector Machines (SVM), Conditional Inference Tree,
and Decision Trees. Blocking size, very important for scaling, was selected
based on experiments that determined feature importance and accuracy. The
DBSCAN algorithm is used for clustering records, using a distance function
derived from random forest classifier. For additional scalability clustering
was parallelized. Tests on the USPTO patent database show that our method
successfully disambiguated 12 million inventor mentions within 6.5 hours.
Evaluation on datasets from USPTO PatentsView inventor name disambiguation
competition shows our algorithm outperforms all algorithms in the competition.