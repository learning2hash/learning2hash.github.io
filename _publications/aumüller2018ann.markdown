---
layout: publication
title: 'Ann-benchmarks: A Benchmarking Tool For Approximate Nearest Neighbor Algorithms'
authors: "Martin Aum\xFCller, Erik Bernhardsson, Alexander Faithfull"
conference: Arxiv
year: 2018
bibkey: "aum\xFCller2018ann"
citations: 5
additional_links: [{name: Other, url: 'http://ann-benchmarks.com'}, {name: Paper,
    url: 'https://arxiv.org/abs/1807.05614'}]
tags: ["Evaluation", "Similarity Search"]
short_authors: "Martin Aum\xFCller, Erik Bernhardsson, Alexander Faithfull"
---
This paper describes ANN-Benchmarks, a tool for evaluating the performance of
in-memory approximate nearest neighbor algorithms. It provides a standard
interface for measuring the performance and quality achieved by nearest
neighbor algorithms on different standard data sets. It supports several
different ways of integrating \(k\)-NN algorithms, and its configuration system
automatically tests a range of parameter settings for each algorithm.
Algorithms are compared with respect to many different (approximate) quality
measures, and adding more is easy and fast; the included plotting front-ends
can visualise these as images, \(\LaTeX\) plots, and websites with interactive
plots. ANN-Benchmarks aims to provide a constantly updated overview of the
current state of the art of \(k\)-NN algorithms. In the short term, this overview
allows users to choose the correct \(k\)-NN algorithm and parameters for their
similarity search task; in the longer term, algorithm designers will be able to
use this overview to test and refine automatic parameter tuning. The paper
gives an overview of the system, evaluates the results of the benchmark, and
points out directions for future work. Interestingly, very different approaches
to \(k\)-NN search yield comparable quality-performance trade-offs. The system is
available at http://ann-benchmarks.com .