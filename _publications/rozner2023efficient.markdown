---
layout: publication
title: Efficient Verification-based Face Identification
authors: Amit Rozner, Barak Battash, Ofir Lindenbaum, Lior Wolf
conference: Arxiv
year: 2023
bibkey: rozner2023efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.13240'}]
tags: [Datasets, Efficiency]
short_authors: Rozner et al.
---
We study the problem of performing face verification with an efficient neural
model \(f\). The efficiency of \(f\) stems from simplifying the face verification
problem from an embedding nearest neighbor search into a binary problem; each
user has its own neural network \(f\). To allow information sharing between
different individuals in the training set, we do not train \(f\) directly but
instead generate the model weights using a hypernetwork \(h\). This leads to the
generation of a compact personalized model for face identification that can be
deployed on edge devices. Key to the method's success is a novel way of
generating hard negatives and carefully scheduling the training objectives. Our
model leads to a substantially small \(f\) requiring only 23k parameters and 5M
floating point operations (FLOPS). We use six face verification datasets to
demonstrate that our method is on par or better than state-of-the-art models,
with a significantly reduced number of parameters and computational burden.
Furthermore, we perform an extensive ablation study to demonstrate the
importance of each element in our method.