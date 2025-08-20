---
layout: publication
title: Linear Hashing With \(\ell_\infty\) Guarantees And Two-sided Kakeya Bounds
authors: Manik Dhar, Zeev Dvir
conference: TheoretiCS
year: 2024
bibkey: dhar2024linear
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.01665'}]
tags: [Evaluation, Hashing Methods]
short_authors: Manik Dhar, Zeev Dvir
---
We show that a randomly chosen linear map over a finite field gives a good
hash function in the \(\ell_\infty\) sense. More concretely, consider a set \(S
\subset \mathbb\{F\}_q^n\) and a randomly chosen linear map \(L : \mathbb\{F\}_q^n
\to \mathbb\{F\}_q^t\) with \(q^t\) taken to be sufficiently smaller than \( |S|\).
Let \(U_S\) denote a random variable distributed uniformly on \(S\). Our main
theorem shows that, with high probability over the choice of \(L\), the random
variable \(L(U_S)\) is close to uniform in the \(\ell_\infty\) norm. In other
words, \{\em every\} element in the range \(\mathbb\{F\}_q^t\) has about the same
number of elements in \(S\) mapped to it. This complements the widely-used
Leftover Hash Lemma (LHL) which proves the analog statement under the
statistical, or \(\ell_1\), distance (for a richer class of functions) as well as
prior work on the expected largest 'bucket size' in linear hash functions
[ADMPT99]. By known bounds from the load balancing literature [RS98], our
results are tight and show that linear functions hash as well as trully random
function up to a constant factor in the entropy loss. Our proof leverages a
connection between linear hashing and the finite field Kakeya problem and
extends some of the tools developed in this area, in particular the polynomial
method.