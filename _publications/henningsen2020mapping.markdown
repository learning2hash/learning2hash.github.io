---
layout: publication
title: Mapping The Interplanetary Filesystem
authors: "Sebastian Henningsen, Martin Florian, Sebastian Rust, Bj\xF6rn Scheuermann"
conference: Proceedings of IFIP Networking 2020
year: 2020
bibkey: henningsen2020mapping
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.07747'}]
tags: []
short_authors: Henningsen et al.
---
The Interplanetary Filesystem (IPFS) is a distributed data storage service
frequently used by blockchain applications and for sharing content in a
censorship-resistant manner. Data is distributed within an open set of peers
using a Kademlia-based distributed hash table (DHT). In this paper, we study
the structure of the resulting overlay network, as it significantly influences
the robustness and performance of IPFS. We monitor and systematically crawl
IPFS' DHT towards mapping the IPFS overlay network. Our measurements found an
average of 44474 nodes at every given time. At least 52.19% of these reside
behind a NAT and are not reachable from the outside, suggesting that a large
share of the network is operated by private individuals on an as-needed basis.
Based on our measurements and our analysis of the IPFS code, we conclude that
the topology of the IPFS network is, in its current state, closer to an
unstructured overlay network than it is to a classical DHT. While such a
structure has benefits for robustness and the resistance against Sybil attacks,
it leaves room for improvement in terms of performance and query privacy.