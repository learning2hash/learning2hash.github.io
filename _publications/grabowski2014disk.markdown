---
layout: publication
title: Disk-based Genome Sequencing Data Compression
authors: "Szymon Grabowski, Sebastian Deorowicz, \u0141ukasz Roguski"
conference: Arxiv
year: 2014
bibkey: grabowski2014disk
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1405.6874'}]
tags: ["Datasets"]
short_authors: "Szymon Grabowski, Sebastian Deorowicz, \u0141ukasz Roguski"
---
Motivation: High-coverage sequencing data have significant, yet hard to
exploit, redundancy. Most FASTQ compressors cannot efficiently compress the DNA
stream of large datasets, since the redundancy between overlapping reads cannot
be easily captured in the (relatively small) main memory. More interesting
solutions for this problem are disk-based~(Yanovsky, 2011; Cox et al., 2012),
where the better of these two, from Cox~\{\it et al.\}~(2012), is based on the
Burrows--Wheeler transform (BWT) and achieves 0.518 bits per base for a 134.0
Gb human genome sequencing collection with almost 45-fold coverage.
  Results: We propose ORCOM (Overlapping Reads COmpression with Minimizers), a
compression algorithm dedicated to sequencing reads (DNA only). Our method
makes use of a conceptually simple and easily parallelizable idea of
minimizers, to obtain 0.317 bits per base as the compression ratio, allowing to
fit the 134.0 Gb dataset into only 5.31 GB of space.
  Availability: http://sun.aei.polsl.pl/orcom under a free license.