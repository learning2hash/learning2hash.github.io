---
layout: publication
title: Emotion-guided Image To Music Generation
authors: Souraja Kundu, Saket Singh, Yuji Iwahori
conference: Arxiv
year: 2024
bibkey: kundu2024emotion
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.22299'}]
tags: []
short_authors: Souraja Kundu, Saket Singh, Yuji Iwahori
---
Generating music from images can enhance various applications, including
background music for photo slideshows, social media experiences, and video
creation. This paper presents an emotion-guided image-to-music generation
framework that leverages the Valence-Arousal (VA) emotional space to produce
music that aligns with the emotional tone of a given image. Unlike previous
models that rely on contrastive learning for emotional consistency, the
proposed approach directly integrates a VA loss function to enable accurate
emotional alignment. The model employs a CNN-Transformer architecture,
featuring pre-trained CNN image feature extractors and three Transformer
encoders to capture complex, high-level emotional features from MIDI music.
Three Transformer decoders refine these features to generate musically and
emotionally consistent MIDI sequences. Experimental results on a newly curated
emotionally paired image-MIDI dataset demonstrate the proposed model's superior
performance across metrics such as Polyphony Rate, Pitch Entropy, Groove
Consistency, and loss convergence.