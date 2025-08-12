---
layout: publication
title: 'Deepscribe: Localization And Classification Of Elamite Cuneiform Signs Via
  Deep Learning'
authors: Edward C. Williams, Grace Su, Sandra R. Schloen, Miller C. Prosser, Susanne
  Paulus, Sanjay Krishnan
conference: Arxiv
year: 2023
bibkey: williams2023deepscribe
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.01268'}]
tags: []
short_authors: Williams et al.
---
Twenty-five hundred years ago, the paperwork of the Achaemenid Empire was
recorded on clay tablets. In 1933, archaeologists from the University of
Chicago's Oriental Institute (OI) found tens of thousands of these tablets and
fragments during the excavation of Persepolis. Many of these tablets have been
painstakingly photographed and annotated by expert cuneiformists, and now
provide a rich dataset consisting of over 5,000 annotated tablet images and
100,000 cuneiform sign bounding boxes. We leverage this dataset to develop
DeepScribe, a modular computer vision pipeline capable of localizing cuneiform
signs and providing suggestions for the identity of each sign. We investigate
the difficulty of learning subtasks relevant to cuneiform tablet transcription
on ground-truth data, finding that a RetinaNet object detector can achieve a
localization mAP of 0.78 and a ResNet classifier can achieve a top-5 sign
classification accuracy of 0.89. The end-to-end pipeline achieves a top-5
classification accuracy of 0.80. As part of the classification module,
DeepScribe groups cuneiform signs into morphological clusters. We consider how
this automatic clustering approach differs from the organization of standard,
printed sign lists and what we may learn from it. These components, trained
individually, are sufficient to produce a system that can analyze photos of
cuneiform tablets from the Achaemenid period and provide useful transliteration
suggestions to researchers. We evaluate the model's end-to-end performance on
locating and classifying signs, providing a roadmap to a linguistically-aware
transliteration system, then consider the model's potential utility when
applied to other periods of cuneiform writing.