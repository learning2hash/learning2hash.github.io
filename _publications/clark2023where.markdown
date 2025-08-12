---
layout: publication
title: 'Where We Are And What We''re Looking At: Query Based Worldwide Image Geo-localization
  Using Hierarchies And Scenes'
authors: Brandon Clark, Alec Kerrigan, Parth Parag Kulkarni, Vicente Vivanco Cepeda,
  Mubarak Shah
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: clark2023where
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.04249'}]
tags: ["CVPR"]
short_authors: Clark et al.
---
Determining the exact latitude and longitude that a photo was taken is a
useful and widely applicable task, yet it remains exceptionally difficult
despite the accelerated progress of other computer vision tasks. Most previous
approaches have opted to learn a single representation of query images, which
are then classified at different levels of geographic granularity. These
approaches fail to exploit the different visual cues that give context to
different hierarchies, such as the country, state, and city level. To this end,
we introduce an end-to-end transformer-based architecture that exploits the
relationship between different geographic levels (which we refer to as
hierarchies) and the corresponding visual scene information in an image through
hierarchical cross-attention. We achieve this by learning a query for each
geographic hierarchy and scene type. Furthermore, we learn a separate
representation for different environmental scenes, as different scenes in the
same location are often defined by completely different visual features. We
achieve state of the art street level accuracy on 4 standard geo-localization
datasets : Im2GPS, Im2GPS3k, YFCC4k, and YFCC26k, as well as qualitatively
demonstrate how our method learns different representations for different
visual hierarchies and scenes, which has not been demonstrated in the previous
methods. These previous testing datasets mostly consist of iconic landmarks or
images taken from social media, which makes them either a memorization task, or
biased towards certain places. To address this issue we introduce a much harder
testing dataset, Google-World-Streets-15k, comprised of images taken from
Google Streetview covering the whole planet and present state of the art
results. Our code will be made available in the camera-ready version.