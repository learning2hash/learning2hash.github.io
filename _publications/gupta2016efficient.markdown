---
layout: publication
title: Efficient Index Maintenance Under Dynamic Genome Modification
authors: Nitish Gupta, Komal Sanjeev, Tim Wall, Carl Kingsford, Rob Patro
conference: Arxiv
year: 2016
bibkey: gupta2016efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.03132'}]
tags: ["Scalability"]
short_authors: Gupta et al.
---
Efficient text indexing data structures have enabled large-scale genomic
sequence analysis and are used to help solve problems ranging from assembly to
read mapping. However, these data structures typically assume that the
underlying reference text is static and will not change over the course of the
queries being made. Some progress has been made in exploring how certain text
indices, like the suffix array, may be updated, rather than rebuilt from
scratch, when the underlying reference changes. Yet, these update operations
can be complex in practice, difficult to implement, and give fairly pessimistic
worst-case bounds. We present a novel data structure, SkipPatch, for
maintaining a k-mer-based index over a dynamically changing genome. SkipPatch
pairs a hash-based k-mer index with an indexable skip list that is used to
efficiently maintain the set of edits that have been applied to the original
genome. SkipPatch is practically fast, significantly outperforming the dynamic
extended suffix array in terms of update and query speed.