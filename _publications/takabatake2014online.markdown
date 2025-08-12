---
layout: publication
title: Online Pattern Matching For String Edit Distance With Moves
authors: Yoshimasa Takabatake, Yasuo Tabei, Hiroshi Sakamoto
conference: Lecture Notes in Computer Science
year: 2014
bibkey: takabatake2014online
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1408.0467'}]
tags: ["Efficiency"]
short_authors: Yoshimasa Takabatake, Yasuo Tabei, Hiroshi Sakamoto
---
Edit distance with moves (EDM) is a string-to-string distance measure that
includes substring moves in addition to ordinal editing operations to turn one
string to the other. Although optimizing EDM is intractable, it has many
applications especially in error detections. Edit sensitive parsing (ESP) is an
efficient parsing algorithm that guarantees an upper bound of parsing
discrepancies between different appearances of the same substrings in a string.
ESP can be used for computing an approximate EDM as the L1 distance between
characteristic vectors built by node labels in parsing trees. However, ESP is
not applicable to a streaming text data where a whole text is unknown in
advance. We present an online ESP (OESP) that enables an online pattern
matching for EDM. OESP builds a parse tree for a streaming text and computes
the L1 distance between characteristic vectors in an online manner. For the
space-efficient computation of EDM, OESP directly encodes the parse tree into a
succinct representation by leveraging the idea behind recent results of a
dynamic succinct tree. We experimentally test OESP on the ability to compute
EDM in an online manner on benchmark datasets, and we show OESP's efficiency.