---
layout: publication
title: Night-to-day Image Translation For Retrieval-based Localization
authors: Asha Anoosheh, Torsten Sattler, Radu Timofte, Marc Pollefeys, Luc van Gool
conference: 2019 International Conference on Robotics and Automation (ICRA)
year: 2018
bibkey: anoosheh2018night
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.09767'}]
tags: ["Datasets", "Evaluation", "ICRA", "Image Retrieval"]
short_authors: Anoosheh et al.
---
Visual localization is a key step in many robotics pipelines, allowing the
robot to (approximately) determine its position and orientation in the world.
An efficient and scalable approach to visual localization is to use image
retrieval techniques. These approaches identify the image most similar to a
query photo in a database of geo-tagged images and approximate the query's pose
via the pose of the retrieved database image. However, image retrieval across
drastically different illumination conditions, e.g. day and night, is still a
problem with unsatisfactory results, even in this age of powerful neural
models. This is due to a lack of a suitably diverse dataset with true
correspondences to perform end-to-end learning. A recent class of neural models
allows for realistic translation of images among visual domains with relatively
little training data and, most importantly, without ground-truth pairings. In
this paper, we explore the task of accurately localizing images captured from
two traversals of the same area in both day and night. We propose ToDayGAN - a
modified image-translation model to alter nighttime driving images to a more
useful daytime representation. We then compare the daytime and translated night
images to obtain a pose estimate for the night image using the known 6-DOF
position of the closest day image. Our approach improves localization
performance by over 250% compared the current state-of-the-art, in the context
of standard metrics in multiple categories.