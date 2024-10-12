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
We consider the \((1+\epsilon)\)-approximate nearest neighbor search problem: given a set \(X\) of \(n\) points in a \(d\)-dimensional space, build a data structure that, given any query point \(y\), finds a point \(x \in X\) whose distance to \(y\) is at most \((1+\epsilon) \min\_\&amp;\#123;x \in X\&amp;\#125; \|x-y\|\) for an accuracy parameter \(\epsilon \in (0,1)\). Our main result is a data structure that occupies only \(O(\epsilon^\&amp;\#123;-2\&amp;\#125; n \log(n) \log(1/\epsilon))\) bits of space, assuming all point coordinates are integers in the range $\&amp;\#123;-n^&amp;\#123;O(1)&amp;\#125; \ldots n^&amp;\#123;O(1)&amp;\#125;\&amp;\#125;\(, i.e., the coordinates have \)O(\log n)$ bits of precision. This improves over the best previously known space bound of $O(\epsilon^&amp;\#123;-2&amp;\#125; n \log(n)^2)$, obtained via the randomized dimensionality reduction method of Johnson and Lindenstrauss (1984). We also consider the more general problem of estimating all distances from a collection of query points to all data points \(X\), and provide almost tight upper and lower bounds for the space complexity of this problem.
