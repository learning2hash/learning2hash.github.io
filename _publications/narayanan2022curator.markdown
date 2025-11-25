---
layout: publication
title: 'Curator: Creating Large-scale Curated Labelled Datasets Using Self-supervised
  Learning'
authors: Tarun Narayanan, Ajay Krishnan, Anirudh Koul, Siddha Ganju
conference: Arxiv
year: 2022
bibkey: narayanan2022curator
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.14099'}]
tags: ["Datasets", "Scalability", "Self-Supervised"]
short_authors: Narayanan et al.
---
Applying Machine learning to domains like Earth Sciences is impeded by the
lack of labeled data, despite a large corpus of raw data available in such
domains. For instance, training a wildfire classifier on satellite imagery
requires curating a massive and diverse dataset, which is an expensive and
time-consuming process that can span from weeks to months. Searching for
relevant examples in over 40 petabytes of unlabelled data requires researchers
to manually hunt for such images, much like finding a needle in a haystack. We
present a no-code end-to-end pipeline, Curator, which dramatically minimizes
the time taken to curate an exhaustive labeled dataset. Curator is able to
search massive amounts of unlabelled data by combining self-supervision,
scalable nearest neighbor search, and active learning to learn and
differentiate image representations. The pipeline can also be readily applied
to solve problems across different domains. Overall, the pipeline makes it
practical for researchers to go from just one reference image to a
comprehensive dataset in a diminutive span of time.