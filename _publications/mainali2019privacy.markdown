---
layout: publication
title: Privacy-enhancing Context Authentication From Location-sensitive Data
authors: Pradip Mainali, Carlton Shepherd, Fabien A. P. Petitcolas
conference: Proceedings of the 14th International Conference on Availability, Reliability
  and Security
year: 2019
bibkey: mainali2019privacy
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.08800'}]
tags: [Hashing Methods, Locality Sensitive Hashing]
short_authors: Pradip Mainali, Carlton Shepherd, Fabien A. P. Petitcolas
---
This paper proposes a new privacy-enhancing, context-aware user
authentication system, ConSec, which uses a transformation of general
location-sensitive data, such as GPS location, barometric altitude and noise
levels, collected from the user's device, into a representation based on
locality-sensitive hashing (LSH). The resulting hashes provide a dimensionality
reduction of the underlying data, which we leverage to model users' behaviour
for authentication using machine learning. We present how ConSec supports
learning from categorical and numerical data, while addressing a number of
on-device and network-based threats. ConSec is implemented subsequently for the
Android platform and evaluated using data collected from 35 users, which is
followed by a security and privacy analysis. We demonstrate that LSH presents a
useful approach for context authentication from location-sensitive data without
directly utilising plain measurements.