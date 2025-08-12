---
layout: publication
title: 'Spatialsense: An Adversarially Crowdsourced Benchmark For Spatial Relation
  Recognition'
authors: Kaiyu Yang, Olga Russakovsky, Jia Deng
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: yang2019spatialsense
citations: 25
additional_links: [{name: Code, url: 'https://github.com/princeton-vl/SpatialSense'},
  {name: Paper, url: 'https://arxiv.org/abs/1908.02660'}]
tags: ["ICCV"]
short_authors: Kaiyu Yang, Olga Russakovsky, Jia Deng
---
Understanding the spatial relations between objects in images is a
surprisingly challenging task. A chair may be "behind" a person even if it
appears to the left of the person in the image (depending on which way the
person is facing). Two students that appear close to each other in the image
may not in fact be "next to" each other if there is a third student between
them.
  We introduce SpatialSense, a dataset specializing in spatial relation
recognition which captures a broad spectrum of such challenges, allowing for
proper benchmarking of computer vision techniques. SpatialSense is constructed
through adversarial crowdsourcing, in which human annotators are tasked with
finding spatial relations that are difficult to predict using simple cues such
as 2D spatial configuration or language priors. Adversarial crowdsourcing
significantly reduces dataset bias and samples more interesting relations in
the long tail compared to existing datasets. On SpatialSense, state-of-the-art
recognition models perform comparably to simple baselines, suggesting that they
rely on straightforward cues instead of fully reasoning about this complex
task. The SpatialSense benchmark provides a path forward to advancing the
spatial reasoning capabilities of computer vision systems. The dataset and code
are available at https://github.com/princeton-vl/SpatialSense.