---
layout: publication
title: 'TACHYON: Efficient Shared Memory Parallel Computation Of Extremum Graphs'
authors: Abhijath Ande, Varshini Subhash, Vijay Natarajan
conference: Computer Graphics Forum
year: 2023
bibkey: ande2023tachyon
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.02724'}]
tags: ["Efficiency"]
short_authors: Abhijath Ande, Varshini Subhash, Vijay Natarajan
---
The extremum graph is a succinct representation of the Morse decomposition of
a scalar field. It has increasingly become a useful data structure that
supports topological feature directed visualization of 2D / 3D scalar fields,
and enables dimensionality reduction together with exploratory analysis of high
dimensional scalar fields. Current methods that employ the extremum graph
compute it either using a simple sequential algorithm for computing the Morse
decomposition or by computing the more detailed Morse-Smale complex. Both
approaches are typically limited to two and three dimensional scalar fields. We
describe a GPU-CPU hybrid parallel algorithm for computing the extremum graph
of scalar fields in all dimensions. The proposed shared memory algorithm
utilizes both fine grained parallelism and task parallelism to achieve
efficiency. An open source software library, TACHYON, that implements the
algorithm exhibits superior performance and good scaling behavior.