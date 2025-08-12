---
layout: publication
title: 'Jazznet: A Dataset Of Fundamental Piano Patterns For Music Audio Machine Learning
  Research'
authors: Tosiron Adegbija
conference: ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2023
bibkey: adegbija2023jazznet
citations: 2
additional_links: [{name: Code, url: 'https://github.com/tosiron/jazznet'}, {name: Paper,
    url: 'https://arxiv.org/abs/2302.08632'}]
tags: ["Datasets", "ICASSP"]
short_authors: Tosiron Adegbija
---
This paper introduces the jazznet Dataset, a dataset of fundamental jazz
piano music patterns for developing machine learning (ML) algorithms in music
information retrieval (MIR). The dataset contains 162520 labeled piano
patterns, including chords, arpeggios, scales, and chord progressions with
their inversions, resulting in more than 26k hours of audio and a total size of
95GB. The paper explains the dataset's composition, creation, and generation,
and presents an open-source Pattern Generator using a method called
Distance-Based Pattern Structures (DBPS), which allows researchers to easily
generate new piano patterns simply by defining the distances between pitches
within the musical patterns. We demonstrate that the dataset can help
researchers benchmark new models for challenging MIR tasks, using a
convolutional recurrent neural network (CRNN) and a deep convolutional neural
network. The dataset and code are available via:
https://github.com/tosiron/jazznet.