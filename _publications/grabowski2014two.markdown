---
layout: publication
title: 'Two Simple Full-text Indexes Based On The Suffix Array'
authors: Szymon Grabowski, Marcin Raniszewski
conference: "Arxiv"
year: 2014
citations: 3
bibkey: grabowski2014two
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1405.5919'}
tags: ['Indexing and Efficiency', 'Quantization and Compression', 'Tools and Libraries']
---
We propose two suffix array inspired full-text indexes. One, called SA-hash,
augments the suffix array with a hash table to speed up pattern searches due to
significantly narrowed search interval before the binary search phase. The
other, called FBCSA, is a compact data structure, similar to M\{\"a\}kinen's
compact suffix array, but working on fixed sized blocks. Experiments on the
Pizza~\&~Chili 200\,MB datasets show that SA-hash is about 2--3 times faster in
pattern searches (counts) than the standard suffix array, for the price of
requiring \\(0.2n-1.1n\\) bytes of extra space, where \\(n\\) is the text length, and
setting a minimum pattern length. FBCSA is relatively fast in single cell
accesses (a few times faster than related indexes at about the same or better
compression), but not competitive if many consecutive cells are to be
extracted. Still, for the task of extracting, e.g., 10 successive cells its
time-space relation remains attractive.
