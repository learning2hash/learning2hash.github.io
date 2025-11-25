---
layout: publication
title: Generative Retrieval As Dense Retrieval
authors: Thong Nguyen, Andrew Yates
conference: GenIR@SIGIR2023
year: 2023
bibkey: nguyen2023generative
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.11397'}]
tags: ["Datasets", "SIGIR", "Scalability", "Similarity Search"]
short_authors: Thong Nguyen, Andrew Yates
---
Generative retrieval is a promising new neural retrieval paradigm that aims
to optimize the retrieval pipeline by performing both indexing and retrieval
with a single transformer model. However, this new paradigm faces challenges
with updating the index and scaling to large collections. In this paper, we
analyze two prominent variants of generative retrieval and show that they can
be conceptually viewed as bi-encoders for dense retrieval. Specifically, we
analytically demonstrate that the generative retrieval process can be
decomposed into dot products between query and document vectors, similar to
dense retrieval. This analysis leads us to propose a new variant of generative
retrieval, called Tied-Atomic, which addresses the updating and scaling issues
by incorporating techniques from dense retrieval. In experiments on two
datasets, NQ320k and the full MSMARCO, we confirm that this approach does not
reduce retrieval effectiveness while enabling the model to scale to large
collections.