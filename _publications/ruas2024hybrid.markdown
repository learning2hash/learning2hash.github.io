---
layout: publication
title: 'Hybrid X-linker: Automated Data Generation And Extreme Multi-label Ranking
  For Biomedical Entity Linking'
authors: Pedro Ruas, Fernando Gallego, Francisco J. Veredas, Francisco M. Couto
conference: Arxiv
year: 2024
bibkey: ruas2024hybrid
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.06292'}]
tags: ["Datasets"]
short_authors: Ruas et al.
---
State-of-the-art deep learning entity linking methods rely on extensive
human-labelled data, which is costly to acquire. Current datasets are limited
in size, leading to inadequate coverage of biomedical concepts and diminished
performance when applied to new data. In this work, we propose to automatically
generate data to create large-scale training datasets, which allows the
exploration of approaches originally developed for the task of extreme
multi-label ranking in the biomedical entity linking task. We propose the
hybrid X-Linker pipeline that includes different modules to link disease and
chemical entity mentions to concepts in the MEDIC and the CTD-Chemical
vocabularies, respectively. X-Linker was evaluated on several biomedical
datasets: BC5CDR-Disease, BioRED-Disease, NCBI-Disease, BC5CDR-Chemical,
BioRED-Chemical, and NLM-Chem, achieving top-1 accuracies of 0.8307, 0.7969,
0.8271, 0.9511, 0.9248, and 0.7895, respectively. X-Linker demonstrated
superior performance in three datasets: BC5CDR-Disease, NCBI-Disease, and
BioRED-Chemical. In contrast, SapBERT outperformed X-Linker in the remaining
three datasets. Both models rely only on the mention string for their
operations. The source code of X-Linker and its associated data are publicly
available for performing biomedical entity linking without requiring
pre-labelled entities with identifiers from specific knowledge organization
systems.