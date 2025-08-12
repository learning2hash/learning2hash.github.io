---
layout: publication
title: Partitioned Data Security On Outsourced Sensitive And Non-sensitive Data
authors: Sharad Mehrotra, Shantanu Sharma, Jeffrey D. Ullman, Anurag Mishra
conference: 2019 IEEE 35th International Conference on Data Engineering (ICDE)
year: 2019
bibkey: mehrotra2018partitioned
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.09233'}]
tags: []
short_authors: Mehrotra et al.
---
Despite extensive research on cryptography, secure and efficient query
processing over outsourced data remains an open challenge. This paper continues
along the emerging trend in secure data processing that recognizes that the
entire dataset may not be sensitive, and hence, non-sensitivity of data can be
exploited to overcome limitations of existing encryption-based approaches. We
propose a new secure approach, entitled query binning (QB) that allows
non-sensitive parts of the data to be outsourced in clear-text while
guaranteeing that no information is leaked by the joint processing of
non-sensitive data (in clear-text) and sensitive data (in encrypted form). QB
maps a query to a set of queries over the sensitive and non-sensitive data in a
way that no leakage will occur due to the joint processing over sensitive and
non-sensitive data. Interestingly, in addition to improve performance, we show
that QB actually strengthens the security of the underlying cryptographic
technique by preventing size, frequency-count, and workload-skew attacks.