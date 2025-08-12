---
layout: publication
title: Utilizing Public Blockchains For The Sybil-resistant Bootstrapping Of Distributed
  Anonymity Services
authors: Roman Matzutt, Jan Pennekamp, Erik Buchholz, Klaus Wehrle
conference: Proceedings of the 15th ACM Asia Conference on Computer and Communications
  Security
year: 2020
bibkey: matzutt2020utilizing
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.06386'}]
tags: ["Privacy & Security"]
short_authors: Matzutt et al.
---
Distributed anonymity services, such as onion routing networks or
cryptocurrency tumblers, promise privacy protection without trusted third
parties. While the security of these services is often well-researched,
security implications of their required bootstrapping processes are usually
neglected: Users either jointly conduct the anonymization themselves, or they
need to rely on a set of non-colluding privacy peers. However, the typically
small number of privacy peers enable single adversaries to mimic distributed
services. We thus present AnonBoot, a Sybil-resistant medium to securely
bootstrap distributed anonymity services via public blockchains. AnonBoot
enforces that peers periodically create a small proof of work to refresh their
eligibility for providing secure anonymity services. A pseudo-random, locally
replicable bootstrapping process using on-chain entropy then prevents biasing
the election of eligible peers. Our evaluation using Bitcoin as AnonBoot's
underlying blockchain shows its feasibility to maintain a trustworthy
repository of 1000 peers with only a small storage footprint while supporting
arbitrarily large user bases on top of most blockchains.