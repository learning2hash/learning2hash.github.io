---
layout: publication
title: 'STALP: Style Transfer With Auxiliary Limited Pairing'
authors: "David Futschik, Michal Ku\u010Dera, Michal Luk\xE1\u010D, Zhaowen Wang,\
  \ Eli Shechtman, Daniel S\xFDkora"
conference: Computer Graphics Forum
year: 2021
bibkey: futschik2021stalp
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.10501'}]
tags: []
short_authors: Futschik et al.
---
We present an approach to example-based stylization of images that uses a
single pair of a source image and its stylized counterpart. We demonstrate how
to train an image translation network that can perform real-time semantically
meaningful style transfer to a set of target images with similar content as the
source image. A key added value of our approach is that it considers also
consistency of target images during training. Although those have no stylized
counterparts, we constrain the translation to keep the statistics of neural
responses compatible with those extracted from the stylized source. In contrast
to concurrent techniques that use a similar input, our approach better
preserves important visual characteristics of the source style and can deliver
temporally stable results without the need to explicitly handle temporal
consistency. We demonstrate its practical utility on various applications
including video stylization, style transfer to panoramas, faces, and 3D models.