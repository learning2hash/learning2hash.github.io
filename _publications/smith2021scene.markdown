---
layout: publication
title: Scene Retrieval For Contextual Visual Mapping
authors: William H. B. Smith, Michael Milford, Klaus D. McDonald-Maier, Shoaib Ehsan
conference: Arxiv
year: 2021
bibkey: smith2021scene
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.12728'}]
tags: ["Datasets", "Evaluation"]
short_authors: Smith et al.
---
Visual navigation localizes a query place image against a reference database
of place images, also known as a `visual map'. Localization accuracy
requirements for specific areas of the visual map, `scene classes', vary
according to the context of the environment and task. State-of-the-art visual
mapping is unable to reflect these requirements by explicitly targetting scene
classes for inclusion in the map. Four different scene classes, including
pedestrian crossings and stations, are identified in each of the Nordland and
St. Lucia datasets. Instead of re-training separate scene classifiers which
struggle with these overlapping scene classes we make our first contribution:
defining the problem of `scene retrieval'. Scene retrieval extends image
retrieval to classification of scenes defined at test time by associating a
single query image to reference images of scene classes. Our second
contribution is a triplet-trained convolutional neural network (CNN) to address
this problem which increases scene classification accuracy by up to 7% against
state-of-the-art networks pre-trained for scene recognition. The second
contribution is an algorithm `DMC' that combines our scene classification with
distance and memorability for visual mapping. Our analysis shows that DMC
includes 64% more images of our chosen scene classes in a visual map than just
using distance interval mapping. State-of-the-art visual place descriptors
AMOS-Net, Hybrid-Net and NetVLAD are finally used to show that DMC improves
scene class localization accuracy by a mean of 3% and localization accuracy of
the remaining map images by a mean of 10% across both datasets.