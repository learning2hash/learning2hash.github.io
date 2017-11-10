---
layout: publication
title: "Graph Cuts for Supervised Binary Coding"
authors: T. Ge, K. He, J. Sun
conference: ECCV
year: 2014
bibkey: ge2014graph
additional_links:
   - {name: "PDF", url: "http://kaiminghe.com/publications/eccv14gcc.pdf"}
---
Learning short binary codes is challenged by the inherent discrete
nature of the problem. The graph cuts algorithm is a well-studied
discrete label assignment solution in computer vision, but has not yet
been applied to solve the binary coding problems. This is partially because
it was unclear how to use it to learn the encoding (hashing) functions
for out-of-sample generalization. In this paper, we formulate supervised
binary coding as a single optimization problem that involves both
the encoding functions and the binary label assignment. Then we apply
the graph cuts algorithm to address the discrete optimization problem
involved, with no continuous relaxation. This method, named as Graph
Cuts Coding (GCC), shows competitive results in various datasets.
