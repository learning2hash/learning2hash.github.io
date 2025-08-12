---
layout: publication
title: Shape-biased Texture Agnostic Representations For Improved Textureless And
  Metallic Object Detection And 6D Pose Estimation
authors: "Peter H\xF6nig, Stefan Thalhammer, Jean-baptiste Weibel, Matthias Hirschmanner,\
  \ Markus Vincze"
conference: 2025 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2025
bibkey: "h\xF6nig2024shape"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.04878'}]
tags: []
short_authors: "H\xF6nig et al."
---
Recent advances in machine learning have greatly benefited object detection
and 6D pose estimation. However, textureless and metallic objects still pose a
significant challenge due to few visual cues and the texture bias of CNNs. To
address his issue, we propose a strategy for inducing a shape bias to CNN
training. In particular, by randomizing textures applied to object surfaces
during data rendering, we create training data without consistent textural
cues. This methodology allows for seamless integration into existing data
rendering engines, and results in negligible computational overhead for data
rendering and network training. Our findings demonstrate that the shape bias we
induce via randomized texturing, improves over existing approaches using style
transfer. We evaluate with three detectors and two pose estimators. For the
most recent object detector and for pose estimation in general, estimation
accuracy improves for textureless and metallic objects. Additionally we show
that our approach increases the pose estimation accuracy in the presence of
image noise and strong illumination changes. Code and datasets are publicly
available at github.com/hoenigpeter/randomized_texturing.