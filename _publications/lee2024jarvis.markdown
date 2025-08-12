---
layout: publication
title: 'Jarvis: Detecting Actions In Video Using Unified Actor-scene Context Relation
  Modeling'
authors: Seok Hwan Lee, Taein Son, Soo Won Seo, Jisong Kim, Jun Won Choi
conference: Arxiv
year: 2024
bibkey: lee2024jarvis
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.03612'}]
tags: []
short_authors: Lee et al.
---
Video action detection (VAD) is a formidable vision task that involves the
localization and classification of actions within the spatial and temporal
dimensions of a video clip. Among the myriad VAD architectures, two-stage VAD
methods utilize a pre-trained person detector to extract the region of interest
features, subsequently employing these features for action detection. However,
the performance of two-stage VAD methods has been limited as they depend solely
on localized actor features to infer action semantics. In this study, we
propose a new two-stage VAD framework called Joint Actor-scene context Relation
modeling based on Visual Semantics (JARViS), which effectively consolidates
cross-modal action semantics distributed globally across spatial and temporal
dimensions using Transformer attention. JARViS employs a person detector to
produce densely sampled actor features from a keyframe. Concurrently, it uses a
video backbone to create spatio-temporal scene features from a video clip.
Finally, the fine-grained interactions between actors and scenes are modeled
through a Unified Action-Scene Context Transformer to directly output the final
set of actions in parallel. Our experimental results demonstrate that JARViS
outperforms existing methods by significant margins and achieves
state-of-the-art performance on three popular VAD datasets, including AVA,
UCF101-24, and JHMDB51-21.