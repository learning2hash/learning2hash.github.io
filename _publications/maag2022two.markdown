---
layout: publication
title: Two Video Data Sets For Tracking And Retrieval Of Out Of Distribution Objects
authors: Kira Maag, Robin Chan, Svenja Uhlemeyer, Kamil Kowol, Hanno Gottschalk
conference: Lecture Notes in Computer Science
year: 2023
bibkey: maag2022two
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.02074'}]
tags: ["Datasets", "Video Retrieval"]
short_authors: Maag et al.
---
In this work we present two video test data sets for the novel computer
vision (CV) task of out of distribution tracking (OOD tracking). Here, OOD
objects are understood as objects with a semantic class outside the semantic
space of an underlying image segmentation algorithm, or an instance within the
semantic space which however looks decisively different from the instances
contained in the training data. OOD objects occurring on video sequences should
be detected on single frames as early as possible and tracked over their time
of appearance as long as possible. During the time of appearance, they should
be segmented as precisely as possible. We present the SOS data set containing
20 video sequences of street scenes and more than 1000 labeled frames with up
to two OOD objects. We furthermore publish the synthetic CARLA-WildLife data
set that consists of 26 video sequences containing up to four OOD objects on a
single frame. We propose metrics to measure the success of OOD tracking and
develop a baseline algorithm that efficiently tracks the OOD objects. As an
application that benefits from OOD tracking, we retrieve OOD sequences from
unlabeled videos of street scenes containing OOD objects.