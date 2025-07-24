---
layout: publication
title: Secure Single-server Nearly-identical Image Deduplication
authors: Jonathan Takeshita, Ryan Karl, Taeho Jung
conference: 2020 29th International Conference on Computer Communications and Networks
  (ICCCN)
year: 2020
bibkey: takeshita2020secure
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.02330'}]
tags: ["Efficiency", "Hashing Methods", "ICCV", "Privacy & Security"]
short_authors: Jonathan Takeshita, Ryan Karl, Taeho Jung
---
Cloud computing is often utilized for file storage. Clients of cloud storage
services want to ensure the privacy of their data, and both clients and servers
want to use as little storage as possible. Cross-user deduplication is one
method to reduce the amount of storage a server uses. Deduplication and privacy
are naturally conflicting goals, especially for nearly-identical (``fuzzy'')
deduplication, as some information about the data must be used to perform
deduplication. Prior solutions thus utilize multiple servers, or only function
for exact deduplication. In this paper, we present a single-server protocol for
cross-user nearly-identical deduplication based on secure locality-sensitive
hashing (SLSH). We formally define our ideal security, and rigorously prove our
protocol secure against fully malicious, colluding adversaries with a proof by
simulation. We show experimentally that the individual parts of the protocol
are computationally feasible, and further discuss practical issues of security
and efficiency.