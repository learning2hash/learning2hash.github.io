---
layout: publication
title: 'Moleculenet: A Benchmark For Molecular Machine Learning'
authors: Zhenqin Wu, Bharath Ramsundar, Evan N. Feinberg, Joseph Gomes, Caleb Geniesse,
  Aneesh S. Pappu, Karl Leswing, Vijay Pande
conference: Chemical Science
year: 2017
bibkey: wu2017moleculenet
citations: 2323
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.00564'}]
tags: ["Datasets", "Evaluation", "Tools & Libraries"]
short_authors: Wu et al.
---
Molecular machine learning has been maturing rapidly over the last few years.
Improved methods and the presence of larger datasets have enabled machine
learning algorithms to make increasingly accurate predictions about molecular
properties. However, algorithmic progress has been limited due to the lack of a
standard benchmark to compare the efficacy of proposed methods; most new
algorithms are benchmarked on different datasets making it challenging to gauge
the quality of proposed methods. This work introduces MoleculeNet, a large
scale benchmark for molecular machine learning. MoleculeNet curates multiple
public datasets, establishes metrics for evaluation, and offers high quality
open-source implementations of multiple previously proposed molecular
featurization and learning algorithms (released as part of the DeepChem open
source library). MoleculeNet benchmarks demonstrate that learnable
representations are powerful tools for molecular machine learning and broadly
offer the best performance. However, this result comes with caveats. Learnable
representations still struggle to deal with complex tasks under data scarcity
and highly imbalanced classification. For quantum mechanical and biophysical
datasets, the use of physics-aware featurizations can be more important than
choice of particular learning algorithm.