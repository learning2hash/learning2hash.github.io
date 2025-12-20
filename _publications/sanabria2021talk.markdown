---
layout: publication
title: 'Talk, Don''t Write: A Study Of Direct Speech-based Image Retrieval'
authors: Ramon Sanabria, Austin Waters, Jason Baldridge
conference: Interspeech 2021
year: 2021
bibkey: sanabria2021talk
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.01894'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Interspeech"]
short_authors: Ramon Sanabria, Austin Waters, Jason Baldridge
---
Speech-based image retrieval has been studied as a proxy for joint
representation learning, usually without emphasis on retrieval itself. As such,
it is unclear how well speech-based retrieval can work in practice -- both in
an absolute sense and versus alternative strategies that combine automatic
speech recognition (ASR) with strong text encoders. In this work, we
extensively study and expand choices of encoder architectures, training
methodology (including unimodal and multimodal pretraining), and other factors.
Our experiments cover different types of speech in three datasets: Flickr
Audio, Places Audio, and Localized Narratives. Our best model configuration
achieves large gains over state of the art, e.g., pushing recall-at-one from
21.8% to 33.2% for Flickr Audio and 27.6% to 53.4% for Places Audio. We also
show our best speech-based models can match or exceed cascaded ASR-to-text
encoding when speech is spontaneous, accented, or otherwise hard to
automatically transcribe.