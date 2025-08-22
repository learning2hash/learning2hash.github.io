---
layout: publication
title: 'News Deja Vu: Connecting Past And Present With Semantic Search'
authors: Brevin Franklin, Emily Silcock, Abhishek Arora, Tom Bryan, Melissa Dell
conference: Proceedings of the Sixth Workshop on Natural Language Processing and Computational
  Social Science (NLP+CSS 2024)
year: 2024
bibkey: franklin2024news
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.15593'}]
tags: ["Datasets"]
short_authors: Franklin et al.
---
Social scientists and the general public often analyze contemporary events by
drawing parallels with the past, a process complicated by the vast, noisy, and
unstructured nature of historical texts. For example, hundreds of millions of
page scans from historical newspapers have been noisily transcribed.
Traditional sparse methods for searching for relevant material in these vast
corpora, e.g., with keywords, can be brittle given complex vocabularies and OCR
noise. This study introduces News Deja Vu, a novel semantic search tool that
leverages transformer large language models and a bi-encoder approach to
identify historical news articles that are most similar to modern news queries.
News Deja Vu first recognizes and masks entities, in order to focus on broader
parallels rather than the specific named entities being discussed. Then, a
contrastively trained, lightweight bi-encoder retrieves historical articles
that are most similar semantically to a modern query, illustrating how
phenomena that might seem unique to the present have varied historical
precedents. Aimed at social scientists, the user-friendly News Deja Vu package
is designed to be accessible for those who lack extensive familiarity with deep
learning. It works with large text datasets, and we show how it can be deployed
to a massive scale corpus of historical, open-source news articles. While human
expertise remains important for drawing deeper insights, News Deja Vu provides
a powerful tool for exploring parallels in how people have perceived past and
present.