---
layout: publication
title: Detection Of Binary Square Fiducial Markers Using An Event Camera
authors: "Hamid Sarmadi, Rafael Mu\xF1oz-salinas, Miguel A. Olivares-mendez, Rafael\
  \ Medina-carnicer"
conference: IEEE Access
year: 2021
bibkey: sarmadi2020detection
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.06516'}]
tags: ["Efficiency", "Evaluation"]
short_authors: Sarmadi et al.
---
Event cameras are a new type of image sensors that output changes in light
intensity (events) instead of absolute intensity values. They have a very high
temporal resolution and a high dynamic range. In this paper, we propose a
method to detect and decode binary square markers using an event camera. We
detect the edges of the markers by detecting line segments in an image created
from events in the current packet. The line segments are combined to form
marker candidates. The bit value of marker cells is decoded using the events on
their borders. To the best of our knowledge, no other approach exists for
detecting square binary markers directly from an event camera using only the
CPU unit in real-time. Experimental results show that the performance of our
proposal is much superior to the one from the RGB ArUco marker detector. The
proposed method can achieve the real-time performance on a single CPU thread.