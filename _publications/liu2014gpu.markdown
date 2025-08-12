---
layout: publication
title: Gpu-accelerated BWT Construction For Large Collection Of Short Reads
authors: Chi-Man Liu, Ruibang Luo, Tak-Wah Lam
conference: Arxiv
year: 2014
bibkey: liu2014gpu
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1401.7457'}]
tags: ["Efficiency"]
short_authors: Chi-Man Liu, Ruibang Luo, Tak-Wah Lam
---
Advances in DNA sequencing technology have stimulated the development of
algorithms and tools for processing very large collections of short strings
(reads). Short-read alignment and assembly are among the most well-studied
problems. Many state-of-the-art aligners, at their core, have used the
Burrows-Wheeler transform (BWT) as a main-memory index of a reference genome
(typical example, NCBI human genome). Recently, BWT has also found its use in
string-graph assembly, for indexing the reads (i.e., raw data from DNA
sequencers). In a typical data set, the volume of reads is tens of times of the
sequenced genome and can be up to 100 Gigabases. Note that a reference genome
is relatively stable and computing the index is not a frequent task. For reads,
the index has to computed from scratch for each given input. The ability of
efficient BWT construction becomes a much bigger concern than before. In this
paper, we present a practical method called CX1 for constructing the BWT of
very large string collections. CX1 is the first tool that can take advantage of
the parallelism given by a graphics processing unit (GPU, a relative cheap
device providing a thousand or more primitive cores), as well as simultaneously
the parallelism from a multi-core CPU and more interestingly, from a cluster of
GPU-enabled nodes. Using CX1, the BWT of a short-read collection of up to 100
Gigabases can be constructed in less than 2 hours using a machine equipped with
a quad-core CPU and a GPU, or in about 43 minutes using a cluster with 4 such
machines (the speedup is almost linear after excluding the first 16 minutes for
loading the reads from the hard disk). The previously fastest tool BRC is
measured to take 12 hours to process 100 Gigabases on one machine; it is
non-trivial how BRC can be parallelized to take advantage a cluster of
machines, let alone GPUs.