---
layout: publication
title: Two-stream Encoder-decoder Network For Localizing Image Forgeries
authors: Aniruddha Mazumdar, Prabin Kumar Bora
conference: Journal of Visual Communication and Image Representation
year: 2021
bibkey: mazumdar2020two
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.12881'}]
tags: []
short_authors: Aniruddha Mazumdar, Prabin Kumar Bora
---
This paper proposes a novel two-stream encoder-decoder network, which
utilizes both the high-level and the low-level image features for precisely
localizing forged regions in a manipulated image. This is motivated from the
fact that the forgery creation process generally introduces both the high-level
artefacts (e.g. unnatural contrast) and the low-level artefacts (e.g. noise
inconsistency) to the forged images. In the proposed two-stream network, one
stream learns the low-level manipulation-related features in the encoder side
by extracting noise residuals through a set of high-pass filters in the first
layer of the encoder network. In the second stream, the encoder learns the
high-level image manipulation features from the input image RGB values. The
coarse feature maps of both the encoders are upsampled by their corresponding
decoder network to produce dense feature maps. The dense feature maps of the
two streams are concatenated and fed to a final convolutional layer with
sigmoidal activation to produce pixel-wise prediction. We have carried out
experimental analysis on multiple standard forensics datasets to evaluate the
performance of the proposed method. The experimental results show the efficacy
of the proposed method with respect to the state-of-the-art.