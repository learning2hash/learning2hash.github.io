---
layout: publication
title: 'Feelsgoodman: Inferring Semantics Of Twitch Neologisms'
authors: Pavel Dolin, Luc D'Hauthuille, Andrea Vattani
conference: Arxiv
year: 2021
bibkey: dolin2021feelsgoodman
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.08411'}]
tags: []
short_authors: Pavel Dolin, Luc D'Hauthuille, Andrea Vattani
---
Twitch chats pose a unique problem in natural language understanding due to a
large presence of neologisms, specifically emotes. There are a total of 8.06
million emotes, over 400k of which were used in the week studied. There is
virtually no information on the meaning or sentiment of emotes, and with a
constant influx of new emotes and drift in their frequencies, it becomes
impossible to maintain an updated manually-labeled dataset. Our paper makes a
two fold contribution. First we establish a new baseline for sentiment analysis
on Twitch data, outperforming the previous supervised benchmark by 7.9% points.
Secondly, we introduce a simple but powerful unsupervised framework based on
word embeddings and k-NN to enrich existing models with out-of-vocabulary
knowledge. This framework allows us to auto-generate a pseudo-dictionary of
emotes and we show that we can nearly match the supervised benchmark above even
when injecting such emote knowledge into sentiment classifiers trained on
extraneous datasets such as movie reviews or Twitter.