---
layout: publication
title: Hashing for Protein Structure Similarity Search
authors: Han Jin, Li Wu-jun
conference: Bioinformatics
year: 2004
bibkey: han2004hashing
citations: 50
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.08286'}]
tags: [Similarity Search, Hashing Methods]
---
Protein structure similarity search (PSSS), which tries to search proteins
with similar structures, plays a crucial role across diverse domains from drug
design to protein function prediction and molecular evolution. Traditional
alignment-based PSSS methods, which directly calculate alignment on the protein
structures, are highly time-consuming with high memory cost. Recently,
alignment-free methods, which represent protein structures as fixed-length
real-valued vectors, are proposed for PSSS. Although these methods have lower
time and memory cost than alignment-based methods, their time and memory cost
is still too high for large-scale PSSS, and their accuracy is unsatisfactory.
In this paper, we propose a novel method, called
\\(\underline\{\text\{p\}\}\\)r\\(\underline\{\text\{o\}\}\\)tein
\\(\underline\{\text\{s\}\}\\)tructure \\(\underline\{\text\{h\}\}\\)ashing (POSH), for PSSS.
POSH learns a binary vector representation for each protein structure, which
can dramatically reduce the time and memory cost for PSSS compared with
real-valued vector representation based methods. Furthermore, in POSH we also
propose expressive hand-crafted features and a structure encoder to well model
both node and edge interactions in proteins. Experimental results on real
datasets show that POSH can outperform other methods to achieve
state-of-the-art accuracy. Furthermore, POSH achieves a memory saving of more
than six times and speed improvement of more than four times, compared with
other methods.