---
layout: publication
title: 'Fuzzy Substring Matching: On-device Fuzzy Friend Search At Snapchat'
authors: Vasyl Pihur, Scott Thompson
conference: Arxiv
year: 2022
bibkey: pihur2022fuzzy
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.02767'}]
tags: ["Similarity Search"]
short_authors: Vasyl Pihur, Scott Thompson
---
About 50% of all queries on Snapchat app are targeted at finding the right
friend to interact with. Since everyone has a unique list of friends and that
list is not very large (maximum a few thousand), it makes sense to perform this
search locally, on users' devices. In addition, the friend list is already
available for other purposes, such as showing the chat feed, and the latency
savings can be significant by avoiding a server round-trip call. Historically,
we resorted to substring matching, ranking prefix matches at the top of the
result list. Introducing the ability to perform fuzzy search on a
resource-constrained device and in the environment where typo's are prevalent
is both prudent and challenging. In this paper, we describe our efficient and
accurate two-step approach to fuzzy search, characterized by a skip-bigram
retrieval layer and a novel local Levenshtein distance computation used for
final ranking.