---
layout: publication
title: One Permutation Hashing
authors: Ping Li, Art Owen, Cun-hui Zhang
conference: "Neural Information Processing Systems"
year: 2012
bibkey: li2012one
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2012/hash/eaa32c96f620053cf442ad32258076b9-Abstract.html"}
tags: ['NEURIPS', 'Supervised']
---
While minwise hashing is promising for large-scale learning in massive binary data, the preprocessing cost is prohibitive as it requires applying (e.g.,) $k=500$ permutations on the data. The testing time is also expensive if a new data point (e.g., a new document or a new image) has not been processed. In this paper, we develop a simple \textbf\{one permutation hashing\} scheme to address this important issue. While it is true that the preprocessing step can be parallelized, it comes at the cost of additional hardware and implementation. Also, reducing $k$ permutations to just one would be much more \textbf\{energy-efficient\}, which might be an important perspective as minwise hashing is commonly deployed in the search industry. While the theoretical probability analysis is interesting, our experiments on similarity estimation and SVM \&amp; logistic regression also confirm the theoretical results.
