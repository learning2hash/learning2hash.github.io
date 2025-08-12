---
layout: publication
title: Shortest Unique Substring Query Revisited
authors: "Atalay Mert \u0130leri, M. O\u011Fuzhan K\xFClekci, Bojian Xu"
conference: Lecture Notes in Computer Science
year: 2014
bibkey: ileri2013shortest
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1312.2738'}]
tags: []
short_authors: "Atalay Mert \u0130leri, M. O\u011Fuzhan K\xFClekci, Bojian Xu"
---
We revisit the problem of finding shortest unique substring (SUS) proposed
recently by [6]. We propose an optimal \\(O(n)\\) time and space algorithm that can
find an SUS for every location of a string of size \\(n\\). Our algorithm
significantly improves the \\(O(n^2)\\) time complexity needed by [6]. We also
support finding all the SUSes covering every location, whereas the solution in
[6] can find only one SUS for every location. Further, our solution is simpler
and easier to implement and can also be more space efficient in practice, since
we only use the inverse suffix array and longest common prefix array of the
string, while the algorithm in [6] uses the suffix tree of the string and other
auxiliary data structures. Our theoretical results are validated by an
empirical study that shows our algorithm is much faster and more space-saving
than the one in [6].