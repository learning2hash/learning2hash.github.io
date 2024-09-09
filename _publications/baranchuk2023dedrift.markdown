---
layout: publication
title: "DeDrift: Robust Similarity Search under Content Drift"
authors: Baranchuk Dmitry, Douze Matthijs, Upadhyay Yash, Yalniz I. Zeki
conference: Arxiv
year: 2023
bibkey: baranchuk2023dedrift
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2308.02752"}
tags: ['ARXIV']
---
The statistical distribution of content uploaded and searched on media sharing sites changes over time due to seasonal, sociological and technical factors. We investigate the impact of this "content drift" for large-scale similarity search tools, based on nearest neighbor search in embedding space. Unless a costly index reconstruction is performed frequently, content drift degrades the search accuracy and efficiency. The degradation is especially severe since, in general, both the query and database distributions change. We introduce and analyze real-world image and video datasets for which temporal information is available over a long time period. Based on the learnings, we devise DeDrift, a method that updates embedding quantizers to continuously adapt large-scale indexing structures on-the-fly. DeDrift almost eliminates the accuracy degradation due to the query and database content drift while being up to 100x faster than a full index reconstruction.