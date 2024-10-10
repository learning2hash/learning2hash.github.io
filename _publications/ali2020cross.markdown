---
layout: publication
title: Cross Hashing Anonymizing Encounters In Decentralised Contact Tracing Protocols
authors: Ali Junade, Dyo Vladimir
conference: "Arxiv"
year: 2020
bibkey: ali2020cross
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2005.12884"}
tags: ['ARXIV', 'Graph']
---
During the COVID-19 (SARS-CoV-2) epidemic Contact Tracing emerged as an essential tool for managing the epidemic. App-based solutions have emerged for Contact Tracing including a protocol designed by Apple and Google (influenced by an open-source protocol known as DP3T). This protocol contains two well-documented de-anonymisation attacks. Firstly that when someone is marked as having tested positive and their keys are made public they can be tracked over a large geographic area for 24 hours at a time. Secondly whilst the app requires a minimum exposure duration to register a contact there is no cryptographic guarantee for this property. This means an adversary can scan Bluetooth networks and retrospectively find who is infected. We propose a novel cross hashing approach to cryptographically guarantee minimum exposure durations. We further mitigate the 24-hour data exposure of infected individuals and reduce computational time for identifying if a user has been exposed using (k)-Anonymous buckets of hashes and Private Set Intersection. We empirically demonstrate that this modified protocol can offer like-for-like efficacy to the existing protocol.
