---
layout: publication
title: 'The B-skip-list: A Simpler Uniquely Represented Alternative To B-trees'
authors: Daniel Golovin
conference: Arxiv
year: 2010
bibkey: golovin2010b
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1005.0662'}]
tags: []
short_authors: Daniel Golovin
---
In previous work, the author introduced the B-treap, a uniquely represented
B-tree analogue, and proved strong performance guarantees for it. However, the
B-treap maintains complex invariants and is very complex to implement. In this
paper we introduce the B-skip-list, which has most of the guarantees of the
B-treap, but is vastly simpler and easier to implement. Like the B-treap, the
B-skip-list may be used to construct strongly history-independent index
structures and filesystems; such constructions reveal no information about the
historical sequence of operations that led to the current logical state. For
example, a uniquely represented filesystem would support the deletion of a file
in a way that, in a strong information-theoretic sense, provably removes all
evidence that the file ever existed. Like the B-tree, the B-skip-list has depth
O(log_B (n)) where B is the block transfer size of the external memory, uses
linear space with high probability, and supports efficient one-dimensional
range queries.