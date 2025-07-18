---
layout: publication
title: Comparison Based Nearest Neighbor Search
authors: Haghiri Siavash, Ghoshdastidar Debarghya, von Luxburg Ulrike
conference: Arxiv
year: 2017
bibkey: haghiri2017comparison
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.01460'}]
tags: [Evaluation]
---
We consider machine learning in a comparison-based setting where we are given
a set of points in a metric space, but we have no access to the actual
distances between the points. Instead, we can only ask an oracle whether the
distance between two points \\(i\\) and \\(j\\) is smaller than the distance between
the points \\(i\\) and \\(k\\). We are concerned with data structures and algorithms to
find nearest neighbors based on such comparisons. We focus on a simple yet
effective algorithm that recursively splits the space by first selecting two
random pivot points and then assigning all other points to the closer of the
two (comparison tree). We prove that if the metric space satisfies certain
expansion conditions, then with high probability the height of the comparison
tree is logarithmic in the number of points, leading to efficient search
performance. We also provide an upper bound for the failure probability to
return the true nearest neighbor. Experiments show that the comparison tree is
competitive with algorithms that have access to the actual distance values, and
needs less triplet comparisons than other competitors.