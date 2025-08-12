---
layout: publication
title: 'U-index: A Universal Indexing Framework For Matching Long Patterns'
authors: Lorraine A. K. Ayad, Gabriele Fici, Ragnar Groot Koerkamp, Grigorios Loukides,
  Rob Patro, Giulio Ermanno Pibiri, Solon P. Pissis
conference: Arxiv
year: 2025
bibkey: ayad2025u
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.14488'}]
tags: []
short_authors: Ayad et al.
---
Text indexing is a fundamental and well-studied problem. Classic solutions either replace the original text with a compressed representation, e.g., the FM-index and its variants, or keep it uncompressed but attach some redundancy - an index - to accelerate matching. The former solutions thus retain excellent compressed space, but are slow in practice. The latter approaches, like the suffix array, instead sacrifice space for speed.
  We show that efficient text indexing can be achieved using just a small extra space on top of the original text, provided that the query patterns are sufficiently long. More specifically, we develop a new indexing paradigm in which a sketch of a query pattern is first matched against a sketch of the text. Once candidate matches are retrieved, they are verified using the original text. This paradigm is thus universal in the sense that it allows us to use any solution to index the sketched text, like a suffix array, FM-index, or r-index.
  We explore both the theory and the practice of this universal framework. With an extensive experimental analysis, we show that, surprisingly, universal indexes can be constructed much faster than their unsketched counterparts and take a fraction of the space, as a direct consequence of (i) having a lower bound on the length of patterns and (ii) working in sketch space. Furthermore, these data structures have the potential of retaining or even improving query time, because matching against the sketched text is faster and verifying candidates can be theoretically done in constant time per occurrence (or, in practice, by short and cache-friendly scans of the text). Finally, we discuss some important applications of this novel indexing paradigm to computational biology. We hypothesize that such indexes will be particularly effective when the queries are sufficiently long, and so demonstrate applications in long-read mapping.