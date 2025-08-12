---
layout: publication
title: Sample Efficient Estimation And Recovery In Sparse FFT Via Isolation On Average
authors: Michael Kapralov
conference: 2017 IEEE 58th Annual Symposium on Foundations of Computer Science (FOCS)
year: 2017
bibkey: kapralov2017sample
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.04544'}]
tags: ["Hashing Methods"]
short_authors: Michael Kapralov
---
The problem of computing the Fourier Transform of a signal whose spectrum is
dominated by a small number \(k\) of frequencies quickly and using a small number
of samples of the signal in time domain (the Sparse FFT problem) has received
significant attention recently. It is known how to approximately compute the
\(k\)-sparse Fourier transform in \(\approx klog^2 n\) time [Hassanieh et
al'STOC'12], or using the optimal number \(O(klog n)\) of samples [Indyk et
al'FOCS'14] in time domain, or come within \((loglog n)^\{O(1)\}\) factors of
both these bounds simultaneously, but no algorithm achieving the optimal
\(O(klog n)\) bound in sublinear time is known.
  In this paper we propose a new technique for analysing noisy hashing schemes
that arise in Sparse FFT, which we refer to as isolation on average. We apply
this technique to two problems in Sparse FFT: estimating the values of a list
of frequencies using few samples and computing Sparse FFT itself, achieving
sample-optimal results in \(klog^\{O(1)\} n\) time for both. We feel that our
approach will likely be of interest in designing Fourier sampling schemes for
more general settings (e.g. model based Sparse FFT).