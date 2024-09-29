---
layout: publication
title: One45;pass One45;hash N45;gram Statistics Estimation
authors: Lemire Daniel, Kaser Owen
conference: "Arxiv"
year: 2006
bibkey: lemire2006statistics
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/cs/0610010"}
tags: ['ARXIV', 'Independent']
---
In multimedia text or bioinformatics databases applications query sequences of n consecutive symbols called n45;grams. Estimating the number of distinct n45;grams is a view45;size estimation problem. While view sizes can be estimated by sampling under statistical assumptions we desire an unassuming algorithm with universally valid accuracy bounds. Most related work has focused on repeatedly hashing the data which is prohibitive for large data sources. We prove that a one45;pass one45;hash algorithm is sufficient for accurate estimates if the hashing is sufficiently independent. To reduce costs further we investigate recursive random hashing algorithms and show that they are sufficiently independent in practice. We compare our running times with exact counts using suffix arrays and show that while we use hardly any storage we are an order of magnitude faster. The approach further is extended to a one45;pass/one45;hash computation of n45;gram entropy and iceberg counts. The experiments use a large collection of English text from the Gutenberg Project as well as synthetic data.
