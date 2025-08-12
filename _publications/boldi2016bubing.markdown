---
layout: publication
title: 'Bubing: Massive Crawling For The Masses'
authors: Paolo Boldi, Andrea Marino, Massimo Santini, Sebastiano Vigna
conference: Arxiv
year: 2016
bibkey: boldi2016bubing
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1601.06919'}]
tags: []
short_authors: Boldi et al.
---
Although web crawlers have been around for twenty years by now, there is
virtually no freely available, opensource crawling software that guarantees
high throughput, overcomes the limits of single-machine systems and at the same
time scales linearly with the amount of resources available. This paper aims at
filling this gap, through the description of BUbiNG, our next-generation web
crawler built upon the authors' experience with UbiCrawler [Boldi et al. 2004]
and on the last ten years of research on the topic. BUbiNG is an opensource
Java fully distributed crawler; a single BUbiNG agent, using sizeable hardware,
can crawl several thousands pages per second respecting strict politeness
constraints, both host- and IP-based. Unlike existing open-source distributed
crawlers that rely on batch techniques (like MapReduce), BUbiNG job
distribution is based on modern high-speed protocols so to achieve very high
throughput.