---
layout: publication
title: Hamming Distributions of Popular Perceptual Hashing Techniques
authors: Mckeown Sean, Buchanan William J
conference: 'Forensic Science International: Digital Investigation'
year: 2023
bibkey: mckeown2022hamming
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.08035'}]
tags: ["Hashing-Methods"]
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