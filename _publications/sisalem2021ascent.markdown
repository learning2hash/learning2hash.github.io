---
layout: publication
title: Ascent Similarity Caching With Approximate Indexes
authors: T. Si-Salem, G. Neglia, D. Carra
conference: Arxiv
year: 2021
bibkey: sisalem2021ascent
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.00957'}]
tags: ["Recommender Systems", "Similarity Search"]
short_authors: T. Si-Salem, G. Neglia, D. Carra
---
Similarity search is a key operation in multimedia retrieval systems and
recommender systems, and it will play an important role also for future machine
learning and augmented reality applications. When these systems need to serve
large objects with tight delay constraints, edge servers close to the end-user
can operate as similarity caches to speed up the retrieval. In this paper we
present A\c\{C\}AI, a new similarity caching policy which improves on the state
of the art by using (i) an (approximate) index for the whole catalog to decide
which objects to serve locally and which to retrieve from the remote server,
and (ii) a mirror ascent algorithm to update the set of local objects with
strong guarantees even when the request process does not exhibit any
statistical regularity.