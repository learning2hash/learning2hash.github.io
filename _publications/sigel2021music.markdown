---
layout: publication
title: Music Sentiment Transfer
authors: Miles Sigel, Michael Zhou, Jiebo Luo
conference: Arxiv
year: 2021
bibkey: sigel2021music
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.05765'}]
tags: ["Datasets"]
short_authors: Miles Sigel, Michael Zhou, Jiebo Luo
---
Music sentiment transfer is a completely novel task. Sentiment transfer is a
natural evolution of the heavily-studied style transfer task, as sentiment
transfer is rooted in applying the sentiment of a source to be the new
sentiment for a target piece of media; yet compared to style transfer,
sentiment transfer has been only scantily studied on images. Music sentiment
transfer attempts to apply the high level objective of sentiment transfer to
the domain of music. We propose CycleGAN to bridge disparate domains. In order
to use the network, we choose to use symbolic, MIDI, data as the music format.
Through the use of a cycle consistency loss, we are able to create one-to-one
mappings that preserve the content and realism of the source data. Results and
literature suggest that the task of music sentiment transfer is more difficult
than image sentiment transfer because of the temporal characteristics of music
and lack of existing datasets.