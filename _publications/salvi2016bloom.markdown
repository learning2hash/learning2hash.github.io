---
layout: publication
title: Bloom Filters and Compact Hash Codes for Efficient and Distributed Image Retrieval
authors: Salvi Andrea, Ercoli Simone, Bertini Marco, Del Bimbo Alberto
conference: "Arxiv"
year: 2016
bibkey: salvi2016bloom
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1605.00957"}
tags: ['ARXIV', 'CNN', 'Image Retrieval']
---
This paper presents a novel method for efficient image retrieval based on a simple and effective hashing of CNN features and the use of an indexing structure based on Bloom filters. These filters are used as gatekeepers for the database of image features allowing to avoid to perform a query if the query features are not stored in the database and speeding up the query process without affecting retrieval performance. Thanks to the limited memory requirements the system is suitable for mobile applications and distributed databases associating each filter to a distributed portion of the database. Experimental validation has been performed on three standard image retrieval datasets outperforming state-of-the-art hashing methods in terms of precision while the proposed indexing method obtains a 2times speedup.
