---
layout: publication
title: 'Marvolo: Programmatic Data Augmentation For Practical Ml-driven Malware Detection'
authors: Michael D. Wong, Edward Raff, James Holt, Ravi Netravali
conference: Arxiv
year: 2022
bibkey: wong2022marvolo
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.03265'}]
tags: ["Datasets"]
short_authors: Wong et al.
---
Data augmentation has been rare in the cyber security domain due to technical
difficulties in altering data in a manner that is semantically consistent with
the original data. This shortfall is particularly onerous given the unique
difficulty of acquiring benign and malicious training data that runs into
copyright restrictions, and that institutions like banks and governments
receive targeted malware that will never exist in large quantities. We present
MARVOLO, a binary mutator that programmatically grows malware (and benign)
datasets in a manner that boosts the accuracy of ML-driven malware detectors.
MARVOLO employs semantics-preserving code transformations that mimic the
alterations that malware authors and defensive benign developers routinely make
in practice , allowing us to generate meaningful augmented data. Crucially,
semantics-preserving transformations also enable MARVOLO to safely propagate
labels from original to newly-generated data samples without mandating
expensive reverse engineering of binaries. Further, MARVOLO embeds several key
optimizations that keep costs low for practitioners by maximizing the density
of diverse data samples generated within a given time (or resource) budget.
Experiments using wide-ranging commercial malware datasets and a recent
ML-driven malware detector show that MARVOLO boosts accuracies by up to 5%,
while operating on only a small fraction (15%) of the potential input binaries.