---
layout: publication
title: Style Transfer With Adaptation To The Central Objects Of The Scene
authors: Alexey Schekalev, Victor Kitov
conference: Studies in Computational Intelligence
year: 2019
bibkey: schekalev2019style
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.01134'}]
tags: []
short_authors: Alexey Schekalev, Victor Kitov
---
Style transfer is a problem of rendering image with some content in the style
of another image, for example a family photo in the style of a painting of some
famous artist. The drawback of classical style transfer algorithm is that it
imposes style uniformly on all parts of the content image, which perturbs
central objects on the content image, such as faces or text, and makes them
unrecognizable. This work proposes a novel style transfer algorithm which
automatically detects central objects on the content image, generates spatial
importance mask and imposes style non-uniformly: central objects are stylized
less to preserve their recognizability and other parts of the image are
stylized as usual to preserve the style. Three methods of automatic central
object detection are proposed and evaluated qualitatively and via a user
evaluation study. Both comparisons demonstrate higher quality of stylization
compared to the classical style transfer method.