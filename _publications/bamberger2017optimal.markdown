---
layout: publication
title: Optimal Fast Johnson-lindenstrauss Embeddings For Large Data Sets
authors: Stefan Bamberger, Felix Krahmer
conference: Sampling Theory, Signal Processing, and Data Analysis
year: 2017
bibkey: bamberger2017optimal
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.01774'}]
tags: [Uncategorized]
short_authors: Stefan Bamberger, Felix Krahmer
---
Johnson-Lindenstrauss embeddings are widely used to reduce the dimension and
thus the processing time of data. To reduce the total complexity, also fast
algorithms for applying these embeddings are necessary. To date, such fast
algorithms are only available either for a non-optimal embedding dimension or
up to a certain threshold on the number of data points.
  We address a variant of this problem where one aims to simultaneously embed
larger subsets of the data set. Our method follows an approach by Nelson: A
subsampled Hadamard transform maps points into a space of lower, but not
optimal dimension. Subsequently, a random matrix with independent entries
projects to an optimal embedding dimension.
  For subsets whose size scales at least polynomially in the ambient dimension,
the complexity of this method comes close to the number of operations just to
read the data under mild assumptions on the size of the data set that are
considerably less restrictive than in previous works. We also prove a lower
bound showing that subsampled Hadamard matrices alone cannot reach an optimal
embedding dimension. Hence, the second embedding cannot be omitted.