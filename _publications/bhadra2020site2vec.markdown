---
layout: publication
title: 'Site2vec: A Reference Frame Invariant Algorithm For Vector Embedding Of Protein-ligand
  Binding Sites'
authors: Arnab Bhadra, Kalidas Y
conference: 'Machine Learning: Science and Technology'
year: 2020
bibkey: bhadra2020site2vec
citations: 7
additional_links: [{name: Code, url: 'http://services.iittp.ac.in/bioinfo/home'},
  {name: Paper, url: 'https://arxiv.org/abs/2003.08149'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "Neural Hashing"]
short_authors: Arnab Bhadra, Kalidas Y
---
Protein-ligand interactions are one of the fundamental types of molecular
interactions in living systems. Ligands are small molecules that interact with
protein molecules at specific regions on their surfaces called binding sites.
Tasks such as assessment of protein functional similarity and detection of side
effects of drugs need identification of similar binding sites of disparate
proteins across diverse pathways. Machine learning methods for similarity
assessment require feature descriptors of binding sites. Traditional methods
based on hand engineered motifs and atomic configurations are not scalable
across several thousands of sites. In this regard, deep neural network
algorithms are now deployed which can capture very complex input feature space.
However, one fundamental challenge in applying deep learning to structures of
binding sites is the input representation and the reference frame. We report
here a novel algorithm Site2Vec that derives reference frame invariant vector
embedding of a protein-ligand binding site. The method is based on pairwise
distances between representative points and chemical compositions in terms of
constituent amino acids of a site. The vector embedding serves as a locality
sensitive hash function for proximity queries and determining similar sites.
The method has been the top performer with more than 95% quality scores in
extensive benchmarking studies carried over 10 datasets and against 23 other
site comparison methods. The algorithm serves for high throughput processing
and has been evaluated for stability with respect to reference frame shifts,
coordinate perturbations and residue mutations. We provide Site2Vec as a stand
alone executable and a web service hosted at
http://services.iittp.ac.in/bioinfo/home.