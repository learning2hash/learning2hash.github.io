---
layout: publication
title: 'Scene Designer: A Unified Model For Scene Search And Synthesis From Sketch'
authors: Ribeiro et al.
conference: 2021 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW)
year: 2021
bibkey: ribeiro2021scene
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.07353'}]
tags: ["ICCV"]
---
Scene Designer is a novel method for searching and generating images using
free-hand sketches of scene compositions; i.e. drawings that describe both the
appearance and relative positions of objects. Our core contribution is a single
unified model to learn both a cross-modal search embedding for matching
sketched compositions to images, and an object embedding for layout synthesis.
We show that a graph neural network (GNN) followed by Transformer under our
novel contrastive learning setting is required to allow learning correlations
between object type, appearance and arrangement, driving a mask generation
module that synthesises coherent scene layouts, whilst also delivering state of
the art sketch based visual search of scenes.