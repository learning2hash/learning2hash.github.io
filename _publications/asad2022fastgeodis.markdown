---
layout: publication
title: 'Fastgeodis: Fast Generalised Geodesic Distance Transform'
authors: Muhammad Asad, Reuben Dorent, Tom Vercauteren
conference: Journal of Open Source Software
year: 2022
bibkey: asad2022fastgeodis
citations: 13
additional_links: [{name: Code, url: 'https://fastgeodis.readthedocs.io'}, {name: Paper,
    url: 'https://arxiv.org/abs/2208.00001'}]
tags: ["Distance Metric Learning", "Efficiency"]
short_authors: Muhammad Asad, Reuben Dorent, Tom Vercauteren
---
The FastGeodis package provides an efficient implementation for computing
Geodesic and Euclidean distance transforms (or a mixture of both), targeting
efficient utilisation of CPU and GPU hardware. In particular, it implements the
paralellisable raster scan method from Criminisi et al. (2009), where elements
in a row (2D) or plane (3D) can be computed with parallel threads. This package
is able to handle 2D as well as 3D data, where it achieves up to a 20x speedup
on a CPU and up to a 74x speedup on a GPU as compared to an existing
open-source library (Wang, 2020) that uses a non-parallelisable single-thread
CPU implementation. The performance speedups reported here were evaluated using
3D volume data on an Nvidia GeForce Titan X (12 GB) with a 6-Core Intel Xeon
E5-1650 CPU. Further in-depth comparison of performance improvements are
discussed in the FastGeodis documentation: https://fastgeodis.readthedocs.io