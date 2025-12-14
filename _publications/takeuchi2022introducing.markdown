---
layout: publication
title: Introducing Auxiliary Text Query-modifier To Content-based Audio Retrieval
authors: Daiki Takeuchi, Yasunori Ohishi, Daisuke Niizumi, Noboru Harada, Kunio Kashino
conference: Interspeech 2022
year: 2022
bibkey: takeuchi2022introducing
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.09732'}]
tags: [INTERSPEECH, Datasets, Audio Retrieval]
short_authors: Takeuchi et al.
---
The amount of audio data available on public websites is growing rapidly, and
an efficient mechanism for accessing the desired data is necessary. We propose
a content-based audio retrieval method that can retrieve a target audio that is
similar to but slightly different from the query audio by introducing auxiliary
textual information which describes the difference between the query and target
audio. While the range of conventional content-based audio retrieval is limited
to audio that is similar to the query audio, the proposed method can adjust the
retrieval range by adding an embedding of the auxiliary text query-modifier to
the embedding of the query sample audio in a shared latent space. To evaluate
our method, we built a dataset comprising two different audio clips and the
text that describes the difference. The experimental results show that the
proposed method retrieves the paired audio more accurately than the baseline.
We also confirmed based on visualization that the proposed method obtains the
shared latent space in which the audio difference and the corresponding text
are represented as similar embedding vectors.