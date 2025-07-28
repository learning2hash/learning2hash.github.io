---
layout: publication
title: 'On Minimizers And Convolutional Filters: Theoretical Connections And Applications
  To Genome Analysis'
authors: Yun William Yu
conference: Journal of Computational Biology
year: 2024
bibkey: yu2024minimizers
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.08452'}]
tags: []
short_authors: Yun William Yu
---
Minimizers and convolutional neural networks (CNNs) are two quite distinct
popular techniques that have both been employed to analyze categorical
biological sequences. At face value, the methods seem entirely dissimilar.
Minimizers use min-wise hashing on a rolling window to extract a single
important k-mer feature per window. CNNs start with a wide array of randomly
initialized convolutional filters, paired with a pooling operation, and then
multiple additional neural layers to learn both the filters themselves and how
they can be used to classify the sequence.
  Here, our main result is a careful mathematical analysis of hash function
properties showing that for sequences over a categorical alphabet, random
Gaussian initialization of convolutional filters with max-pooling is equivalent
to choosing a minimizer ordering such that selected k-mers are (in Hamming
distance) far from the k-mers within the sequence but close to other
minimizers. In empirical experiments, we find that this property manifests as
decreased density in repetitive regions, both in simulation and on real human
telomeres. We additionally train from scratch a CNN embedding of synthetic
short-reads from the SARS-CoV-2 genome into 3D Euclidean space that locally
recapitulates the linear sequence distance of the read origins, a modest step
towards building a deep learning assembler, though it is at present too slow to
be practical. In total, this manuscript provides a partial explanation for the
effectiveness of CNNs in categorical sequence analysis.