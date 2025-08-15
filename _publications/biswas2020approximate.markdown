---
layout: publication
title: Approximate Nearest Neighbour Search On Privacy-aware Encoding Of User Locations
  To Identify Susceptible Infections In Simulated Epidemics
authors: Chandan Biswas, Debasis Ganguly, Ujjwal Bhattacharya
conference: Forum for Information Retrieval Evaluation
year: 2021
bibkey: biswas2020approximate
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.08851'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Similarity Search"]
short_authors: Chandan Biswas, Debasis Ganguly, Ujjwal Bhattacharya
---
Amidst an increasing number of infected cases during the Covid-19 pandemic,
it is essential to trace, as early as possible, the susceptible people who
might have been infected by the disease due to their close proximity with
people who were tested positive for the virus. This early contact tracing is
likely to limit the rate of spread of the infection within a locality. In this
paper, we investigate how effectively and efficiently can such a list of
susceptible people be found given a list of infected persons and their
locations. To address this problem from an information retrieval (search)
perspective, we represent the location of each person at each time instant as a
point in a vector space. By using the locations of the given list of infected
persons as queries, we investigate the feasibility of applying approximate
nearest neighbour (ANN) based indexing and retrieval approaches to obtain a
list of top-k suspected users in real-time. Since leveraging information from
true user location data can lead to security and privacy concerns, we also
investigate what effects does distance-preserving encoding methods have on the
effectiveness of the ANN methods. Experiments conducted on real and synthetic
datasets demonstrate that the top-k retrieved lists of susceptible users
retrieved with existing ANN approaches (KD-tree and HNSW) yield satisfactory
precision and recall values, thus indicating that ANN approaches can
potentially be applied in practice to facilitate real-time contact tracing even
under the presence of imposed privacy constraints.