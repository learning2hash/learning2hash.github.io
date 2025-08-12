---
layout: publication
title: 'Rice-marlin Codes: Tiny And Efficient Variable-to-fixed Codes'
authors: "Manuel Martinez, Joan Serra-sagrist\xE0"
conference: 2019 Data Compression Conference (DCC)
year: 2019
bibkey: martinez2018rice
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.05756'}]
tags: ["Efficiency"]
short_authors: "Manuel Martinez, Joan Serra-sagrist\xE0"
---
Marlin is a Variable-to-Fixed (VF) codec optimized for high decoding speed
through the use of small sized dictionaries that fit in the L1 cache of most
CPUs. While the size of Marlin dictionaries is adequate for decoding, they are
still too large to be encoded fast. We address this problem by proposing two
techniques to reduce the alphabet size. The first technique is to encode rare
symbols in their own segment, and the second is to combine Marlin dictionaries
with Rice encoding, hence our name Rice-Marlin for our new codec. Using those
techniques, we are able to reduce the size of Marlin dictionaries by a factor
of 16, not only enabling faster encoding speed, but also achieving better
compression efficiency.