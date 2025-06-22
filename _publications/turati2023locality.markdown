---
layout: publication
title: Locality-sensitive Hashing Does Not Guarantee Privacy! Attacks On Google's
  Floc And The Minhash Hierarchy System
authors: Florian Eth Zurich Turati, Carlos Eth Zurich Cotrini, Karel Eth Zurich Kubicek,
  David Eth Zurich Basin
conference: Arxiv
year: 2023
citations: 4
bibkey: turati2023locality
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.13635'}]
tags: [Privacy and Security, Hashing Methods]
---
Recently proposed systems aim at achieving privacy using locality-sensitive
hashing. We show how these approaches fail by presenting attacks against two
such systems: Google's FLoC proposal for privacy-preserving targeted
advertising and the MinHash Hierarchy, a system for processing mobile users'
traffic behavior in a privacy-preserving way. Our attacks refute the pre-image
resistance, anonymity, and privacy guarantees claimed for these systems.
  In the case of FLoC, we show how to deanonymize users using Sybil attacks and
to reconstruct 10% or more of the browsing history for 30% of its users using
Generative Adversarial Networks. We achieve this only analyzing the hashes used
by FLoC. For MinHash, we precisely identify the movement of a subset of
individuals and, on average, we can limit users' movement to just 10% of the
possible geographic area, again using just the hashes. In addition, we refute
their differential privacy claims.