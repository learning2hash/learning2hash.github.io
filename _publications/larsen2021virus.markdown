---
layout: publication
title: 'Virus-mnist: Machine Learning Baseline Calculations For Image Classification'
authors: Erik Larsen, Korey MacVittie, John Lilly
conference: Arxiv
year: 2021
bibkey: larsen2021virus
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.02375'}]
tags: ["Evaluation"]
short_authors: Erik Larsen, Korey MacVittie, John Lilly
---
The Virus-MNIST data set is a collection of thumbnail images that is similar
in style to the ubiquitous MNIST hand-written digits. These, however, are cast
by reshaping possible malware code into an image array. Naturally, it is poised
to take on a role in benchmarking progress of virus classifier model training.
Ten types are present: nine classified as malware and one benign. Cursory
examination reveals unequal class populations and other key aspects that must
be considered when selecting classification and pre-processing methods.
Exploratory analyses show possible identifiable characteristics from aggregate
metrics (e.g., the pixel median values), and ways to reduce the number of
features by identifying strong correlations. A model comparison shows that
Light Gradient Boosting Machine, Gradient Boosting Classifier, and Random
Forest algorithms produced the highest accuracy scores, thus showing promise
for deeper scrutiny.