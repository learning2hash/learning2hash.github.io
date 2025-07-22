---
layout: publication
title: Vector Search With Small Radiuses
authors: "Szilvasy Gergely, Mazar\xE9 Pierre-emmanuel, Douze Matthijs"
conference: Arxiv
year: 2024
bibkey: szilvasy2024vector
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.10746'}]
tags: ["Vector-Indexing", "Evaluation", "Image-Retrieval", "Datasets"]
short_authors: "Szilvasy Gergely, Mazar\xE9 Pierre-emmanuel, Douze Matthijs"
---
In recent years, the dominant accuracy metric for vector search is the recall
of a result list of fixed size (top-k retrieval), considering as ground truth
the exact vector retrieval results. Although convenient to compute, this metric
is distantly related to the end-to-end accuracy of a full system that
integrates vector search. In this paper we focus on the common case where a
hard decision needs to be taken depending on the vector retrieval results, for
example, deciding whether a query image matches a database image or not. We
solve this as a range search task, where all vectors within a certain radius
from the query are returned.
  We show that the value of a range search result can be modeled rigorously
based on the query-to-vector distance. This yields a metric for range search,
RSM, that is both principled and easy to compute without running an end-to-end
evaluation. We apply this metric to the case of image retrieval. We show that
indexing methods that are adapted for top-k retrieval do not necessarily
maximize the RSM. In particular, for inverted file based indexes, we show that
visiting a limited set of clusters and encoding vectors compactly yields near
optimal results.