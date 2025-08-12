---
layout: publication
title: On Sparse Representation In Fourier And Local Bases
authors: Pier Luigi Dragotti, Yue M. Lu
conference: IEEE Transactions on Information Theory
year: 2014
bibkey: dragotti2013sparse
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1310.6011'}]
tags: []
short_authors: Pier Luigi Dragotti, Yue M. Lu
---
We consider the classical problem of finding the sparse representation of a
signal in a pair of bases. When both bases are orthogonal, it is known that the
sparse representation is unique when the sparsity \\(K\\) of the signal satisfies
\\(K<1/\mu(D)\\), where \\(\mu(D)\\) is the mutual coherence of the dictionary.
Furthermore, the sparse representation can be obtained in polynomial time by
Basis Pursuit (BP), when \\(K<0.91/\mu(D)\\). Therefore, there is a gap between the
unicity condition and the one required to use the polynomial-complexity BP
formulation. For the case of general dictionaries, it is also well known that
finding the sparse representation under the only constraint of unicity is
NP-hard.
  In this paper, we introduce, for the case of Fourier and canonical bases, a
polynomial complexity algorithm that finds all the possible \\(K\\)-sparse
representations of a signal under the weaker condition that \\(K<\sqrt\{2\}
/\mu(D)\\). Consequently, when \\(K<1/\mu(D)\\), the proposed algorithm solves the
unique sparse representation problem for this structured dictionary in
polynomial time. We further show that the same method can be extended to many
other pairs of bases, one of which must have local atoms. Examples include the
union of Fourier and local Fourier bases, the union of discrete cosine
transform and canonical bases, and the union of random Gaussian and canonical
bases.