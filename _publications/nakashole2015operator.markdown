---
layout: publication
title: An Operator For Entity Extraction In Mapreduce
authors: Ndapandula Nakashole
conference: Arxiv
year: 2015
bibkey: nakashole2015operator
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1512.04973'}]
tags: ["Datasets"]
short_authors: Ndapandula Nakashole
---
Dictionary-based entity extraction involves finding mentions of dictionary
entities in text. Text mentions are often noisy, containing spurious or missing
words. Efficient algorithms for detecting approximate entity mentions follow
one of two general techniques. The first approach is to build an index on the
entities and perform index lookups of document substrings. The second approach
recognizes that the number of substrings generated from documents can explode
to large numbers, to get around this, they use a filter to prune many such
substrings which do not match any dictionary entity and then only verify the
remaining substrings if they are entity mentions of dictionary entities, by
means of a text join. The choice between the index-based approach and the
filter & verification-based approach is a case-to-case decision as the best
approach depends on the characteristics of the input entity dictionary, for
example frequency of entity mentions. Choosing the right approach for the
setting can make a substantial difference in execution time. Making this choice
is however non-trivial as there are parameters within each of the approaches
that make the space of possible approaches very large. In this paper, we
present a cost-based operator for making the choice among execution plans for
entity extraction. Since we need to deal with large dictionaries and even
larger large datasets, our operator is developed for implementations of
MapReduce distributed algorithms.