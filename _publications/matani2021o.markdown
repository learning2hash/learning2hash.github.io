---
layout: publication
title: An \(o(k \log{n})\) Algorithm For Prefix Based Ranked Autocomplete
authors: Dhruv Matani
conference: Arxiv
year: 2021
bibkey: matani2021o
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.15535'}]
tags: []
short_authors: Dhruv Matani
---
Many search engines such as Google, Bing & Yahoo! show search suggestions
when users enter search phrases on their interfaces. These suggestions are
meant to assist the user in finding what she wants quickly and also suggesting
common searches that may result in finding information that is more relevant.
It also serves the purpose of helping the user if she is not sure of what to
search for, but has a vague idea of what it is that she wants. We present an
algorithm that takes time proportional to \(O(k log\{n\})\), and \(O(n)\) extra
space for providing the user with the top \(k\) ranked suggestions out of a
corpus of \(n\) possible suggestions based on the prefix of the query that she
has entered so far.