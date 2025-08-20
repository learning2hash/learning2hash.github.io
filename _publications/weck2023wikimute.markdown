---
layout: publication
title: 'Wikimute: A Web-sourced Dataset Of Semantic Descriptions For Music Audio'
authors: Benno Weck, Holger Kirchhoff, Peter Grosche, Xavier Serra
conference: Lecture Notes in Computer Science
year: 2024
bibkey: weck2023wikimute
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.09207'}]
tags: [Datasets, Multimodal Retrieval, Evaluation]
short_authors: Weck et al.
---
Multi-modal deep learning techniques for matching free-form text with music
have shown promising results in the field of Music Information Retrieval (MIR).
Prior work is often based on large proprietary data while publicly available
datasets are few and small in size. In this study, we present WikiMuTe, a new
and open dataset containing rich semantic descriptions of music. The data is
sourced from Wikipedia's rich catalogue of articles covering musical works.
Using a dedicated text-mining pipeline, we extract both long and short-form
descriptions covering a wide range of topics related to music content such as
genre, style, mood, instrumentation, and tempo. To show the use of this data,
we train a model that jointly learns text and audio representations and
performs cross-modal retrieval. The model is evaluated on two tasks: tag-based
music retrieval and music auto-tagging. The results show that while our
approach has state-of-the-art performance on multiple tasks, but still observe
a difference in performance depending on the data used for training.