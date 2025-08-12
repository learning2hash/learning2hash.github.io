---
layout: publication
title: Large-image Object Detection For Fine-grained Recognition Of Punches Patterns
  In Medieval Panel Painting
authors: Josh Bruegger, Diana Ioana Catana, Vanja MacOvaz, Matias Valdenegro-Toro,
  Matthia Sabatelli, Marco Zullich
conference: Lecture Notes in Computer Science
year: 2025
bibkey: bruegger2025large
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.12489'}]
tags: ["Datasets"]
short_authors: Bruegger et al.
---
The attribution of the author of an art piece is typically a laborious manual
process, usually relying on subjective evaluations of expert figures. However,
there are some situations in which quantitative features of the artwork can
support these evaluations. The extraction of these features can sometimes be
automated, for instance, with the use of Machine Learning (ML) techniques. An
example of these features is represented by repeated, mechanically impressed
patterns, called punches, present chiefly in 13th and 14th-century panel
paintings from Tuscany. Previous research in art history showcased a strong
connection between the shapes of punches and specific artists or workshops,
suggesting the possibility of using these quantitative cues to support the
attribution. In the present work, we first collect a dataset of large-scale
images of these panel paintings. Then, using YOLOv10, a recent and popular
object detection model, we train a ML pipeline to perform object detection on
the punches contained in the images. Due to the large size of the images, the
detection procedure is split across multiple frames by adopting a
sliding-window approach with overlaps, after which the predictions are combined
for the whole image using a custom non-maximal suppression routine. Our results
indicate how art historians working in the field can reliably use our method
for the identification and extraction of punches.