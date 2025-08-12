---
layout: publication
title: A Fair And Memory/time-efficient Hashmap
authors: Abolfazl Asudeh, Nima Shahbazi, Stavros Sintos
conference: SIGMOD 2024
year: 2023
bibkey: asudeh2023fair
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.11355'}]
tags: ["Efficiency"]
short_authors: Abolfazl Asudeh, Nima Shahbazi, Stavros Sintos
---
Hashmap is a fundamental data structure in computer science. There has been
extensive research on constructing hashmaps that minimize the number of
collisions leading to efficient lookup query time. Recently, the data-dependant
approaches, construct hashmaps tailored for a target data distribution that
guarantee to uniformly distribute data across different buckets and hence
minimize the collisions. Still, to the best of our knowledge, none of the
existing technique guarantees group fairness among different groups of items
stored in the hashmap.
  Therefore, in this paper, we introduce FairHash, a data-dependant hashmap
that guarantees uniform distribution at the group-level across hash buckets,
and hence, satisfies the statistical parity notion of group fairness. We
formally define, three notions of fairness and, unlike existing work, FairHash
satisfies all three of them simultaneously. We propose three families of
algorithms to design fair hashmaps, suitable for different settings. Our
ranking-based algorithms reduce the unfairness of data-dependant hashmaps
without any memory-overhead. The cut-based algorithms guarantee zero-unfairness
in all cases, irrespective of how the data is distributed, but those introduce
an extra memory-overhead. Last but not least, the discrepancy-based algorithms
enable trading off between various fairness notions. In addition to the
theoretical analysis, we perform extensive experiments to evaluate the
efficiency and efficacy of our algorithms on real datasets. Our results verify
the superiority of FairHash compared to the other baselines on fairness at
almost no performance cost.