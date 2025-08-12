---
layout: publication
title: Automated Latent Fingerprint Recognition
authors: Kai Cao, Anil K. Jain
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2018
bibkey: cao2017automated
citations: 177
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.01925'}]
tags: ["Evaluation"]
short_authors: Kai Cao, Anil K. Jain
---
Latent fingerprints are one of the most important and widely used evidence in
law enforcement and forensic agencies worldwide. Yet, NIST evaluations show
that the performance of state-of-the-art latent recognition systems is far from
satisfactory. An automated latent fingerprint recognition system with high
accuracy is essential to compare latents found at crime scenes to a large
collection of reference prints to generate a candidate list of possible mates.
In this paper, we propose an automated latent fingerprint recognition algorithm
that utilizes Convolutional Neural Networks (ConvNets) for ridge flow
estimation and minutiae descriptor extraction, and extract complementary
templates (two minutiae templates and one texture template) to represent the
latent. The comparison scores between the latent and a reference print based on
the three templates are fused to retrieve a short candidate list from the
reference database. Experimental results show that the rank-1 identification
accuracies (query latent is matched with its true mate in the reference
database) are 64.7% for the NIST SD27 and 75.3% for the WVU latent databases,
against a reference database of 100K rolled prints. These results are the best
among published papers on latent recognition and competitive with the
performance (66.7% and 70.8% rank-1 accuracies on NIST SD27 and WVU DB,
respectively) of a leading COTS latent Automated Fingerprint Identification
System (AFIS). By score-level (rank-level) fusion of our system with the
commercial off-the-shelf (COTS) latent AFIS, the overall rank-1 identification
performance can be improved from 64.7% and 75.3% to 73.3% (74.4%) and 76.6%
(78.4%) on NIST SD27 and WVU latent databases, respectively.