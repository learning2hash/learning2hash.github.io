---
layout: publication
title: Midi Miner -- A Python Library For Tonal Tension And Track Classification
authors: Rui Guo, Dorien Herremans, Thor Magnusson
conference: Arxiv
year: 2019
bibkey: guo2019midi
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.02049'}]
tags: ["Tools & Libraries"]
short_authors: Rui Guo, Dorien Herremans, Thor Magnusson
---
We present a Python library, called Midi Miner, that can calculate tonal
tension and classify different tracks. MIDI (Music Instrument Digital
Interface) is a hardware and software standard for communicating musical events
between digital music devices. It is often used for tasks such as music
representation, communication between devices, and even music generation [5].
Tension is an essential element of the music listening experience, which can
come from a number of musical features including timbre, loudness and harmony
[3]. Midi Miner provides a Python implementation for the tonal tension model
based on the spiral array [1] as presented by Herremans and Chew [4]. Midi
Miner also performs key estimation and includes a track classifier that can
disentangle melody, bass, and harmony tracks. Even though tracks are often
separated in MIDI files, the musical function of each track is not always
clear. The track classifier keeps the identified tracks and discards messy
tracks, which can enable further analysis and training tasks.