---
layout: publication
title: 'Average Localised Proximity: A New Data Descriptor With Good Default One-class
  Classification Performance'
authors: Oliver Urs Lenz, Daniel Peralta, Chris Cornelis
conference: Pattern Recognition
year: 2021
bibkey: lenz2021average
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.11037'}]
tags: []
short_authors: Oliver Urs Lenz, Daniel Peralta, Chris Cornelis
---
One-class classification is a challenging subfield of machine learning in
which so-called data descriptors are used to predict membership of a class
based solely on positive examples of that class, and no counter-examples. A
number of data descriptors that have been shown to perform well in previous
studies of one-class classification, like the Support Vector Machine (SVM),
require setting one or more hyperparameters. There has been no systematic
attempt to date to determine optimal default values for these hyperparameters,
which limits their ease of use, especially in comparison with
hyperparameter-free proposals like the Isolation Forest (IF). We address this
issue by determining optimal default hyperparameter values across a collection
of 246 one-class classification problems derived from 50 different real-world
datasets. In addition, we propose a new data descriptor, Average Localised
Proximity (ALP) to address certain issues with existing approaches based on
nearest neighbour distances. Finally, we evaluate classification performance
using a leave-one-dataset-out procedure, and find strong evidence that ALP
outperforms IF and a number of other data descriptors, as well as weak evidence
that it outperforms SVM, making ALP a good default choice.