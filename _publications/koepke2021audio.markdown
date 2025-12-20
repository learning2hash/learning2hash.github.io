---
layout: publication
title: 'Audio Retrieval With Natural Language Queries: A Benchmark Study'
authors: "A. Sophia Koepke, Andreea-Maria Oncescu, Jo\xE3o F. Henriques, Zeynep Akata,\
  \ Samuel Albanie"
conference: IEEE Transactions on Multimedia
year: 2021
bibkey: koepke2021audio
citations: 67
additional_links: [{name: Code, url: 'https://github.com/akoepke/audio-retrieval-benchmark'},
  {name: Paper, url: 'https://arxiv.org/abs/2112.09418'}]
tags: ["Audio Retrieval", "Datasets", "Evaluation", "Text Retrieval"]
short_authors: Koepke et al.
---
The objectives of this work are cross-modal text-audio and audio-text
retrieval, in which the goal is to retrieve the audio content from a pool of
candidates that best matches a given written description and vice versa.
Text-audio retrieval enables users to search large databases through an
intuitive interface: they simply issue free-form natural language descriptions
of the sound they would like to hear. To study the tasks of text-audio and
audio-text retrieval, which have received limited attention in the existing
literature, we introduce three challenging new benchmarks. We first construct
text-audio and audio-text retrieval benchmarks from the AudioCaps and Clotho
audio captioning datasets. Additionally, we introduce the SoundDescs benchmark,
which consists of paired audio and natural language descriptions for a diverse
collection of sounds that are complementary to those found in AudioCaps and
Clotho. We employ these three benchmarks to establish baselines for cross-modal
text-audio and audio-text retrieval, where we demonstrate the benefits of
pre-training on diverse audio tasks. We hope that our benchmarks will inspire
further research into audio retrieval with free-form text queries. Code, audio
features for all datasets used, and the SoundDescs dataset are publicly
available at https://github.com/akoepke/audio-retrieval-benchmark.