---
layout: publication
title: 'AMC: Attention Guided Multi-modal Correlation Learning For Image Search'
authors: Kan Chen, Trung Bui, Fang Chen, Zhaowen Wang, Ram Nevatia
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: chen2017amc
citations: 34
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.00763'}]
tags: ["CVPR", "Datasets", "Image Retrieval"]
short_authors: Chen et al.
---
Given a user's query, traditional image search systems rank images according
to its relevance to a single modality (e.g., image content or surrounding
text). Nowadays, an increasing number of images on the Internet are available
with associated meta data in rich modalities (e.g., titles, keywords, tags,
etc.), which can be exploited for better similarity measure with queries. In
this paper, we leverage visual and textual modalities for image search by
learning their correlation with input query. According to the intent of query,
attention mechanism can be introduced to adaptively balance the importance of
different modalities. We propose a novel Attention guided Multi-modal
Correlation (AMC) learning method which consists of a jointly learned hierarchy
of intra and inter-attention networks. Conditioned on query's intent,
intra-attention networks (i.e., visual intra-attention network and language
intra-attention network) attend on informative parts within each modality; a
multi-modal inter-attention network promotes the importance of the most
query-relevant modalities. In experiments, we evaluate AMC models on the search
logs from two real world image search engines and show a significant boost on
the ranking of user-clicked images in search results. Additionally, we extend
AMC models to caption ranking task on COCO dataset and achieve competitive
results compared with recent state-of-the-arts.