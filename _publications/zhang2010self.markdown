---
layout: publication
title: "Self-Taught Hashing for Fast Similarity Search"
authors: D. Zhang, J. Wang, D. Cai, and J. Lu
conference: SIGIR
year: 2010
bibkey: zhang2010self
additional_links:
   - {name: "PDF", url: "http://www.dcs.bbk.ac.uk/~dell/publications/dellzhang_sigir2010.pdf"}
   - {name: "URL", url: "http://www.dcs.bbk.ac.uk/~dell/publications/dellzhang_sigir2010_suppl.html"}
   - {name: "Code", url: "http://www.dcs.bbk.ac.uk/~dell/publications/dellzhang_sigir2010/sth_v1.zip"}
   - {name: "Talk", url: "http://www.dcs.bbk.ac.uk/~dell/publications/dellzhang_sigir2010_slides.pdf"}
---
The ability of fast similarity search at large scale is of great
importance to many Information Retrieval (IR) applications.
A promising way to accelerate similarity search is semantic
hashing which designs compact binary codes for a large number
of documents so that semantically similar documents
are mapped to similar codes (within a short Hamming distance).
Although some recently proposed techniques are
able to generate high-quality codes for documents known
in advance, obtaining the codes for previously unseen documents
remains to be a very challenging problem. In this
paper, we emphasise this issue and propose a novel SelfTaught
Hashing (STH) approach to semantic hashing: we
first find the optimal l-bit binary codes for all documents in
the given corpus via unsupervised learning, and then train
l classifiers via supervised learning to predict the l-bit code
for any query document unseen before. Our experiments on
three real-world text datasets show that the proposed approach
using binarised Laplacian Eigenmap (LapEig) and
linear Support Vector Machine (SVM) outperforms stateof-the-art
techniques significantly.
