---
layout: publication
title: Using Dynamical Quantization To Perform Split Attempts In Online Tree Regressors
authors: Saulo Martiello Mastelini, Andre Carlos Ponce de Leon Ferreira de Carvalho
conference: Arxiv
year: 2020
bibkey: mastelini2020using
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.00083'}]
tags: [Hashing Methods, Evaluation, Quantization, Efficiency]
short_authors: Saulo Martiello Mastelini, Andre Carlos Ponce de Leon Ferreira de Carvalho
---
A central aspect of online decision tree solutions is evaluating the incoming
data and enabling model growth. For such, trees much deal with different kinds
of input features and partition them to learn from the data. Numerical features
are no exception, and they pose additional challenges compared to other kinds
of features, as there is no trivial strategy to choose the best point to make a
split decision. The problem is even more challenging in regression tasks
because both the features and the target are continuous. Typical online
solutions evaluate and store all the points monitored between split attempts,
which goes against the constraints posed in real-time applications. In this
paper, we introduce the Quantization Observer (QO), a simple yet effective
hashing-based algorithm to monitor and evaluate split point candidates in
numerical features for online tree regressors. QO can be easily integrated into
incremental decision trees, such as Hoeffding Trees, and it has a monitoring
cost of \(O(1)\) per instance and sub-linear cost to evaluate split candidates.
Previous solutions had a \(O(log n)\) cost per insertion (in the best case) and
a linear cost to evaluate split points. Our extensive experimental setup
highlights QO's effectiveness in providing accurate split point suggestions
while spending much less memory and processing time than its competitors.