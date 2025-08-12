---
layout: publication
title: 'Improved Esp-index: A Practical Self-index For Highly Repetitive Texts'
authors: Yoshimasa Takabatake, Yasuo Tabei, Hiroshi Sakamoto
conference: Lecture Notes in Computer Science
year: 2014
bibkey: takabatake2014improved
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1404.4972'}]
tags: []
short_authors: Yoshimasa Takabatake, Yasuo Tabei, Hiroshi Sakamoto
---
While several self-indexes for highly repetitive texts exist, developing a
practical self-index applicable to real world repetitive texts remains a
challenge. ESP-index is a grammar-based self-index on the notion of
edit-sensitive parsing (ESP), an efficient parsing algorithm that guarantees
upper bounds of parsing discrepancies between different appearances of the same
subtexts in a text. Although ESP-index performs efficient top-down searches of
query texts, it has a serious issue on binary searches for finding appearances
of variables for a query text, which resulted in slowing down the query
searches. We present an improved ESP-index (ESP-index-I) by leveraging the idea
behind succinct data structures for large alphabets. While ESP-index-I keeps
the same types of efficiencies as ESP-index about the top-down searches, it
avoid the binary searches using fast rank/select operations. We experimentally
test ESP-index-I on the ability to search query texts and extract subtexts from
real world repetitive texts on a large-scale, and we show that ESP-index-I
performs better that other possible approaches.