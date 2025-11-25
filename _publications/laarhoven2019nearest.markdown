---
layout: publication
title: Nearest Neighbor Decoding For Tardos Fingerprinting Codes
authors: Thijs Laarhoven
conference: Proceedings of the ACM Workshop on Information Hiding and Multimedia Security
year: 2019
bibkey: laarhoven2019nearest
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.06196'}]
tags: ["Compact Codes", "Efficiency", "Privacy & Security", "Similarity Search"]
short_authors: Thijs Laarhoven
---
Over the past decade, various improvements have been made to Tardos'
collusion-resistant fingerprinting scheme [Tardos, STOC 2003], ultimately
resulting in a good understanding of what is the minimum code length required
to achieve collusion-resistance. In contrast, decreasing the cost of the actual
decoding algorithm for identifying the potential colluders has received less
attention, even though previous results have shown that using joint decoding
strategies, deemed too expensive for decoding, may lead to better code lengths.
Moreover, in dynamic settings a fast decoder may be required to provide answers
in real-time, further raising the question whether the decoding costs of
score-based fingerprinting schemes can be decreased with a smarter decoding
algorithm. In this paper we show how to model the decoding step of score-based
fingerprinting as a nearest neighbor search problem, and how this relation
allows us to apply techniques from the field of (approximate) nearest neighbor
searching to obtain decoding times which are sublinear in the total number of
users. As this does not affect the encoding and embedding steps, this decoding
mechanism can easily be deployed within existing fingerprinting schemes, and
this may bring a truly efficient joint decoder closer to reality. Besides the
application to fingerprinting, similar techniques can be used to decrease the
decoding costs of group testing methods, which may be of independent interest.