---
layout: publication
title: Efficient Online ML API Selection For Multi-label Classification Tasks
authors: Lingjiao Chen, Matei Zaharia, James Zou
conference: Arxiv
year: 2021
bibkey: chen2021efficient
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.09127'}]
tags: [Evaluation, Tools & Libraries, Efficiency]
short_authors: Lingjiao Chen, Matei Zaharia, James Zou
---
Multi-label classification tasks such as OCR and multi-object recognition are
a major focus of the growing machine learning as a service industry. While many
multi-label prediction APIs are available, it is challenging for users to
decide which API to use for their own data and budget, due to the heterogeneity
in those APIs' price and performance. Recent work shows how to select from
single-label prediction APIs. However the computation complexity of the
previous approach is exponential in the number of labels and hence is not
suitable for settings like OCR. In this work, we propose FrugalMCT, a
principled framework that adaptively selects the APIs to use for different data
in an online fashion while respecting user's budget. The API selection problem
is cast as an integer linear program, which we show has a special structure
that we leverage to develop an efficient online API selector with strong
performance guarantees. We conduct systematic experiments using ML APIs from
Google, Microsoft, Amazon, IBM, Tencent and other providers for tasks including
multi-label image classification, scene text recognition and named entity
recognition. Across diverse tasks, FrugalMCT can achieve over 90% cost
reduction while matching the accuracy of the best single API, or up to 8%
better accuracy while matching the best API's cost.