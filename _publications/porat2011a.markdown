---
layout: publication
title: "A cuckoo hashing variant with improved memory utilization and insertion time"
authors: Porat Ely, Shalem Bar
conference: Arxiv
year: 2011
bibkey: porat2011a
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1104.5400"}
tags: ['ARXIV', 'TIP']
---
Cuckoo hashing [4] is a multiple choice hashing scheme in which each item can be placed in multiple locations, and collisions are resolved by moving items to their alternative locations. In the classical implementation of two-way cuckoo hashing, the memory is partitioned into contiguous disjoint fixed-size buckets. Each item is hashed to two buckets, and may be stored in any of the positions within those buckets. Ref. [2] analyzed a variation in which the buckets are contiguous and overlap. However, many systems retrieve data from secondary storage in same-size blocks called pages. Fetching a page is a relatively expensive process; but once a page is fetched, its contents can be accessed orders of magnitude faster. We utilize this property of memory retrieval, presenting a variant of cuckoo hashing incorporating the following constraint: each bucket must be fully contained in a single page, but buckets are not necessarily contiguous. Empirical results show that this modification increases memory utilization and decreases the number of iterations required to insert an item. If each item is hashed to two buckets of capacity two, the page size is 8, and each bucket is fully contained in a single page, the memory utilization equals 89.71% in the classical contiguous disjoint bucket variant, 93.78% in the contiguous overlapping bucket variant, and increases to 97.46% in our new non-contiguous bucket variant. When the memory utilization is 92% and we use breadth first search to look for a vacant position, the number of iterations required to insert a new item is dramatically reduced from 545 in the contiguous overlapping buckets variant to 52 in our new non-contiguous bucket variant. In addition to the empirical results, we present a theoretical lower bound on the memory utilization of our variation as a function of the page size.