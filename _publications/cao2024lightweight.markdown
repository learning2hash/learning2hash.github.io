---
layout: publication
title: Lightweight Predictive 3D Gaussian Splats
authors: Junli Cao, Vidit Goel, Chaoyang Wang, Anil Kag, Ju Hu, Sergei Korolev, Chenfanfu
  Jiang, Sergey Tulyakov, Jian Ren
conference: Arxiv
year: 2024
bibkey: cao2024lightweight
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.19434'}]
tags: ["Efficiency", "Scalability"]
short_authors: Cao et al.
---
Recent approaches representing 3D objects and scenes using Gaussian splats
show increased rendering speed across a variety of platforms and devices. While
rendering such representations is indeed extremely efficient, storing and
transmitting them is often prohibitively expensive. To represent large-scale
scenes, one often needs to store millions of 3D Gaussians, occupying gigabytes
of disk space. This poses a very practical limitation, prohibiting widespread
adoption.Several solutions have been proposed to strike a balance between disk
size and rendering quality, noticeably reducing the visual quality. In this
work, we propose a new representation that dramatically reduces the hard drive
footprint while featuring similar or improved quality when compared to the
standard 3D Gaussian splats. When compared to other compact solutions, ours
offers higher quality renderings with significantly reduced storage, being able
to efficiently run on a mobile device in real-time. Our key observation is that
nearby points in the scene can share similar representations. Hence, only a
small ratio of 3D points needs to be stored. We introduce an approach to
identify such points which are called parent points. The discarded points
called children points along with attributes can be efficiently predicted by
tiny MLPs.