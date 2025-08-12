---
layout: publication
title: A Distance-preserving Matrix Sketch
authors: Leland Wilkinson, Hengrui Luo
conference: Journal of Computational and Graphical Statistics
year: 2022
bibkey: wilkinson2020distance
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.03979'}]
tags: []
short_authors: Leland Wilkinson, Hengrui Luo
---
Visualizing very large matrices involves many formidable problems. Various
popular solutions to these problems involve sampling, clustering, projection,
or feature selection to reduce the size and complexity of the original task. An
important aspect of these methods is how to preserve relative distances between
points in the higher-dimensional space after reducing rows and columns to fit
in a lower dimensional space. This aspect is important because conclusions
based on faulty visual reasoning can be harmful. Judging dissimilar points as
similar or similar points as dissimilar on the basis of a visualization can
lead to false conclusions. To ameliorate this bias and to make visualizations
of very large datasets feasible, we introduce two new algorithms that
respectively select a subset of rows and columns of a rectangular matrix. This
selection is designed to preserve relative distances as closely as possible. We
compare our matrix sketch to more traditional alternatives on a variety of
artificial and real datasets.