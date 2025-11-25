---
layout: publication
title: Unified Multimodal Interleaved Document Representation For Retrieval
authors: Jaewoo Lee, Joonho Ko, Jinheon Baek, Soyeong Jeong, Sung Ju Hwang
conference: Arxiv
year: 2024
bibkey: lee2024unified
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.02729'}]
tags: ["Multimodal Retrieval", "Re-Ranking"]
short_authors: Lee et al.
---
Information Retrieval (IR) methods aim to identify documents relevant to a
query, which have been widely applied in various natural language tasks.
However, existing approaches typically consider only the textual content within
documents, overlooking the fact that documents can contain multiple modalities,
including images and tables. Also, they often segment each long document into
multiple discrete passages for embedding, which prevents them from capturing
the overall document context and interactions between paragraphs. To address
these two challenges, we propose a method that holistically embeds documents
interleaved with multiple modalities by leveraging the capability of recent
vision-language models that enable the processing and integration of text,
images, and tables into a unified format and representation. Moreover, to
mitigate the information loss from segmenting documents into passages, instead
of representing and retrieving passages individually, we further merge the
representations of segmented passages into one single document representation,
while we additionally introduce a reranking strategy to decouple and identify
the relevant passage within the document if necessary. Then, through extensive
experiments on diverse IR scenarios considering both the textual and multimodal
queries, we show that our approach substantially outperforms relevant
baselines, thanks to the consideration of the multimodal information within
documents.