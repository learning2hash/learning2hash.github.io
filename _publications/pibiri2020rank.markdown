---
layout: publication
title: Rank/select Queries Over Mutable Bitmaps
authors: Giulio Ermanno Pibiri, Shunsuke Kanda
conference: Information Systems
year: 2021
bibkey: pibiri2020rank
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.12809'}]
tags: []
short_authors: Giulio Ermanno Pibiri, Shunsuke Kanda
---
The problem of answering rank/select queries over a bitmap is of utmost
importance for many succinct data structures. When the bitmap does not change,
many solutions exist in the theoretical and practical side. In this work we
consider the case where one is allowed to modify the bitmap via a flip(i)
operation that toggles its i-th bit. By adapting and properly extending some
results concerning prefix-sum data structures, we present a practical solution
to the problem, tailored for modern CPU instruction sets. Compared to the
state-of-the-art, our solution improves runtime with no space degradation.
Moreover, it does not incur in a significant runtime penalty when compared to
the fastest immutable indexes, while providing even lower space overhead.