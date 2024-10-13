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
<p>A basic task in bioinformatics is the counting of <span
class="math inline">\(k\)</span>-mers in genome strings. The <span
class="math inline">\(k\)</span>-mer counting problem is to build a
histogram of all substrings of length <span
class="math inline">\(k\)</span> in a given genome sequence. We present
the open source <span class="math inline">\(k\)</span>-mer counting
software Gerbil that has been designed for the efficient counting of
<span class="math inline">\(k\)</span>-mers for <span
class="math inline">\(k\geq32\)</span>. Given the technology trend
towards long reads of next-generation sequencers, support for large
<span class="math inline">\(k\)</span> becomes increasingly important.
While existing <span class="math inline">\(k\)</span>-mer counting tools
suffer from excessive memory resource consumption or degrading
performance for large <span class="math inline">\(k\)</span>, Gerbil is
able to efficiently support large <span class="math inline">\(k\)</span>
without much loss of performance. Our software implements a two-disk
approach. In the first step, DNA reads are loaded from disk and
distributed to temporary files that are stored at a working disk. In a
second step, the temporary files are read again, split into <span
class="math inline">\(k\)</span>-mers and counted via a hash table
approach. In addition, Gerbil can optionally use GPUs to accelerate the
counting step. For large <span class="math inline">\(k\)</span>, we
outperform state-of-the-art open source <span
class="math inline">\(k\)</span>-mer counting tools for large genome
data sets.</p>
