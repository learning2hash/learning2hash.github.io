---
layout: publication
title: Secure K-nearest Neighbor Query Over Encrypted Data In Outsourced Environments
authors: Yousef Elmehdwi, Bharath K. Samanthula, Wei Jiang
conference: 2014 IEEE 30th International Conference on Data Engineering (ICDE)
year: 2013
bibkey: elmehdwi2013secure
citations: 281
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1307.4824'}]
tags: ["Efficiency"]
short_authors: Yousef Elmehdwi, Bharath K. Samanthula, Wei Jiang
---
For the past decade, query processing on relational data has been studied
extensively, and many theoretical and practical solutions to query processing
have been proposed under various scenarios. With the recent popularity of cloud
computing, users now have the opportunity to outsource their data as well as
the data management tasks to the cloud. However, due to the rise of various
privacy issues, sensitive data (e.g., medical records) need to be encrypted
before outsourcing to the cloud. In addition, query processing tasks should be
handled by the cloud; otherwise, there would be no point to outsource the data
at the first place. To process queries over encrypted data without the cloud
ever decrypting the data is a very challenging task. In this paper, we focus on
solving the k-nearest neighbor (kNN) query problem over encrypted database
outsourced to a cloud: a user issues an encrypted query record to the cloud,
and the cloud returns the k closest records to the user. We first present a
basic scheme and demonstrate that such a naive solution is not secure. To
provide better security, we propose a secure kNN protocol that protects the
confidentiality of the data, user's input query, and data access patterns.
Also, we empirically analyze the efficiency of our protocols through various
experiments. These results indicate that our secure protocol is very efficient
on the user end, and this lightweight scheme allows a user to use any mobile
device to perform the kNN query.