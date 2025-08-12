---
layout: publication
title: Towards Accurate Camera Geopositioning By Image Matching
authors: Raffaele Imbriaco, Clint Sebastian, Egor Bondarev, Peter de With
conference: Arxiv
year: 2019
bibkey: imbriaco2019towards
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.05454'}]
tags: ["Evaluation"]
short_authors: Imbriaco et al.
---
In this work, we present a camera geopositioning system based on matching a
query image against a database with panoramic images. For matching, our system
uses memory vectors aggregated from global image descriptors based on
convolutional features to facilitate fast searching in the database. To speed
up searching, a clustering algorithm is used to balance geographical
positioning and computation time. We refine the obtained position from the
query image using a new outlier removal algorithm. The matching of the query
image is obtained with a recall@5 larger than 90% for panorama-to-panorama
matching. We cluster available panoramas from geographically adjacent locations
into a single compact representation and observe computational gains of
approximately 50% at the cost of only a small (approximately 3%) recall loss.
Finally, we present a coordinate estimation algorithm that reduces the median
geopositioning error by up to 20%.