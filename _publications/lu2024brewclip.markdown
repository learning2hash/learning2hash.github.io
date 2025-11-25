---
layout: publication
title: 'Brewclip: A Bifurcated Representation Learning Framework For Audio-visual
  Retrieval'
authors: Zhenyu Lu, Lakshay Sethi
conference: Arxiv
year: 2024
bibkey: lu2024brewclip
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.10383'}]
tags: ["Datasets", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Zhenyu Lu, Lakshay Sethi
---
Previous methods for audio-image matching generally fall into one of two
categories: pipeline models or End-to-End models. Pipeline models first
transcribe speech and then encode the resulting text; End-to-End models encode
speech directly. Generally, pipeline models outperform end-to-end models, but
the intermediate transcription necessarily discards some potentially useful
non-textual information. In addition to textual information, speech can convey
details such as accent, mood, and and emphasis, which should be effectively
captured in the encoded representation. In this paper, we investigate whether
non-textual information, which is overlooked by pipeline-based models, can be
leveraged to improve speech-image matching performance. We thoroughly analyze
and compare End-to-End models, pipeline models, and our proposed dual-channel
model for robust audio-image retrieval on a variety of datasets. Our approach
achieves a substantial performance gain over the previous state-of-the-art by
leveraging strong pretrained models, a prompting mechanism and a bifurcated
design.