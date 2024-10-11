---
layout: publication
title: Extracting Parallel Paragraphs From Common Crawl
authors: Kúdela Jakub, Holubová Irena, Bojar Ondřej
conference: "The Prague Bulletin of Mathematical Linguistics Volume"
year: 2018
bibkey: kúdela2018extracting
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1804.10413"}
tags: ['Graph']
---
Most of the current methods for mining parallel texts from the web assume that web pages of web sites share same structure across languages. We believe that there still exists a non-negligible amount of parallel data spread across sources not satisfying this assumption. We propose an approach based on a combination of bivec (a bilingual extension of word2vec) and locality-sensitive hashing which allows us to efficiently identify pairs of parallel segments located anywhere on pages of a given web domain, regardless their structure. We validate our method on realigning segments from a large parallel corpus. Another experiment with real-world data provided by Common Crawl Foundation confirms that our solution scales to hundreds of terabytes large set of web-crawled data.
