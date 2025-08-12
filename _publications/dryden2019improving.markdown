---
layout: publication
title: Improving Strong-scaling Of CNN Training By Exploiting Finer-grained Parallelism
authors: Nikoli Dryden, Naoya Maruyama, Tom Benson, Tim Moon, Marc Snir, Brian van
  Essen
conference: 2019 IEEE International Parallel and Distributed Processing Symposium
  (IPDPS)
year: 2019
bibkey: dryden2019improving
citations: 44
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.06681'}]
tags: []
short_authors: Dryden et al.
---
Scaling CNN training is necessary to keep up with growing datasets and reduce
training time. We also see an emerging need to handle datasets with very large
samples, where memory requirements for training are large. Existing training
frameworks use a data-parallel approach that partitions samples within a
mini-batch, but limits to scaling the mini-batch size and memory consumption
makes this untenable for large samples. We describe and implement new
approaches to convolution, which parallelize using spatial decomposition or a
combination of sample and spatial decomposition. This introduces many
performance knobs for a network, so we develop a performance model for CNNs and
present a method for using it to automatically determine efficient
parallelization strategies.
  We evaluate our algorithms with microbenchmarks and image classification with
ResNet-50. Our algorithms allow us to prototype a model for a mesh-tangling
dataset, where sample sizes are very large. We show that our parallelization
achieves excellent strong and weak scaling and enables training for previously
unreachable datasets.