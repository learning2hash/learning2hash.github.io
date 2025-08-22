---
layout: publication
title: End-to-end Latent Fingerprint Search
authors: Kai Cao, Dinh-luan Nguyen, Cori Tymoszek, A. K. Jain
conference: IEEE Transactions on Information Forensics and Security
year: 2019
bibkey: cao2018end
citations: 65
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.10213'}]
tags: ["Efficiency", "Evaluation", "Quantization"]
short_authors: Cao et al.
---
Latent fingerprints are one of the most important and widely used sources of
evidence in law enforcement and forensic agencies. Yet the performance of the
state-of-the-art latent recognition systems is far from satisfactory, and they
often require manual markups to boost the latent search performance. Further,
the COTS systems are proprietary and do not output the true comparison scores
between a latent and reference prints to conduct quantitative evidential
analysis. We present an end-to-end latent fingerprint search system, including
automated region of interest (ROI) cropping, latent image preprocessing,
feature extraction, feature comparison , and outputs a candidate list. Two
separate minutiae extraction models provide complementary minutiae templates.
To compensate for the small number of minutiae in small area and poor quality
latents, a virtual minutiae set is generated to construct a texture template. A
96-dimensional descriptor is extracted for each minutia from its neighborhood.
For computational efficiency, the descriptor length for virtual minutiae is
further reduced to 16 using product quantization. Our end-to-end system is
evaluated on three latent databases: NIST SD27 (258 latents); MSP (1,200
latents), WVU (449 latents) and N2N (10,000 latents) against a background set
of 100K rolled prints, which includes the true rolled mates of the latents with
rank-1 retrieval rates of 65.7%, 69.4%, 65.5%, and 7.6% respectively. A
multi-core solution implemented on 24 cores obtains 1ms per latent to rolled
comparison.