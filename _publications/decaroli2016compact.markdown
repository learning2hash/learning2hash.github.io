---
layout: publication
title: A Compact Index For Order-preserving Pattern Matching
authors: Gianni Decaroli, Travis Gagie, Giovanni Manzini
conference: Arxiv
year: 2016
bibkey: decaroli2016compact
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1606.05724'}]
tags: ["Efficiency"]
short_authors: Gianni Decaroli, Travis Gagie, Giovanni Manzini
---
Order-preserving pattern matching was introduced recently but it has already
attracted much attention. Given a reference sequence and a pattern, we want to
locate all substrings of the reference sequence whose elements have the same
relative order as the pattern elements. For this problem we consider the
offline version in which we build an index for the reference sequence so that
subsequent searches can be completed very efficiently. We propose a
space-efficient index that works well in practice despite its lack of good
worst-case time bounds. Our solution is based on the new approach of
decomposing the indexed sequence into an order component, containing ordering
information, and a delta component, containing information on the absolute
values. Experiments show that this approach is viable, faster than the
available alternatives, and it is the first one offering simultaneously small
space usage and fast retrieval.