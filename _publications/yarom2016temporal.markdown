---
layout: publication
title: 'Temporal-needle: A View And Appearance Invariant Video Descriptor'
authors: Michal Yarom, Michal Irani
conference: Arxiv
year: 2016
bibkey: yarom2016temporal
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.04854'}]
tags: []
short_authors: Michal Yarom, Michal Irani
---
The ability to detect similar actions across videos can be very useful for
real-world applications in many fields. However, this task is still challenging
for existing systems, since videos that present the same action, can be taken
from significantly different viewing directions, performed by different actors
and backgrounds and under various video qualities. Video descriptors play a
significant role in these systems. In this work we propose the
"temporal-needle" descriptor which captures the dynamic behavior, while being
invariant to viewpoint and appearance. The descriptor is computed using multi
temporal scales of the video and by computing self-similarity for every patch
through time in every temporal scale. The descriptor is computed for every
pixel in the video. However, to find similar actions across videos, we consider
only a small subset of the descriptors - the statistical significant
descriptors. This allow us to find good correspondences across videos more
efficiently. Using the descriptor, we were able to detect the same behavior
across videos in a variety of scenarios. We demonstrate the use of the
descriptor in tasks such as temporal and spatial alignment, action detection
and even show its potential in unsupervised video clustering into categories.
In this work we handled only videos taken with stationary cameras, but the
descriptor can be extended to handle moving camera as well.