---
layout: publication
title: 'Arion: Arithmetization-oriented Permutation And Hashing From Generalized Triangular
  Dynamical Systems'
authors: Arnab Roy, Matthias Johann Steiner, Stefano Trevisani
conference: Arxiv
year: 2023
bibkey: roy2023arion
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.04639'}]
tags: ["Hashing Methods"]
short_authors: Arnab Roy, Matthias Johann Steiner, Stefano Trevisani
---
In this paper we propose the (keyed) permutation Arion and the hash function
ArionHash over \(\mathbb\{F\}_p\) for odd and particularly large primes. The design
of Arion is based on the newly introduced Generalized Triangular Dynamical
System (GTDS), which provides a new algebraic framework for constructing
(keyed) permutation using polynomials over a finite field. At round level Arion
is the first design which is instantiated using the new GTDS. We provide
extensive security analysis of our construction including algebraic
cryptanalysis (e.g. interpolation and Gr\"obner basis attacks) that are
particularly decisive in assessing the security of permutations and hash
functions over \(\mathbb\{F\}_p\). From an application perspective, ArionHash aims
for efficient implementation in zkSNARK protocols and Zero-Knowledge proof
systems. For this purpose, we exploit that CCZ-equivalence of graphs can lead
to a more efficient implementation of Arithmetization-Oriented primitives.
  We compare the efficiency of ArionHash in R1CS and Plonk settings with other
hash functions such as Poseidon, Anemoi and Griffin. For demonstrating the
practical efficiency of ArionHash we implemented it with the zkSNARK libraries
libsnark and Dusk Network Plonk. Our result shows that ArionHash is
significantly faster than Poseidon - a hash function designed for
zero-knowledge proof systems. We also found that an aggressive version of
ArionHash is considerably faster than Anemoi and Griffin in a practical zkSNARK
setting.