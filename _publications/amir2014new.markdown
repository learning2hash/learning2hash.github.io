---
layout: publication
title: 'Polynomials: A New Tool For Length Reduction In Binary Discrete Convolutions'
authors: Amihood Amir, Oren Kapah, Ely Porat, Amir Rothschild
conference: "Arxiv"
year: 2014
citations: 3
bibkey: amir2014new
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1410.5607'}
tags: ['Evaluation Metrics', 'Applications']
---
Efficient handling of sparse data is a key challenge in Computer Science.
Binary convolutions, such as polynomial multiplication or the Walsh Transform
are a useful tool in many applications and are efficiently solved.
  In the last decade, several problems required efficient solution of sparse
binary convolutions. both randomized and deterministic algorithms were
developed for efficiently computing the sparse polynomial multiplication. The
key operation in all these algorithms was length reduction. The sparse data is
mapped into small vectors that preserve the convolution result. The reduction
method used to-date was the modulo function since it preserves location (of the
"1" bits) up to cyclic shift.
  To date there is no known efficient algorithm for computing the sparse Walsh
transform. Since the modulo function does not preserve the Walsh transform a
new method for length reduction is needed. In this paper we present such a new
method - polynomials. This method enables the development of an efficient
algorithm for computing the binary sparse Walsh transform. To our knowledge,
this is the first such algorithm. We also show that this method allows a faster
deterministic computation of sparse polynomial multiplication than currently
known in the literature.
