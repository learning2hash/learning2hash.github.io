---
layout: publication
title: Passage Summarization With Recurrent Models For Audio-sheet Music Retrieval
authors: Luis Carvalho, Gerhard Widmer
conference: Arxiv
year: 2023
bibkey: carvalho2023passage
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.12111'}]
tags: [Uncategorized]
short_authors: Luis Carvalho, Gerhard Widmer
---
Many applications of cross-modal music retrieval are related to connecting
sheet music images to audio recordings. A typical and recent approach to this
is to learn, via deep neural networks, a joint embedding space that correlates
short fixed-size snippets of audio and sheet music by means of an appropriate
similarity structure. However, two challenges that arise out of this strategy
are the requirement of strongly aligned data to train the networks, and the
inherent discrepancies of musical content between audio and sheet music
snippets caused by local and global tempo differences. In this paper, we
address these two shortcomings by designing a cross-modal recurrent network
that learns joint embeddings that can summarize longer passages of
corresponding audio and sheet music. The benefits of our method are that it
only requires weakly aligned audio-sheet music pairs, as well as that the
recurrent network handles the non-linearities caused by tempo variations
between audio and sheet music. We conduct a number of experiments on synthetic
and real piano data and scores, showing that our proposed recurrent method
leads to more accurate retrieval in all possible configurations.