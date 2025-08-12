---
layout: publication
title: 'K-sort: A New Sorting Algorithm That Beats Heap Sort For N <= 70 Lakhs!'
authors: Kiran Kumar Sundararajan, Mita Pal, Soubhik Chakraborty, N. C. Mahanti
conference: Arxiv
year: 2011
bibkey: sundararajan2011k
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1107.3622'}]
tags: ["Efficiency", "Scalability"]
short_authors: Sundararajan et al.
---
Sundararajan and Chakraborty (2007) introduced a new version of Quick sort
removing the interchanges. Khreisat (2007) found this algorithm to be competing
well with some other versions of Quick sort. However, it uses an auxiliary
array thereby increasing the space complexity. Here, we provide a second
version of our new sort where we have removed the auxiliary array. This second
improved version of the algorithm, which we call K-sort, is found to sort
elements faster than Heap sort for an appreciably large array size (n <=
70,00,000) for uniform U[0, 1] inputs.