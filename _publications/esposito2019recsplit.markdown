---
layout: publication
title: Recsplit Minimal Perfect Hashing Via Recursive Splitting
authors: Esposito Emmanuel, Graf Thomas Mueller, Vigna Sebastiano
conference: "Arxiv"
year: 2019
bibkey: esposito2019recsplit
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1910.06416"}
tags: ['ARXIV', 'Independent']
---
A minimal perfect hash function bijectively maps a key set \{&#37; raw &#37;\}\\(S\\)\{&#37; endraw &#37;\} out of a universe \{&#37; raw &#37;\}\\(U\\)\{&#37; endraw &#37;\} into the first \{&#37; raw &#37;\}\\(|S|\\)\{&#37; endraw &#37;\} natural numbers. Minimal perfect hash functions are used, for example, to map irregularly-shaped keys, such as string, in a compact space so that metadata can then be simply stored in an array. While it is known that just \{&#37; raw &#37;\}\\(1.44\\)\{&#37; endraw &#37;\} bits per key are necessary to store a minimal perfect function, no published technique can go below \{&#37; raw &#37;\}\\(2\\)\{&#37; endraw &#37;\} bits per key in practice. We propose a new technique for storing minimal perfect hash functions with expected linear construction time and expected constant lookup time that makes it possible to build for the first time, for example, structures which need \{&#37; raw &#37;\}\\(1.56\\)\{&#37; endraw &#37;\} bits per key, that is, within \{&#37; raw &#37;\}\\(8.3\\)\{&#37; endraw &#37;\}&#37; of the lower bound, in less than \{&#37; raw &#37;\}\\(2\\)\{&#37; endraw &#37;\} ms per key. We show that instances of our construction are able to simultaneously beat the construction time, space usage and lookup time of the state-of-the-art data structure reaching \{&#37; raw &#37;\}\\(2\\)\{&#37; endraw &#37;\} bits per key. Moreover, we provide parameter choices giving structures which are competitive with alternative, larger-size data structures in terms of space and lookup time. The construction of our data structures can be easily parallelized or mapped on distributed computational units (e.g., within the MapReduce framework), and structures larger than the available RAM can be directly built in mass storage.
