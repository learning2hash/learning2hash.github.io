---
layout: publication
title: Multi-modal Video Chapter Generation
authors: Xiao Cao, Zitan Chen, Canyu Le, Lei Meng
conference: Arxiv
year: 2022
bibkey: cao2022multi
citations: 0
additional_links: [{name: Code, url: 'https://github.com/czt117/MVCG'}, {name: Paper,
    url: 'https://arxiv.org/abs/2209.12694'}]
tags: []
short_authors: Cao et al.
---
Chapter generation becomes practical technique for online videos nowadays.
The chapter breakpoints enable users to quickly find the parts they want and
get the summative annotations. However, there is no public method and dataset
for this task. To facilitate the research along this direction, we introduce a
new dataset called Chapter-Gen, which consists of approximately 10k
user-generated videos with annotated chapter information. Our data collection
procedure is fast, scalable and does not require any additional manual
annotation. On top of this dataset, we design an effective baseline specificlly
for video chapters generation task. which captures two aspects of a
video,including visual dynamics and narration text. It disentangles local and
global video features for localization and title generation respectively. To
parse the long video efficiently, a skip sliding window mechanism is designed
to localize potential chapters. And a cross attention multi-modal fusion module
is developed to aggregate local features for title generation. Our experiments
demonstrate that the proposed framework achieves superior results over existing
methods which illustrate that the method design for similar task cannot be
transfered directly even after fine-tuning. Code and dataset are available at
https://github.com/czt117/MVCG.