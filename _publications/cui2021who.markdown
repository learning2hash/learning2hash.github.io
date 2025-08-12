---
layout: publication
title: Who's Waldo? Linking People Across Text And Images
authors: Claire Yuqing Cui, Apoorv Khandelwal, Yoav Artzi, Noah Snavely, Hadar Averbuch-Elor
conference: Arxiv
year: 2021
bibkey: cui2021who
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.07253'}]
tags: ["Datasets", "Evaluation"]
short_authors: Cui et al.
---
We present a task and benchmark dataset for person-centric visual grounding,
the problem of linking between people named in a caption and people pictured in
an image. In contrast to prior work in visual grounding, which is predominantly
object-based, our new task masks out the names of people in captions in order
to encourage methods trained on such image-caption pairs to focus on contextual
cues (such as rich interactions between multiple people), rather than learning
associations between names and appearances. To facilitate this task, we
introduce a new dataset, Who's Waldo, mined automatically from image-caption
data on Wikimedia Commons. We propose a Transformer-based method that
outperforms several strong baselines on this task, and are releasing our data
to the research community to spur work on contextual models that consider both
vision and language.