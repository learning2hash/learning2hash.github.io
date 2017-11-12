---
layout: publication
title: "Composite Hashing with Multiple Information Sources"
authors: D. Zhang, F. Wang, L. Si
conference: SIGIR
year: 2011
bibkey: zhang2011composite
additional_links:
   - {name: "PDF", url: "https://www.cs.purdue.edu/homes/lsi/SIGIR_2011B.pdf"}
---
Similarity search applications with a large amount of text
and image data demands an efficient and effective solution.
One useful strategy is to represent the examples in databases
as compact binary codes through semantic hashing, which
has attracted much attention due to its fast query/search
speed and drastically reduced storage requirement. All of
the current semantic hashing methods only deal with the
case when each example is represented by one type of features.
However, examples are often described from several
different information sources in many real world applications.
For example, the characteristics of a webpage can be
derived from both its content part and its associated links.
To address the problem of learning good hashing codes in
this scenario, we propose a novel research problem – Composite
Hashing with Multiple Information Sources (CHMIS).
The focus of the new research problem is to design an algorithm
for incorporating the features from different information
sources into the binary hashing codes efficiently and
effectively. In particular, we propose an algorithm CHMISAW
(CHMIS with Adjusted Weights) for learning the codes.
The proposed algorithm integrates information from several
different sources into the binary hashing codes by adjusting
the weights on each individual source for maximizing
the coding performance, and enables fast conversion from
query examples to their binary hashing codes. Experimental
results on five different datasets demonstrate the superior
performance of the proposed method against several other
state-of-the-art semantic hashing techniques.
