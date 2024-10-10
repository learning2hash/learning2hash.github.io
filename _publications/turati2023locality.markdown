---
layout: publication
title: Locality-sensitive Hashing Does Not Guarantee Privacy! Attacks On Googles Floc And The Minhash Hierarchy System
authors: Turati Florian Eth Zurich, Cotrini Carlos Eth Zurich, Kubicek Karel Eth Zurich, Basin David Eth Zurich
conference: "Arxiv"
year: 2023
bibkey: turati2023locality
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2302.13635"}
tags: ['ARXIV', 'Graph', 'Independent']
---
Recently proposed systems aim at achieving privacy using locality-sensitive hashing. We show how these approaches fail by presenting attacks against two such systems Googles FLoC proposal for privacy-preserving targeted advertising and the MinHash Hierarchy a system for processing mobile users traffic behavior in a privacy-preserving way. Our attacks refute the pre-image resistance anonymity and privacy guarantees claimed for these systems. In the case of FLoC we show how to deanonymize users using Sybil attacks and to reconstruct 1037; or more of the browsing history for 3037; of its users using Generative Adversarial Networks. We achieve this only analyzing the hashes used by FLoC. For MinHash we precisely identify the movement of a subset of individuals and on average we can limit users movement to just 1037; of the possible geographic area again using just the hashes. In addition we refute their differential privacy claims.
