---
layout: publication
title: 'Babylon: Reusing Bitcoin Mining To Enhance Proof-of-stake Security'
authors: Ertem Nusret Tas, David Tse, Fisher Yu, Sreeram Kannan
conference: Arxiv
year: 2022
bibkey: tas2022babylon
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.07946'}]
tags: ["Efficiency", "Privacy & Security", "Robustness"]
short_authors: Tas et al.
---
Bitcoin is the most secure blockchain in the world, supported by the immense
hash power of its Proof-of-Work miners, but consumes huge amount of energy.
Proof-of-Stake chains are energy-efficient, have fast finality and
accountability, but face several fundamental security issues: susceptibility to
non-slashable long-range safety attacks, non-slashable transaction censorship
and stalling attacks and difficulty to bootstrap new PoS chains from low token
valuation. We propose Babylon, a blockchain platform which combines the best of
both worlds by reusing the immense Bitcoin hash power to enhance the security
of PoS chains. Babylon provides a data-available timestamping service, securing
PoS chains by allowing them to timestamp data-available block checkpoints,
fraud proofs and censored transactions on Babylon. Babylon miners merge mine
with Bitcoin and thus the platform has zero additional energy cost. The
security of a Babylon-enhanced PoS protocol is formalized by a cryptoeconomic
security theorem which shows slashable safety and liveness guarantees.