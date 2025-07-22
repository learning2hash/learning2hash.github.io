---
layout: publication
title: Binary Hashing with Semidefinite Relaxation and Augmented Lagrangian
authors: Do Thanh-toan, Doan Anh-dzung, Nguyen Duc-thanh, Cheung Ngai-man
conference: Lecture Notes in Computer Science
year: 2016
bibkey: do2016binary
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1607.05396'}]
tags: ["Supervised", "Hashing-Methods", "Datasets", "Neural-Hashing", "Compact-Codes", "Unsupervised", "Evaluation"]
short_authors: Do et al.
---
This paper proposes two approaches for inferencing binary codes in two-step
(supervised, unsupervised) hashing. We first introduce an unified formulation
for both supervised and unsupervised hashing. Then, we cast the learning of one
bit as a Binary Quadratic Problem (BQP). We propose two approaches to solve
BQP. In the first approach, we relax BQP as a semidefinite programming problem
which its global optimum can be achieved. We theoretically prove that the
objective value of the binary solution achieved by this approach is well
bounded. In the second approach, we propose an augmented Lagrangian based
approach to solve BQP directly without relaxing the binary constraint.
Experimental results on three benchmark datasets show that our proposed methods
compare favorably with the state of the art.