---
layout: publication
title: 'Andro-simnet: Android Malware Family Classification Using Social Network Analysis'
authors: Hye Min Kim, Hyun Min Song, Jae Woo Seo, Huy Kang Kim
conference: 2018 16th Annual Conference on Privacy, Security and Trust (PST)
year: 2018
bibkey: kim2018andro
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.09456'}]
tags: []
short_authors: Kim et al.
---
While the rapid adaptation of mobile devices changes our daily life more
conveniently, the threat derived from malware is also increased. There are lots
of research to detect malware to protect mobile devices, but most of them adopt
only signature-based malware detection method that can be easily bypassed by
polymorphic and metamorphic malware. To detect malware and its variants, it is
essential to adopt behavior-based detection for efficient malware
classification. This paper presents a system that classifies malware by using
common behavioral characteristics along with malware families. We measure the
similarity between malware families with carefully chosen features commonly
appeared in the same family. With the proposed similarity measure, we can
classify malware by malware's attack behavior pattern and tactical
characteristics. Also, we apply a community detection algorithm to increase the
modularity within each malware family network aggregation. To maintain high
classification accuracy, we propose a process to derive the optimal weights of
the selected features in the proposed similarity measure. During this process,
we find out which features are significant for representing the similarity
between malware samples. Finally, we provide an intuitive graph visualization
of malware samples which is helpful to understand the distribution and likeness
of the malware networks. In the experiment, the proposed system achieved 97%
accuracy for malware classification and 95% accuracy for prediction by K-fold
cross-validation using the real malware dataset.