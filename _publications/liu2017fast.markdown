---
layout: publication
title: Fast Screening Algorithm For Rotation And Scale Invariant Template Matching
authors: Bolin Liu, Xiao Shu, Xiaolin Wu
conference: Arxiv
year: 2017
bibkey: liu2017fast
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.05647'}]
tags: ["Efficiency"]
short_authors: Bolin Liu, Xiao Shu, Xiaolin Wu
---
This paper presents a generic pre-processor for expediting conventional
template matching techniques. Instead of locating the best matched patch in the
reference image to a query template via exhaustive search, the proposed
algorithm rules out regions with no possible matches with minimum computational
efforts. While working on simple patch features, such as mean, variance and
gradient, the fast pre-screening is highly discriminative. Its computational
efficiency is gained by using a novel octagonal-star-shaped template and the
inclusion-exclusion principle to extract and compare patch features. Moreover,
it can handle arbitrary rotation and scaling of reference images effectively.
Extensive experiments demonstrate that the proposed algorithm greatly reduces
the search space while never missing the best match.