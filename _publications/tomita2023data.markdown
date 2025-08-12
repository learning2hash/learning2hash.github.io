---
layout: publication
title: Data-efficient Sequence-based Visual Place Recognition With Highly Compressed
  JPEG Images
authors: Mihnea-Alexandru Tomita, Bruno Ferrarini, Michael Milford, Klaus McDonald-Maier,
  Shoaib Ehsan
conference: Arxiv
year: 2023
bibkey: tomita2023data
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.13314'}]
tags: []
short_authors: Tomita et al.
---
Visual Place Recognition (VPR) is a fundamental task that allows a robotic
platform to successfully localise itself in the environment. For decentralised
VPR applications where the visual data has to be transmitted between several
agents, the communication channel may restrict the localisation process when
limited bandwidth is available. JPEG is an image compression standard that can
employ high compression ratios to facilitate lower data transmission for VPR
applications. However, when applying high levels of JPEG compression, both the
image clarity and size are drastically reduced. In this paper, we incorporate
sequence-based filtering in a number of well-established, learnt and non-learnt
VPR techniques to overcome the performance loss resulted from introducing high
levels of JPEG compression. The sequence length that enables 100% place
matching performance is reported and an analysis of the amount of data required
for each VPR technique to perform the transfer on the entire spectrum of JPEG
compression is provided. Moreover, the time required by each VPR technique to
perform place matching is investigated, on both uniformly and non-uniformly
JPEG compressed data. The results show that it is beneficial to use a highly
compressed JPEG dataset with an increased sequence length, as similar levels of
VPR performance are reported at a significantly reduced bandwidth. The results
presented in this paper also emphasize that there is a trade-off between the
amount of data transferred and the total time required to perform VPR. Our
experiments also suggest that is often favourable to compress the query images
to the same quality of the map, as more efficient place matching can be
performed. The experiments are conducted on several VPR datasets, under mild to
extreme JPEG compression.