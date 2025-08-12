---
layout: publication
title: 'Masksearch: Querying Image Masks At Scale'
authors: Dong He, Jieyu Zhang, Maureen Daum, Alexander Ratner, Magdalena Balazinska
conference: Arxiv
year: 2023
bibkey: he2023masksearch
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.02375'}]
tags: ["Tools & Libraries"]
short_authors: He et al.
---
Machine learning tasks over image databases often generate masks that
annotate image content (e.g., saliency maps, segmentation maps, depth maps) and
enable a variety of applications (e.g., determine if a model is learning
spurious correlations or if an image was maliciously modified to mislead a
model). While queries that retrieve examples based on mask properties are
valuable to practitioners, existing systems do not support them efficiently. In
this paper, we formalize the problem and propose MaskSearch, a system that
focuses on accelerating queries over databases of image masks while
guaranteeing the correctness of query results. MaskSearch leverages a novel
indexing technique and an efficient filter-verification query execution
framework. Experiments with our prototype show that MaskSearch, using indexes
approximately 5% of the compressed data size, accelerates individual queries by
up to two orders of magnitude and consistently outperforms existing methods on
various multi-query workloads that simulate dataset exploration and analysis
processes.