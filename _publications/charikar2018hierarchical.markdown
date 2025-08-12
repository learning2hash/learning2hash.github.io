---
layout: publication
title: Hierarchical Clustering For Euclidean Data
authors: Moses Charikar, Vaggos Chatziafratis, Rad Niazadeh, Grigory Yaroslavtsev
conference: Arxiv
year: 2019
bibkey: charikar2018hierarchical
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.10582'}]
tags: ["Unsupervised"]
short_authors: Charikar et al.
---
Recent works on Hierarchical Clustering (HC), a well-studied problem in
exploratory data analysis, have focused on optimizing various objective
functions for this problem under arbitrary similarity measures. In this paper
we take the first step and give novel scalable algorithms for this problem
tailored to Euclidean data in R^d and under vector-based similarity measures, a
prevalent model in several typical machine learning applications. We focus
primarily on the popular Gaussian kernel and other related measures, presenting
our results through the lens of the objective introduced recently by Moseley
and Wang [2017]. We show that the approximation factor in Moseley and Wang
[2017] can be improved for Euclidean data. We further demonstrate both
theoretically and experimentally that our algorithms scale to very high
dimension d, while outperforming average-linkage and showing competitive
results against other less scalable approaches.