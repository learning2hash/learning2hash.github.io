---
layout: publication
title: 'Killing Two Birds With One Stone: Can An Audio Captioning System Also Be Used
  For Audio-text Retrieval?'
authors: "Etienne Labb\xE9, Thomas Pellegrini, Julien Pinquier"
conference: DCASE2023 Sep 2023 Tampere Finland
year: 2023
bibkey: "labb\xE92023killing"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.15090'}]
tags: [Text Retrieval, Evaluation, Datasets]
short_authors: "Etienne Labb\xE9, Thomas Pellegrini, Julien Pinquier"
---
Automated Audio Captioning (AAC) aims to develop systems capable of
describing an audio recording using a textual sentence. In contrast, Audio-Text
Retrieval (ATR) systems seek to find the best matching audio recording(s) for a
given textual query (Text-to-Audio) or vice versa (Audio-to-Text). These tasks
require different types of systems: AAC employs a sequence-to-sequence model,
while ATR utilizes a ranking model that compares audio and text representations
within a shared projection subspace. However, this work investigates the
relationship between AAC and ATR by exploring the ATR capabilities of an
unmodified AAC system, without fine-tuning for the new task. Our AAC system
consists of an audio encoder (ConvNeXt-Tiny) trained on AudioSet for audio
tagging, and a transformer decoder responsible for generating sentences. For
AAC, it achieves a high SPIDEr-FL score of 0.298 on Clotho and 0.472 on
AudioCaps on average. For ATR, we propose using the standard Cross-Entropy loss
values obtained for any audio/caption pair. Experimental results on the Clotho
and AudioCaps datasets demonstrate decent recall values using this simple
approach. For instance, we obtained a Text-to-Audio R@1 value of 0.382 for
Au-dioCaps, which is above the current state-of-the-art method without external
data. Interestingly, we observe that normalizing the loss values was necessary
for Audio-to-Text retrieval.