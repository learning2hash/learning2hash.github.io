---
layout: publication
title: 'Stegguard: Fingerprinting Self-supervised Pre-trained Encoders Via Secrets
  Embeder And Extractor'
authors: Xingdong Ren, Tianxing Zhang, Hanzhou Wu, Xinpeng Zhang, Yinggui Wang, Guangling
  Sun
conference: Arxiv
year: 2023
bibkey: ren2023stegguard
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.03380'}]
tags: ["Self-Supervised"]
short_authors: Ren et al.
---
In this work, we propose StegGuard, a novel fingerprinting mechanism to
verify the ownership of the suspect pre-trained encoder using steganography. A
critical perspective in StegGuard is that the unique characteristic of the
transformation from an image to an embedding, conducted by the pre-trained
encoder, can be equivalently exposed how an embeder embeds secrets into images
and how an extractor extracts the secrets from encoder's embeddings with a
tolerable error after the secrets are subjected to the encoder's
transformation. While each independent encoder has a distinct transformation,
the piracy encoder has a similar transformation to the victim. Based on these,
we learn a pair of secrets embeder and extractor as the fingerprint for the
victim encoder. We introduce a frequency-domain channel attention embedding
block into the embeder to adaptively embed secrets into suitable frequency
bands. During verification, if the secrets embedded into the query images can
be extracted with an acceptable error from the suspect encoder's embeddings,
the suspect encoder is determined as piracy, otherwise independent. Extensive
experiments demonstrate that depending on a very limited number of query
images, StegGuard can reliably identify across varied independent encoders, and
is robust against model stealing related attacks including model extraction,
fine-tuning, pruning, embedding noising and shuffle.