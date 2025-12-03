---
layout: publication
title: Real-time Community Detection In Large Social Networks On A Laptop
authors: Benjamin Paul Chamberlain, Josh Levy-Kramer, Clive Humby, Marc Peter Deisenroth
conference: Arxiv
year: 2016
bibkey: chamberlain2016real
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1601.03958'}]
tags: ["Efficiency", "Evaluation", "Hashing Methods", "Locality-Sensitive-Hashing", "Scalability"]
short_authors: Chamberlain et al.
---
For a broad range of research, governmental and commercial applications it is
important to understand the allegiances, communities and structure of key
players in society. One promising direction towards extracting this information
is to exploit the rich relational data in digital social networks (the social
graph). As social media data sets are very large, most approaches make use of
distributed computing systems for this purpose. Distributing graph processing
requires solving many difficult engineering problems, which has lead some
researchers to look at single-machine solutions that are faster and easier to
maintain. In this article, we present a single-machine real-time system for
large-scale graph processing that allows analysts to interactively explore
graph structures. The key idea is that the aggregate actions of large numbers
of users can be compressed into a data structure that encapsulates user
similarities while being robust to noise and queryable in real-time. We achieve
single machine real-time performance by compressing the neighbourhood of each
vertex using minhash signatures and facilitate rapid queries through Locality
Sensitive Hashing. These techniques reduce query times from hours using
industrial desktop machines operating on the full graph to milliseconds on
standard laptops. Our method allows exploration of strongly associated regions
(i.e. communities) of large graphs in real-time on a laptop. It has been
deployed in software that is actively used by social network analysts and
offers another channel for media owners to monetise their data, helping them to
continue to provide free services that are valued by billions of people
globally.