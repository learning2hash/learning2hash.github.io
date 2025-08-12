---
layout: publication
title: 'BIT-VO: Visual Odometry At 300 FPS Using Binary Features From The Focal Plane'
authors: Riku Murai, Sajad Saeedi, Paul H. J. Kelly
conference: 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems
  (IROS)
year: 2020
bibkey: murai2020bit
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.11186'}]
tags: ["IROS"]
short_authors: Riku Murai, Sajad Saeedi, Paul H. J. Kelly
---
Focal-plane Sensor-processor (FPSP) is a next-generation camera technology
which enables every pixel on the sensor chip to perform computation in
parallel, on the focal plane where the light intensity is captured. SCAMP-5 is
a general-purpose FPSP used in this work and it carries out computations in the
analog domain before analog to digital conversion. By extracting features from
the image on the focal plane, data which is digitized and transferred is
reduced. As a consequence, SCAMP-5 offers a high frame rate while maintaining
low energy consumption. Here, we present BIT-VO, which is, to the best of our
knowledge, the first 6 Degrees of Freedom visual odometry algorithm which
utilises the FPSP. Our entire system operates at 300 FPS in a natural scene,
using binary edges and corner features detected by the SCAMP-5.