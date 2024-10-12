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
A basic task in bioinformatics is the counting of \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}-mers in genome strings. The \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}-mer counting problem is to build a histogram of all substrings of length \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\} in a given genome sequence. We present the open source \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}-mer counting software Gerbil that has been designed for the efficient counting of \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}-mers for \{&#37; raw &#37;\}\\(k\geq32\\)\{&#37; endraw &#37;\}. Given the technology trend towards long reads of next-generation sequencers, support for large \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\} becomes increasingly important. While existing \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}-mer counting tools suffer from excessive memory resource consumption or degrading performance for large \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}, Gerbil is able to efficiently support large \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\} without much loss of performance. Our software implements a two-disk approach. In the first step, DNA reads are loaded from disk and distributed to temporary files that are stored at a working disk. In a second step, the temporary files are read again, split into \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}-mers and counted via a hash table approach. In addition, Gerbil can optionally use GPUs to accelerate the counting step. For large \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}, we outperform state-of-the-art open source \{&#37; raw &#37;\}\\(k\\)\{&#37; endraw &#37;\}-mer counting tools for large genome data sets.
