---
layout: publication
title: Learning Video Retrieval Models With Relevance-aware Online Mining
authors: Alex Falcon, Giuseppe Serra, Oswald Lanz
conference: Lecture Notes in Computer Science
year: 2022
bibkey: falcon2022learning
citations: 2
additional_links: [{name: Code, url: 'https://github.com/aranciokov/ranp.'}, {name: Paper,
    url: 'https://arxiv.org/abs/2203.08688'}]
tags: ["Datasets", "Evaluation", "Video Retrieval"]
short_authors: Alex Falcon, Giuseppe Serra, Oswald Lanz
---
Due to the amount of videos and related captions uploaded every hour, deep
learning-based solutions for cross-modal video retrieval are attracting more
and more attention. A typical approach consists in learning a joint text-video
embedding space, where the similarity of a video and its associated caption is
maximized, whereas a lower similarity is enforced with all the other captions,
called negatives. This approach assumes that only the video and caption pairs
in the dataset are valid, but different captions - positives - may also
describe its visual contents, hence some of them may be wrongly penalized. To
address this shortcoming, we propose the Relevance-Aware Negatives and
Positives mining (RANP) which, based on the semantics of the negatives,
improves their selection while also increasing the similarity of other valid
positives. We explore the influence of these techniques on two video-text
datasets: EPIC-Kitchens-100 and MSR-VTT. By using the proposed techniques, we
achieve considerable improvements in terms of nDCG and mAP, leading to
state-of-the-art results, e.g. +5.3% nDCG and +3.0% mAP on EPIC-Kitchens-100.
We share code and pretrained models at
https://github.com/aranciokov/ranp.