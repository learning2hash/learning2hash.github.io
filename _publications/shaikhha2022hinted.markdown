---
layout: publication
title: 'Hinted Dictionaries: Efficient Functional Ordered Sets And Maps'
authors: Amir Shaikhha, Mahdi Ghorbani, Hesam Shahrokhi
conference: Arxiv
year: 2022
bibkey: shaikhha2022hinted
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.04380'}]
tags: ["Tools & Libraries"]
short_authors: Amir Shaikhha, Mahdi Ghorbani, Hesam Shahrokhi
---
This article introduces hinted dictionaries for expressing efficient ordered
sets and maps functionally. As opposed to the traditional ordered dictionaries
with logarithmic operations, hinted dictionaries can achieve better performance
by using cursor-like objects referred to as hints. Hinted dictionaries unify
the interfaces of imperative ordered dictionaries (e.g., C++ maps) and
functional ones (e.g., Adams' sets). We show that such dictionaries can use
sorted arrays, unbalanced trees, and balanced trees as their underlying
representations. Throughout the article, we use Scala to present the different
components of hinted dictionaries. We also provide a C++ implementation to
evaluate the effectiveness of hinted dictionaries. Hinted dictionaries provide
superior performance for set-set operations in comparison with the standard
library of C++. Also, they show a competitive performance in comparison with
the SciPy library for sparse vector operations.