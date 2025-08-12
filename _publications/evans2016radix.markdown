---
layout: publication
title: Radix Sort Trees In The Large
authors: Steven N. Evans, Anton Wakolbinger
conference: Electronic Communications in Probability
year: 2017
bibkey: evans2016radix
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.07385'}]
tags: ["Tree Based ANN"]
short_authors: Steven N. Evans, Anton Wakolbinger
---
The trie-based radix sort algorithm stores pairwise different infinite binary
strings in the leaves of a binary tree in a way that the Ulam-Harris coding of
each leaf equals a prefix (that is, an initial segment) of the corresponding
string, with the prefixes being of minimal length so that they are pairwise
different. We investigate the \{\em radix sort tree chains\} -- the tree-valued
Markov chains that arise when successively storing infinite binary strings
\\(Z_1,\ldots, Z_n\\), \\(n=1,2,\ldots\\) according to the trie-based radix sort
algorithm, where the source strings \\(Z_1, Z_2,\ldots\\) are independent and
identically distributed. We establish a bijective correspondence between the
full Doob--Martin boundary of the radix sort tree chain with a \{\em symmetric
Bernoulli source\} (that is, each \\(Z_k\\) is a fair coin-tossing sequence) and the
family of radix sort tree chains for which the common distribution of the \\(Z_k\\)
is a diffuse probability measure on \\(\\{0,1\\}^\infty\\). In essence, our result
characterizes all the ways that it is possible to condition such a chain of
radix sort trees consistently on its behavior "in the large".