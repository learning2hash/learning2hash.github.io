---
layout: publication
title: Fast Fourier Sparsity Testing
authors: Grigory Yaroslavtsev, Samson Zhou
conference: Arxiv
year: 2019
bibkey: yaroslavtsev2019fast
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.05686'}]
tags: ["Efficiency"]
short_authors: Grigory Yaroslavtsev, Samson Zhou
---
A function \(f : \mathbb\{F\}_2^n \to \mathbb\{R\}\) is \(s\)-sparse if it has at
most \(s\) non-zero Fourier coefficients. Motivated by applications to fast
sparse Fourier transforms over \(\mathbb\{F\}_2^n\), we study efficient algorithms
for the problem of approximating the \(ℓ₂\)-distance from a given function to
the closest \(s\)-sparse function. While previous works (e.g., Gopalan et al.
SICOMP 2011) study the problem of distinguishing \(s\)-sparse functions from
those that are far from \(s\)-sparse under Hamming distance, to the best of our
knowledge no prior work has explicitly focused on the more general problem of
distance estimation in the \(ℓ₂\) setting, which is particularly
well-motivated for noisy Fourier spectra. Given the focus on efficiency, our
main result is an algorithm that solves this problem with query complexity
\(\mathcal\{O\}(s)\) for constant accuracy and error parameters, which is only
quadratically worse than applicable lower bounds.