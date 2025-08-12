---
layout: publication
title: 'One-shot Doc Snippet Detection: Powering Search In Document Beyond Text'
authors: Abhinav Java, Shripad Deshmukh, Milan Aggarwal, Surgan Jandial, Mausoom Sarkar,
  Balaji Krishnamurthy
conference: 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2023
bibkey: java2022one
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.06584'}]
tags: []
short_authors: Java et al.
---
Active consumption of digital documents has yielded scope for research in
various applications, including search. Traditionally, searching within a
document has been cast as a text matching problem ignoring the rich layout and
visual cues commonly present in structured documents, forms, etc. To that end,
we ask a mostly unexplored question: "Can we search for other similar snippets
present in a target document page given a single query instance of a document
snippet?". We propose MONOMER to solve this as a one-shot snippet detection
task. MONOMER fuses context from visual, textual, and spatial modalities of
snippets and documents to find query snippet in target documents. We conduct
extensive ablations and experiments showing MONOMER outperforms several
baselines from one-shot object detection (BHRL), template matching, and
document understanding (LayoutLMv3). Due to the scarcity of relevant data for
the task at hand, we train MONOMER on programmatically generated data having
many visually similar query snippets and target document pairs from two
datasets - Flamingo Forms and PubLayNet. We also do a human study to validate
the generated data.