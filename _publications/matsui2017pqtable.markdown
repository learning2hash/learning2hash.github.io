---
layout: publication
title: PQTable: Non-exhaustive Fast Search for Product-quantized Codes using Hash Tables
authors: Matsui Yusuke, Yamasaki Toshihiko, Aizawa Kiyoharu
conference: Arxiv
year: 2017
bibkey: matsui2017pqtable
additional_links:
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1704.06556"}
tags: ['Arxiv', 'Quantisation']
---
In this paper, we propose a product quantization table (PQTable); a fast search method for product-quantized codes via hash-tables. An identifier of each database vector is associated with the slot of a hash table by using its PQ-code as a key. For querying, an input vector is PQ-encoded and hashed, and the items associated with that code are then retrieved. The proposed PQTable produces the same results as a linear PQ scan, and is 10^2 to 10^5 times faster. Although state-of-the-art performance can be achieved by previous inverted-indexing-based approaches, such methods require manually-designed parameter setting and significant training; our PQTable is free of these limitations, and therefore offers a practical and effective solution for real-world problems. Specifically, when the vectors are highly compressed, our PQTable achieves one of the fastest search performances on a single CPU to date with significantly efficient memory usage (0.059 ms per query over 10^9 data points with just 5.5 GB memory consumption). Finally, we show that our proposed PQTable can naturally handle the codes of an optimized product quantization (OPQTable).
