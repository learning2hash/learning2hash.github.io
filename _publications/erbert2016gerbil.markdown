---
layout: publication
title: Gerbil A Fast And Memory-efficient k-mer Counter With Gpu-support
authors: Erbert Marius, Rechner Steffen, Müller-hannemann Matthias
conference: "Arxiv"
year: 2016
bibkey: erbert2016gerbil
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1607.06618"}
tags: ['ARXIV']
---
A basic task in bioinformatics is the counting of \\(k\\)-mers in genome strings. The \\(k\\)-mer counting problem is to build a histogram of all substrings of length \\(k\\) in a given genome sequence. We present the open source \\(k\\)-mer counting software Gerbil that has been designed for the efficient counting of \\(k\\)-mers for \\(k\geq32\\). Given the technology trend towards long reads of next-generation sequencers, support for large \\(k\\) becomes increasingly important. While existing \\(k\\)-mer counting tools suffer from excessive memory resource consumption or degrading performance for large \\(k\\), Gerbil is able to efficiently support large \\(k\\) without much loss of performance. Our software implements a two-disk approach. In the first step, DNA reads are loaded from disk and distributed to temporary files that are stored at a working disk. In a second step, the temporary files are read again, split into \\(k\\)-mers and counted via a hash table approach. In addition, Gerbil can optionally use GPUs to accelerate the counting step. For large \\(k\\), we outperform state-of-the-art open source \\(k\\)-mer counting tools for large genome data sets.
