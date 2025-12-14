---
layout: publication
title: Do We Really Need Scene-specific Pose Encoders?
authors: Yoli Shavit, Ron Ferens
conference: 2020 25th International Conference on Pattern Recognition (ICPR)
year: 2020
bibkey: shavit2020do
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.12014'}]
tags: [Image Retrieval]
short_authors: Yoli Shavit, Ron Ferens
---
Visual pose regression models estimate the camera pose from a query image
with a single forward pass. Current models learn pose encoding from an image
using deep convolutional networks which are trained per scene. The resulting
encoding is typically passed to a multi-layer perceptron in order to regress
the pose. In this work, we propose that scene-specific pose encoders are not
required for pose regression and that encodings trained for visual similarity
can be used instead. In order to test our hypothesis, we take a shallow
architecture of several fully connected layers and train it with pre-computed
encodings from a generic image retrieval model. We find that these encodings
are not only sufficient to regress the camera pose, but that, when provided to
a branching fully connected architecture, a trained model can achieve
competitive results and even surpass current \textit\{state-of-the-art\} pose
regressors in some cases. Moreover, we show that for outdoor localization, the
proposed architecture is the only pose regressor, to date, consistently
localizing in under 2 meters and 5 degrees.