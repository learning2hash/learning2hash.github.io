---
layout: publication
title: The Bitwise Hashing Trick For Personalized Search
authors: Braddock Gaskill
conference: Applied Artificial Intelligence
year: 2019
bibkey: gaskill2019the
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.08646'}]
tags: ["Evaluation", "Hashing Methods", "Large Scale Search", "Memory Efficiency", "Similarity Search"]
short_authors: Braddock Gaskill
---
Many real world problems require fast and efficient lexical comparison of
large numbers of short text strings. Search personalization is one such domain.
We introduce the use of feature bit vectors using the hashing trick for
improving relevance in personalized search and other personalization
applications. We present results of several lexical hashing and comparison
methods. These methods are applied to a user's historical behavior and are used
to predict future behavior. Using a single bit per dimension instead of
floating point results in an order of magnitude decrease in data structure
size, while preserving or even improving quality. We use real data to simulate
a search personalization task. A simple method for combining bit vectors
demonstrates an order of magnitude improvement in compute time on the task with
only a small decrease in accuracy.