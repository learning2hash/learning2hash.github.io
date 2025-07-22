---
layout: publication
title: Linear Cross-modal Hashing For Efficient Multimedia Search
authors: Zhu Xiaofeng, Huang, Shen, Zhao
conference: Proceedings of the 21st ACM international conference on Multimedia
year: 2013
bibkey: zhu2013linear
citations: 278
additional_links: [{name: Paper, url: 'https://dl.acm.org/citation.cfm?id=2502107'}]
tags: ["Hashing-Methods", "Scalability", "Datasets", "Compact-Codes", "Evaluation"]
short_authors: Zhu et al.
---
Most existing cross-modal hashing methods suffer from the scalability issue in the training phase. In this paper, we propose a novel 
cross-modal hashing approach with a linear time complexity to the training data size, to enable scalable indexing for multimedia 
search across multiple modals. Taking both the intra-similarity in each modal and the inter-similarity across different modals 
into consideration, the proposed approach aims at effectively learning hash functions from large-scale training datasets. 
More specifically, for each modal, we first partition the training data into \\(k\\) clusters and then represent each training data 
point with its distances to \\(k\\) centroids of the clusters. Interestingly, such a k-dimensional data representation can reduce 
the time complexity of the training phase from traditional O(n2) or higher to O(n), where \\(n\\) is the training data size, leading to 
practical learning on large-scale datasets. We further prove that this new representation preserves the intra-similarity in each modal. 
To preserve the inter-similarity among data points across different modals, we transform the derived data representations into a 
common binary subspace in which binary codes from all the modals are "consistent" and comparable. The transformation simultaneously 
outputs the hash functions for all modals, which are used to convert unseen data into binary codes. Given a query of one modal, 
it is first mapped into the binary codes using the modal's hash functions, followed by matching the database binary codes of any other 
modals. Experimental results on two benchmark datasets confirm the scalability and the effectiveness of the proposed approach in 
comparison with the state of the art.