---
layout: publication
title: "Sparse Hashing for Scalable Approximate Model Counting: Theory and Practice"
authors: Meel Kuldeep S., Akshay S.
conference: Arxiv
year: 2020
bibkey: meel2020sparse
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2004.14692"}
tags: ['ACL', 'ARXIV']
---
Given a CNF formula F on n variables, the problem of model counting or #SAT is
to compute the number of satisfying assignments of F . Model counting is a
fundamental but hard problem in computer science with varied applications.
Recent years have witnessed a surge of effort towards developing efficient
algorithmic techniques that combine the classical 2-universal hashing with the
remarkable progress in SAT solving over the past decade. These techniques
augment the CNF formula F with random XOR constraints and invoke an NP oracle
repeatedly on the resultant CNF-XOR formulas. In practice, calls to the NP
oracle calls are replaced a SAT solver whose runtime performance is adversely
affected by size of XOR constraints. The standard construction of 2-universal
hash functions chooses every variable with probability p = 1/2 leading to XOR
constraints of size n/2 in expectation. Consequently, the challenge is to design
sparse hash functions where variables can be chosen with smaller probability and
lead to smaller sized XOR constraints. In this paper, we address this challenge
from theoretical and practical perspectives. First, we formalize a relaxation of
universal hashing, called concentrated hashing and establish a novel and
beautiful connection between concentration measures of these hash functions and
isoperimetric inequalities on boolean hypercubes. This allows us to obtain (log
m) tight bounds on variance and dispersion index and show that p = O( log(m)/m )
suffices for design of sparse hash functions from {0, 1}^n to {0, 1}^m. We then
use sparse hash functions belonging to this concentrated hash family to develop
new approximate counting algorithms. A comprehensive experimental evaluation of
our algorithm on 1893 benchmarks demonstrates that usage of sparse hash
functions can lead to significant speedups.
