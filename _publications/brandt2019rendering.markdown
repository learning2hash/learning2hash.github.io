---
layout: publication
title: Rendering Of Complex Heterogenous Scenes Using Progressive Blue Surfels
authors: "Sascha Brandt, Claudius J\xE4hn, Matthias Fischer, Friedhelm Meyer Auf Der\
  \ Heide"
conference: Arxiv
year: 2019
bibkey: brandt2019rendering
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.08225'}]
tags: ["Efficiency"]
short_authors: Brandt et al.
---
We present a technique for rendering highly complex 3D scenes in real-time by
generating uniformly distributed points on the scene's visible surfaces. The
technique is applicable to a wide range of scene types, like scenes directly
based on complex and detailed CAD data consisting of billions of polygons (in
contrast to scenes handcrafted solely for visualization). This allows to
visualize such scenes smoothly even in VR on a HMD with good image quality,
while maintaining the necessary frame-rates. In contrast to other point based
rendering methods, we place points in an approximated blue noise distribution
only on visible surfaces and store them in a highly GPU efficient data
structure, allowing to progressively refine the number of rendered points to
maximize the image quality for a given target frame rate. Our evaluation shows
that scenes consisting of a high amount of polygons can be rendered with
interactive frame rates with good visual quality on standard hardware.