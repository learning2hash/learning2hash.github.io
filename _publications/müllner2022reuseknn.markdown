---
layout: publication
title: 'Reuseknn: Neighborhood Reuse For Differentially-private Knn-based Recommendations'
authors: "Peter M\xFCllner, Elisabeth Lex, Markus Schedl, Dominik Kowald"
conference: ACM Transactions on Intelligent Systems and Technology
year: 2023
bibkey: "m\xFCllner2022reuseknn"
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.11561'}]
tags: ["Privacy & Security", "Recommender Systems"]
short_authors: "M\xFCllner et al."
---
User-based KNN recommender systems (UserKNN) utilize the rating data of a
target user's k nearest neighbors in the recommendation process. This, however,
increases the privacy risk of the neighbors since their rating data might be
exposed to other users or malicious parties. To reduce this risk, existing work
applies differential privacy by adding randomness to the neighbors' ratings,
which reduces the accuracy of UserKNN. In this work, we introduce ReuseKNN, a
novel differentially-private KNN-based recommender system. The main idea is to
identify small but highly reusable neighborhoods so that (i) only a minimal set
of users requires protection with differential privacy, and (ii) most users do
not need to be protected with differential privacy, since they are only rarely
exploited as neighbors. In our experiments on five diverse datasets, we make
two key observations: Firstly, ReuseKNN requires significantly smaller
neighborhoods, and thus, fewer neighbors need to be protected with differential
privacy compared to traditional UserKNN. Secondly, despite the small
neighborhoods, ReuseKNN outperforms UserKNN and a fully differentially private
approach in terms of accuracy. Overall, ReuseKNN leads to significantly less
privacy risk for users than in the case of UserKNN.