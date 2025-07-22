---
layout: publication
title: 'TISIS : Trajectory Indexing For Similarity Search'
authors: Jarrad Sara, Naacke Hubert, Gancarski Stephane
conference: Arxiv
year: 2024
bibkey: jarrad2024tisis
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.11301'}]
tags: ["Evaluation", "Similarity-Search", "Scalability", "Datasets"]
short_authors: Jarrad Sara, Naacke Hubert, Gancarski Stephane
---
Social media platforms enable users to share diverse types of information,
including geolocation data that captures their movement patterns. Such
geolocation data can be leveraged to reconstruct the trajectory of a user's
visited Points of Interest (POIs). A key requirement in numerous applications
is the ability to measure the similarity between such trajectories, as this
facilitates the retrieval of trajectories that are similar to a given reference
trajectory. This is the main focus of our work. Existing methods predominantly
rely on applying a similarity function to each candidate trajectory to identify
those that are sufficiently similar. However, this approach becomes
computationally expensive when dealing with large-scale datasets. To mitigate
this challenge, we propose TISIS, an efficient method that uses trajectory
indexing to quickly find similar trajectories that share common POIs in the
same order. Furthermore, to account for scenarios where POIs in trajectories
may not exactly match but are contextually similar, we introduce TISIS*, a
variant of TISIS that incorporates POI embeddings. This extension allows for
more comprehensive retrieval of similar trajectories by considering semantic
similarities between POIs, beyond mere exact matches. Extensive experimental
evaluations demonstrate that the proposed approach significantly outperforms a
baseline method based on the well-known Longest Common SubSequence (LCSS)
algorithm, yielding substantial performance improvements across various
real-world datasets.