---
layout: publication
title: Approximate Nearest Neighbors In Limited Space
authors: Indyk Piotr, Wagner Tal
conference: "Arxiv"
year: 2018
bibkey: indyk2018approximate
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1807.00112"}
tags: ['ARXIV', 'Unsupervised']
---
We consider the \{&#37; raw &#37;\}\\((1+\epsilon)\\)\{&#37; endraw &#37;\}-approximate nearest neighbor search problem: given a set \{&#37; raw &#37;\}\\(X\\)\{&#37; endraw &#37;\} of \{&#37; raw &#37;\}\\(n\\)\{&#37; endraw &#37;\} points in a \{&#37; raw &#37;\}\\(d\\)\{&#37; endraw &#37;\}-dimensional space, build a data structure that, given any query point \{&#37; raw &#37;\}\\(y\\)\{&#37; endraw &#37;\}, finds a point \{&#37; raw &#37;\}\\(x \in X\\)\{&#37; endraw &#37;\} whose distance to \{&#37; raw &#37;\}\\(y\\)\{&#37; endraw &#37;\} is at most \{&#37; raw &#37;\}\\((1+\epsilon) \min\_\{x \in X\} \|x-y\|\\)\{&#37; endraw &#37;\} for an accuracy parameter \{&#37; raw &#37;\}\\(\epsilon \in (0,1)\\)\{&#37; endraw &#37;\}. Our main result is a data structure that occupies only \{&#37; raw &#37;\}\\(O(\epsilon^\{-2\} n \log(n) \log(1/\epsilon))\\)\{&#37; endraw &#37;\} bits of space, assuming all point coordinates are integers in the range $\\{-n^\{O(1)\} \ldots n^\{O(1)\}\\}\{&#37; raw &#37;\}\\(, i.e., the coordinates have \\)\{&#37; endraw &#37;\}O(\log n)$ bits of precision. This improves over the best previously known space bound of $O(\epsilon^\{-2\} n \log(n)^2)$, obtained via the randomized dimensionality reduction method of Johnson and Lindenstrauss (1984). We also consider the more general problem of estimating all distances from a collection of query points to all data points \{&#37; raw &#37;\}\\(X\\)\{&#37; endraw &#37;\}, and provide almost tight upper and lower bounds for the space complexity of this problem.
