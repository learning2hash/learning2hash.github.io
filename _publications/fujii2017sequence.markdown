---
layout: publication
title: Sequence-to-label Script Identification For Multilingual OCR
authors: Yasuhisa Fujii, Karel Driesen, Jonathan Baccash, Ash Hurst, Ashok C. Popat
conference: 2017 14th IAPR International Conference on Document Analysis and Recognition
  (ICDAR)
year: 2017
bibkey: fujii2017sequence
citations: 42
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.04671'}]
tags: []
short_authors: Fujii et al.
---
We describe a novel line-level script identification method. Previous work
repurposed an OCR model generating per-character script codes, counted to
obtain line-level script identification. This has two shortcomings. First, as a
sequence-to-sequence model it is more complex than necessary for the
sequence-to-label problem of line script identification. This makes it harder
to train and inefficient to run. Second, the counting heuristic may be
suboptimal compared to a learned model. Therefore we reframe line script
identification as a sequence-to-label problem and solve it using two
components, trained end-toend: Encoder and Summarizer. The encoder converts a
line image into a feature sequence. The summarizer aggregates the sequence to
classify the line. We test various summarizers with identical inception-style
convolutional networks as encoders. Experiments on scanned books and photos
containing 232 languages in 30 scripts show 16% reduction of script
identification error rate compared to the baseline. This improved script
identification reduces the character error rate attributable to script
misidentification by 33%.