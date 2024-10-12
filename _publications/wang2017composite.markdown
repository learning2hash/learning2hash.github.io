---
layout: publication
title: Composite Quantization
authors: Wang Jingdong, Zhang Ting
conference: "Arxiv"
year: 2017
bibkey: wang2017composite
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1712.00955"}
tags: ['ARXIV', 'Quantisation']
---
This paper studies the compact coding approach to approximate nearest neighbor search. We introduce a composite quantization framework. It uses the composition of several (\(M\)) elements, each of which is selected from a different dictionary, to accurately approximate a \(D\)-dimensional vector, thus yielding accurate search, and represents the data vector by a short code composed of the indices of the selected elements in the corresponding dictionaries. Our key contribution lies in introducing a near-orthogonality constraint, which makes the search efficiency is guaranteed as the cost of the distance computation is reduced to \(O(M)\) from \(O(D)\) through a distance table lookup scheme. The resulting approach is called near-orthogonal composite quantization. We theoretically justify the equivalence between near-orthogonal composite quantization and minimizing an upper bound of a function formed by jointly considering the quantization error and the search cost according to a generalized triangle inequality. We empirically show the efficacy of the proposed approach over several benchmark datasets. In addition, we demonstrate the superior performances in other three applications: combination with inverted multi-index, quantizing the query for mobile search, and inner-product similarity search.
