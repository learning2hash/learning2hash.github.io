---
layout: publication
title: Top-down Attention Recurrent VLAD Encoding For Action Recognition In Videos
authors: Swathikiran Sudhakaran, Oswald Lanz
conference: Lecture Notes in Computer Science
year: 2018
bibkey: sudhakaran2018top
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.09892'}]
tags: ["Video Retrieval"]
short_authors: Swathikiran Sudhakaran, Oswald Lanz
---
Most recent approaches for action recognition from video leverage deep
architectures to encode the video clip into a fixed length representation
vector that is then used for classification. For this to be successful, the
network must be capable of suppressing irrelevant scene background and extract
the representation from the most discriminative part of the video. Our
contribution builds on the observation that spatio-temporal patterns
characterizing actions in videos are highly correlated with objects and their
location in the video. We propose Top-down Attention Action VLAD (TA-VLAD), a
deep recurrent architecture with built-in spatial attention that performs
temporally aggregated VLAD encoding for action recognition from videos. We
adopt a top-down approach of attention, by using class specific activation maps
obtained from a deep CNN pre-trained for image classification, to weight
appearance features before encoding them into a fixed-length video descriptor
using Gated Recurrent Units. Our method achieves state of the art recognition
accuracy on HMDB51 and UCF101 benchmarks.