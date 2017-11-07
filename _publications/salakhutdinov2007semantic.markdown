---
layout: publication
title: "Semantic Hashing"
authors: R. Salakhutdinov, G. Hinton
conference: NIPS
year: 2007
bibkey: salakhutdinov2007semantic
additional_links:
   - {name: "PDF", url: "http://www.cs.utoronto.ca/~rsalakhu/papers/semantic_final.pdf"}
   - {name: "Code", url: "https://github.com/gynnash/AutoEncoder"}
---
We show how to learn a deep graphical model of the word-count
vectors obtained from a large set of documents. The values of the
latent variables in the deepest layer are easy to infer and give a
much better representation of each document than Latent Semantic
Analysis. When the deepest layer is forced to use a small number of
binary variables (e.g. 32), the graphical model performs “semantic
hashing”: Documents are mapped to memory addresses in such a
way that semantically similar documents are located at nearby addresses.
Documents similar to a query document can then be found
by simply accessing all the addresses that differ by only a few bits
from the address of the query document. This way of extending the
efficiency of hash-coding to approximate matching is much faster
than locality sensitive hashing, which is the fastest current method.
By using semantic hashing to filter the documents given to TF-IDF,
we achieve higher accuracy than applying TF-IDF to the entire document
set.
