---
layout: publication
title: Space-efficient Huffman Codes Revisited
authors: "Szymon Grabowski, Dominik K\xF6ppl"
conference: Information Processing Letters
year: 2022
bibkey: grabowski2021space
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.05495'}]
tags: ["Compact Codes", "Efficiency", "Memory Efficiency"]
short_authors: "Szymon Grabowski, Dominik K\xF6ppl"
---
Canonical Huffman code is an optimal prefix-free compression code whose
codewords enumerated in the lexicographical order form a list of binary words
in non-decreasing lengths. Gagie et al. (2015) gave a representation of this
coding capable to encode or decode a symbol in constant worst case time. It
uses \\(\sigma \lg \ell_\{\text\{max\}\} + o(\sigma) + O(\ell_\{\text\{max\}\}^2)\\) bits
of space, where \\(\sigma\\) and \\(\ell_\{\text\{max\}\}\\) are the alphabet size and
maximum codeword length, respectively. We refine their representation to reduce
the space complexity to \\(\sigma \lg \ell_\{\text\{max\}\} (1 + o(1))\\) bits while
preserving the constant encode and decode times. Our algorithmic idea can be
applied to any canonical code.