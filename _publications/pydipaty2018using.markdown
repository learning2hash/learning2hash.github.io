---
layout: publication
title: On Using Non-volatile Memory In Apache Lucene
authors: Ramdoot Pydipaty, Amit Saha
conference: Arxiv
year: 2018
bibkey: pydipaty2018using
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.04343'}]
tags: []
short_authors: Ramdoot Pydipaty, Amit Saha
---
Apache Lucene is a widely popular information retrieval library used to
provide search functionality in an extremely wide variety of applications.
Naturally, it has to efficiently index and search large number of documents.
With non-volatile memory in DIMM form factor (NVDIMM), software now has access
to durable, byte-addressable memory with write latency within an order of
magnitude of DRAM write latency.
  In this preliminary article, we present the first reported work on the impact
of using NVDIMM on the performance of committing, searching, and near-real time
searching in Apache Lucene. We show modest improvements by using NVM but, our
empirical study suggests that bigger impact requires redesigning Lucene to
access NVM as byte-addressable memory using loads and stores, instead of
accessing NVM via the file system.