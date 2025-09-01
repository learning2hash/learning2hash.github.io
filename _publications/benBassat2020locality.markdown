---
layout: publication
title: Locality-sensitive Hashing For Efficient Web Application Security Testing
authors: Ilan Ben-Bassat, Erez Rokah
conference: Proceedings of the 5th International Conference on Information Systems
  Security and Privacy
year: 2019
bibkey: benBassat2020locality
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.01128'}]
tags: ["Hashing Methods", "Locality-Sensitive-Hashing"]
short_authors: Ilan Ben-Bassat, Erez Rokah
---
Web application security has become a major concern in recent years, as more
and more content and services are available online. A useful method for
identifying security vulnerabilities is black-box testing, which relies on an
automated crawling of web applications. However, crawling Rich Internet
Applications (RIAs) is a very challenging task. One of the key obstacles
crawlers face is the state similarity problem: how to determine if two
client-side states are equivalent. As current methods do not completely solve
this problem, a successful scan of many real-world RIAs is still not possible.
We present a novel approach to detect redundant content for security testing
purposes. The algorithm applies locality-sensitive hashing using MinHash
sketches in order to analyze the Document Object Model (DOM) structure of web
pages, and to efficiently estimate similarity between them. Our experimental
results show that this approach allows a successful scan of RIAs that cannot be
crawled otherwise.