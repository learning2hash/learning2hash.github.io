---
layout: publication
title: 'Anchornet: A Weakly Supervised Network To Learn Geometry-sensitive Features
  For Semantic Matching'
authors: David Novotny, Diane Larlus, Andrea Vedaldi
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: novotny2017anchornet
citations: 59
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.04749'}]
tags: ["CVPR", "Supervised"]
short_authors: David Novotny, Diane Larlus, Andrea Vedaldi
---
Despite significant progress of deep learning in recent years,
state-of-the-art semantic matching methods still rely on legacy features such
as SIFT or HoG. We argue that the strong invariance properties that are key to
the success of recent deep architectures on the classification task make them
unfit for dense correspondence tasks, unless a large amount of supervision is
used. In this work, we propose a deep network, termed AnchorNet, that produces
image representations that are well-suited for semantic matching. It relies on
a set of filters whose response is geometrically consistent across different
object instances, even in the presence of strong intra-class, scale, or
viewpoint variations. Trained only with weak image-level labels, the final
representation successfully captures information about the object structure and
improves results of state-of-the-art semantic matching methods such as the
deformable spatial pyramid or the proposal flow methods. We show positive
results on the cross-instance matching task where different instances of the
same object category are matched as well as on a new cross-category semantic
matching task aligning pairs of instances each from a different object class.