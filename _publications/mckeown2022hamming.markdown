---
layout: publication
title: Hamming Distributions Of Popular Perceptual Hashing Techniques
authors: Sean McKeown, William J Buchanan
conference: DFRWS (Digital Forensics Research Conference) EU 2023 21-24 March 2023
  Bonn Germany
year: 2022
bibkey: mckeown2022hamming
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.08035'}]
tags: ["Evaluation", "Hashing Methods", "Tools & Libraries"]
short_authors: Sean McKeown, William J Buchanan
---
Content-based file matching has been widely deployed for decades, largely for
the detection of sources of copyright infringement, extremist materials, and
abusive sexual media. Perceptual hashes, such as Microsoft's PhotoDNA, are one
automated mechanism for facilitating detection, allowing for machines to
approximately match visual features of an image or video in a robust manner.
However, there does not appear to be much public evaluation of such approaches,
particularly when it comes to how effective they are against content-preserving
modifications to media files. In this paper, we present a million-image scale
evaluation of several perceptual hashing archetypes for popular algorithms
(including Facebook's PDQ, Apple's Neuralhash, and the popular pHash library)
against seven image variants. The focal point is the distribution of Hamming
distance scores between both unrelated images and image variants to better
understand the problems faced by each approach.