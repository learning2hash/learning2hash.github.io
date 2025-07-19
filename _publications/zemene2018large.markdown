---
layout: publication
title: Large-scale Image Geo-Localization Using Dominant Sets
authors: Zemene et al.
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2018
bibkey: zemene2018large
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.01238'}]
tags: [SCALABILITY]
---
This paper presents a new approach for the challenging problem of
geo-locating an image using image matching in a structured database of
city-wide reference images with known GPS coordinates. We cast the
geo-localization as a clustering problem on local image features. Akin to
existing approaches on the problem, our framework builds on low-level features
which allow partial matching between images. For each local feature in the
query image, we find its approximate nearest neighbors in the reference set.
Next, we cluster the features from reference images using Dominant Set
clustering, which affords several advantages over existing approaches. First,
it permits variable number of nodes in the cluster which we use to dynamically
select the number of nearest neighbors (typically coming from multiple
reference images) for each query feature based on its discrimination value.
Second, as we also quantify in our experiments, this approach is several orders
of magnitude faster than existing approaches. Thus, we obtain multiple clusters
(different local maximizers) and obtain a robust final solution to the problem
using multiple weak solutions through constrained Dominant Set clustering on
global image features, where we enforce the constraint that the query image
must be included in the cluster. This second level of clustering also bypasses
heuristic approaches to voting and selecting the reference image that matches
to the query. We evaluated the proposed framework on an existing dataset of
102k street view images as well as a new dataset of 300k images, and show that
it outperforms the state-of-the-art by 20% and 7%, respectively, on the two
datasets.