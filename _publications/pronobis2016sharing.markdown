---
layout: publication
title: Sharing Hash Codes For Multiple Purposes
authors: Wikor Pronobis, Danny Panknin, Johannes Kirschnick, Vignesh Srinivasan, Wojciech
  Samek, Volker Markl, Manohar Kaul, Klaus-robert Mueller, Shinichi Nakajima
conference: Japanese Journal of Statistics and Data Science
year: 2018
bibkey: pronobis2016sharing
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1609.03219'}]
tags: [Hashing Methods, Locality Sensitive Hashing, Efficiency, Evaluation]
short_authors: Pronobis et al.
---
Locality sensitive hashing (LSH) is a powerful tool for sublinear-time
approximate nearest neighbor search, and a variety of hashing schemes have been
proposed for different dissimilarity measures. However, hash codes
significantly depend on the dissimilarity, which prohibits users from adjusting
the dissimilarity at query time. In this paper, we propose \{multiple purpose
LSH (mp-LSH) which shares the hash codes for different dissimilarities. mp-LSH
supports L2, cosine, and inner product dissimilarities, and their corresponding
weighted sums, where the weights can be adjusted at query time. It also allows
us to modify the importance of pre-defined groups of features. Thus, mp-LSH
enables us, for example, to retrieve similar items to a query with the user
preference taken into account, to find a similar material to a query with some
properties (stability, utility, etc.) optimized, and to turn on or off a part
of multi-modal information (brightness, color, audio, text, etc.) in
image/video retrieval. We theoretically and empirically analyze the performance
of three variants of mp-LSH, and demonstrate their usefulness on real-world
data sets.