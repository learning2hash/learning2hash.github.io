---
layout: publication
title: 'Scanrefer: 3D Object Localization In RGB-D Scans Using Natural Language'
authors: "Dave Zhenyu Chen, Angel X. Chang, Matthias Nie\xDFner"
conference: Lecture Notes in Computer Science
year: 2020
bibkey: chen2019scanrefer
citations: 168
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.08830'}]
tags: ["Datasets"]
short_authors: "Dave Zhenyu Chen, Angel X. Chang, Matthias Nie\xDFner"
---
We introduce the task of 3D object localization in RGB-D scans using natural
language descriptions. As input, we assume a point cloud of a scanned 3D scene
along with a free-form description of a specified target object. To address
this task, we propose ScanRefer, learning a fused descriptor from 3D object
proposals and encoded sentence embeddings. This fused descriptor correlates
language expressions with geometric features, enabling regression of the 3D
bounding box of a target object. We also introduce the ScanRefer dataset,
containing 51,583 descriptions of 11,046 objects from 800 ScanNet scenes.
ScanRefer is the first large-scale effort to perform object localization via
natural language expression directly in 3D.