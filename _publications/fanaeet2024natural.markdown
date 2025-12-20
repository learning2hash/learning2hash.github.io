---
layout: publication
title: Natural Learning
authors: Hadi Fanaee-T
conference: Early Years Educator
year: 2024
bibkey: fanaeet2024natural
citations: 0
additional_links: [{name: Code, url: 'http://natural-learning.cc'}, {name: Paper,
    url: 'https://arxiv.org/abs/2404.05903'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "Locality-Sensitive-Hashing"]
short_authors: Hadi Fanaee-T
---
We introduce Natural Learning (NL), a novel algorithm that elevates the
explainability and interpretability of machine learning to an extreme level. NL
simplifies decisions into intuitive rules, like "We rejected your loan because
your income, employment status, and age collectively resemble a rejected
prototype more than an accepted prototype." When applied to real-life datasets,
NL produces impressive results. For example, in a colon cancer dataset with
1545 patients and 10935 genes, NL achieves 98.1% accuracy, comparable to DNNs
and RF, by analyzing just 3 genes of test samples against 2 discovered
prototypes. Similarly, in the UCI's WDBC dataset, NL achieves 98.3% accuracy
using only 7 features and 2 prototypes. Even on the MNIST dataset (0 vs. 1), NL
achieves 99.5% accuracy with only 3 pixels from 2 prototype images. NL is
inspired by prototype theory, an old concept in cognitive psychology suggesting
that people learn single sparse prototypes to categorize objects. Leveraging
this relaxed assumption, we redesign Support Vector Machines (SVM), replacing
its mathematical formulation with a fully nearest-neighbor-based solution, and
to address the curse of dimensionality, we utilize locality-sensitive hashing.
Following theory's generalizability principle, we propose a recursive method to
prune non-core features. As a result, NL efficiently discovers the sparsest
prototypes in O(n^2pL) with high parallelization capacity in terms of n.
Evaluation of NL with 17 benchmark datasets shows its significant
outperformance compared to decision trees and logistic regression, two methods
widely favored in healthcare for their interpretability. Moreover, NL achieves
performance comparable to finetuned black-box models such as deep neural
networks and random forests in 40% of cases, with only a 1-2% lower average
accuracy. The code is available via http://natural-learning.cc.