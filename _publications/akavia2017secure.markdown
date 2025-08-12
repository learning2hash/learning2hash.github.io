---
layout: publication
title: Secure Search On The Cloud Via Coresets And Sketches
authors: Adi Akavia, Dan Feldman, Hayim Shaul
conference: Arxiv
year: 2017
bibkey: akavia2017secure
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.05811'}]
tags: ["Efficiency"]
short_authors: Adi Akavia, Dan Feldman, Hayim Shaul
---
*Secure Search* is the problem of retrieving from a database table (or
any unsorted array) the records matching specified attributes, as in SQL SELECT
queries, but where the database and the query are encrypted. Secure search has
been the leading example for practical applications of Fully Homomorphic
Encryption (FHE) starting in Gentry's seminal work; however, to the best of our
knowledge all state-of-the-art secure search algorithms to date are realized by
a polynomial of degree \(Ω(m)\) for \(m\) the number of records, which is
typically too slow in practice even for moderate size \(m\).
  In this work we present the first algorithm for secure search that is
realized by a polynomial of degree polynomial in \(log m\). We implemented our
algorithm in an open source library based on HELib implementation for the
Brakerski-Gentry-Vaikuntanthan's FHE scheme, and ran experiments on Amazon's
EC2 cloud. Our experiments show that we can retrieve the first match in a
database of millions of entries in less than an hour using a single machine;
the time reduced almost linearly with the number of machines.
  Our result utilizes a new paradigm of employing coresets and sketches, which
are modern data summarization techniques common in computational geometry and
machine learning, for efficiency enhancement for homomorphic encryption. As a
central tool we design a novel sketch that returns the first positive entry in
a (not necessarily sparse) array; this sketch may be of independent interest.