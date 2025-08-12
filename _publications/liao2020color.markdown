---
layout: publication
title: Color-complexity Enabled Exhaustive Color-dots Identification And Spatial Patterns
  Testing In Images
authors: Shuting Liao, Li-yu Liu, Ting-an Chen, Kuang-yu Chen, Fushing Hsieh
conference: PLOS ONE
year: 2021
bibkey: liao2020color
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.14485'}]
tags: ["Evaluation"]
short_authors: Liao et al.
---
Targeted color-dots with varying shapes and sizes in images are first
exhaustively identified, and then their multiscale 2D geometric patterns are
extracted for testing spatial uniformness in a progressive fashion. Based on
color theory in physics, we develop a new color-identification algorithm
relying on highly associative relations among the three color-coordinates: RGB
or HSV. Such high associations critically imply low color-complexity of a color
image, and renders potentials of exhaustive identification of targeted
color-dots of all shapes and sizes. Via heterogeneous shaded regions and
lighting conditions, our algorithm is shown being robust, practical and
efficient comparing with the popular Contour and OpenCV approaches. Upon all
identified color-pixels, we form color-dots as individually connected networks
with shapes and sizes. We construct minimum spanning trees (MST) as spatial
geometries of dot-collectives of various size-scales. Given a size-scale, the
distribution of distances between immediate neighbors in the observed MST is
extracted, so do many simulated MSTs under the spatial uniformness assumption.
We devise a new algorithm for testing 2D spatial uniformness based on a
Hierarchical clustering tree upon all involving MSTs. Our developments are
illustrated on images obtained by mimicking chemical spraying via drone in
Precision Agriculture.