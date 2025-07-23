---
layout: publication
title: 'A Line In The Sand: Recommendation Or Ad-hoc Retrieval?'
authors: Kallumadi Surya, Mitra Bhaskar, Iofciu Tereza
conference: Arxiv
year: 2018
bibkey: kallumadi2018line
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.08061'}]
tags: ["Evaluation", "Recommender Systems"]
short_authors: Kallumadi Surya, Mitra Bhaskar, Iofciu Tereza
---
The popular approaches to recommendation and ad-hoc retrieval tasks are
largely distinct in the literature. In this work, we argue that many
recommendation problems can also be cast as ad-hoc retrieval tasks. To
demonstrate this, we build a solution for the RecSys 2018 Spotify challenge by
combining standard ad-hoc retrieval models and using popular retrieval tools
sets. We draw a parallel between the playlist continuation task and the task of
finding good expansion terms for queries in ad-hoc retrieval, and show that
standard pseudo-relevance feedback can be effective as a collaborative
filtering approach. We also use ad-hoc retrieval for content-based
recommendation by treating the input playlist title as a query and associating
all candidate tracks with meta-descriptions extracted from the background data.
The recommendations from these two approaches are further supplemented by a
nearest neighbor search based on track embeddings learned by a popular neural
model. Our final ranked list of recommendations is produced by a learning to
rank model. Our proposed solution using ad-hoc retrieval models achieved a
competitive performance on the music recommendation task at RecSys 2018
challenge---finishing at rank 7 out of 112 participating teams and at rank 5
out of 31 teams for the main and the creative tracks, respectively.