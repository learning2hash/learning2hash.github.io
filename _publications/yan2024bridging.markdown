---
layout: publication
title: Bridging Language Gaps In Audio-text Retrieval
authors: Zhiyong Yan, Heinrich Dinkel, Yongqing Wang, Jizhong Liu, Junbo Zhang, Yujun
  Wang, Bin Wang
conference: Interspeech 2024
year: 2024
bibkey: yan2024bridging
citations: 1
additional_links: [{name: Code, url: 'https://github.com/zyyan4/ml-clap'}, {name: Paper,
    url: 'https://arxiv.org/abs/2406.07012'}]
tags: ["Datasets", "Evaluation", "Interspeech", "Text Retrieval"]
short_authors: Yan et al.
---
Audio-text retrieval is a challenging task, requiring the search for an audio
clip or a text caption within a database. The predominant focus of existing
research on English descriptions poses a limitation on the applicability of
such models, given the abundance of non-English content in real-world data. To
address these linguistic disparities, we propose a language enhancement (LE),
using a multilingual text encoder (SONAR) to encode the text data with
language-specific information. Additionally, we optimize the audio encoder
through the application of consistent ensemble distillation (CED), enhancing
support for variable-length audio-text retrieval. Our methodology excels in
English audio-text retrieval, demonstrating state-of-the-art (SOTA) performance
on commonly used datasets such as AudioCaps and Clotho. Simultaneously, the
approach exhibits proficiency in retrieving content in seven other languages
with only 10% of additional language-enhanced training data, yielding promising
results. The source code is publicly available
https://github.com/zyyan4/ml-clap.