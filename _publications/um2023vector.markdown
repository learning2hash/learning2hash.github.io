---
layout: publication
title: Vector Embeddings By Sequence Similarity And Context For Improved Compression,
  Similarity Search, Clustering, Organization, And Manipulation Of Cdna Libraries
authors: Daniel H. Um, David A. Knowles, Gail E. Kaiser
conference: Computational Biology and Chemistry
year: 2025
bibkey: um2023vector
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.05118'}]
tags: ["Evaluation", "Similarity Search"]
short_authors: Daniel H. Um, David A. Knowles, Gail E. Kaiser
---
This paper demonstrates the utility of organized numerical representations of
genes in research involving flat string gene formats (i.e., FASTA/FASTQ5).
FASTA/FASTQ files have several current limitations, such as their large file
sizes, slow processing speeds for mapping and alignment, and contextual
dependencies. These challenges significantly hinder investigations and tasks
that involve finding similar sequences. The solution lies in transforming
sequences into an alternative representation that facilitates easier clustering
into similar groups compared to the raw sequences themselves. By assigning a
unique vector embedding to each short sequence, it is possible to more
efficiently cluster and improve upon compression performance for the string
representations of cDNA libraries. Furthermore, through learning alternative
coordinate vector embeddings based on the contexts of codon triplets, we can
demonstrate clustering based on amino acid properties. Finally, using this
sequence embedding method to encode barcodes and cDNA sequences, we can improve
the time complexity of the similarity search by coupling vector embeddings with
an algorithm that determines the proximity of vectors in Euclidean space; this
allows us to perform sequence similarity searches in a quicker and more modular
fashion.