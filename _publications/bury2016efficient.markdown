---
layout: publication
title: Efficient Similarity Search In Dynamic Data Streams
authors: Bury Marc, Schwiegelshohn Chris, Sorella Mara
conference: "Arxiv"
year: 2016
bibkey: bury2016efficient
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1605.03949"}
tags: ['ARXIV', 'Independent', 'LSH']
---
The Jaccard index is an important similarity measure for item sets and Boolean data. On large datasets, an exact similarity computation is often infeasible for all item pairs both due to time and space constraints, giving rise to faster approximate methods. The algorithm of choice used to quickly compute the Jaccard index \{&#37; raw &#37;\}\\(\frac\{\vert A \cap B \vert\}\{\vert A\cup B\vert\}\\)\{&#37; endraw &#37;\} of two item sets \{&#37; raw &#37;\}\\(A\\)\{&#37; endraw &#37;\} and \{&#37; raw &#37;\}\\(B\\)\{&#37; endraw &#37;\} is usually a form of min-hashing. Most min-hashing schemes are maintainable in data streams processing only additions, but none are known to work when facing item-wise deletions. In this paper, we investigate scalable approximation algorithms for rational set similarities, a broad class of similarity measures including Jaccard. Motivated by a result of Chierichetti and Kumar [J. ACM 2015] who showed any rational set similarity \{&#37; raw &#37;\}\\(S\\)\{&#37; endraw &#37;\} admits a locality sensitive hashing (LSH) scheme if and only if the corresponding distance \{&#37; raw &#37;\}\\(1-S\\)\{&#37; endraw &#37;\} is a metric, we can show that there exists a space efficient summary maintaining a \{&#37; raw &#37;\}\\((1\pm \varepsilon)\\)\{&#37; endraw &#37;\} multiplicative approximation to \{&#37; raw &#37;\}\\(1-S\\)\{&#37; endraw &#37;\} in dynamic data streams. This in turn also yields a \{&#37; raw &#37;\}\\(\varepsilon\\)\{&#37; endraw &#37;\} additive approximation of the similarity. The existence of these approximations hints at, but does not directly imply a LSH scheme in dynamic data streams. Our second and main contribution now lies in the design of such a LSH scheme maintainable in dynamic data streams. The scheme is space efficient, easy to implement and to the best of our knowledge the first of its kind able to process deletions.
