---
layout: publication
title: Property-preserving Hash Functions From Standard Assumptions
authors: Fleischhacker Nils, Larsen Kasper Green, Simkin And Mark
conference: Lecture Notes in Computer Science
year: 2021
bibkey: fleischhacker2021property
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.06453'}]
tags: [Hashing Methods, Evaluation, Robustness]
---
Property-preserving hash functions allow for compressing long inputs \\(x_0\\)
and \\(x_1\\) into short hashes \\(h(x_0)\\) and \\(h(x_1)\\) in a manner that allows for
computing a predicate \\(P(x_0, x_1)\\) given only the two hash values without
having access to the original data. Such hash functions are said to be
adversarially robust if an adversary that gets to pick \\(x_0\\) and \\(x_1\\) after
the hash function has been sampled, cannot find inputs for which the predicate
evaluated on the hash values outputs the incorrect result.
  In this work we construct robust property-preserving hash functions for the
hamming-distance predicate which distinguishes inputs with a hamming distance
at least some threshold \\(t\\) from those with distance less than \\(t\\). The
security of the construction is based on standard lattice hardness assumptions.
  Our construction has several advantages over the best known previous
construction by Fleischhacker and Simkin. Our construction relies on a single
well-studied hardness assumption from lattice cryptography whereas the previous
work relied on a newly introduced family of computational hardness assumptions.
In terms of computational effort, our construction only requires a small number
of modular additions per input bit, whereas previously several exponentiations
per bit as well as the interpolation and evaluation of high-degree polynomials
over large fields were required. An additional benefit of our construction is
that the description of the hash function can be compressed to \\(\lambda\\) bits
assuming a random oracle. Previous work has descriptions of length
\\(\mathcal\{O\}(\ell \lambda)\\) bits for input bit-length \\(\ell\\), which has a
secret structure and thus cannot be compressed.
  We prove a lower bound on the output size of any property-preserving hash
function for the hamming distance predicate. The bound shows that the size of
our hash value is not far from optimal.