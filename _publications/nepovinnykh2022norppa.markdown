---
layout: publication
title: 'NORPPA: Novel Ringed Seal Re-identification By Pelage Pattern Aggregation'
authors: "Ekaterina Nepovinnykh, Ilia Chelak, Tuomas Eerola, Heikki K\xE4lvi\xE4inen"
conference: Arxiv
year: 2022
bibkey: nepovinnykh2022norppa
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.02498'}]
tags: [Evaluation, Image Retrieval, Datasets]
short_authors: Nepovinnykh et al.
---
We propose a method for Saimaa ringed seal (Pusa hispida saimensis)
re-identification. Access to large image volumes through camera trapping and
crowdsourcing provides novel possibilities for animal monitoring and
conservation and calls for automatic methods for analysis, in particular, when
re-identifying individual animals from the images. The proposed method NOvel
Ringed seal re-identification by Pelage Pattern Aggregation (NORPPA) utilizes
the permanent and unique pelage pattern of Saimaa ringed seals and
content-based image retrieval techniques. First, the query image is
preprocessed, and each seal instance is segmented. Next, the seal's pelage
pattern is extracted using a U-net encoder-decoder based method. Then,
CNN-based affine invariant features are embedded and aggregated into Fisher
Vectors. Finally, the cosine distance between the Fisher Vectors is used to
find the best match from a database of known individuals. We perform extensive
experiments of various modifications of the method on a new challenging Saimaa
ringed seals re-identification dataset. The proposed method is shown to produce
the best re-identification accuracy on our dataset in comparisons with
alternative approaches.