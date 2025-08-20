---
layout: publication
title: Geometrically Mappable Image Features
authors: Janine Thoma, Danda Pani Paudel, Ajad Chhatkuli, Luc van Gool
conference: IEEE Robotics and Automation Letters
year: 2020
bibkey: thoma2020geometrically
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.09682'}]
tags: [Evaluation, Image Retrieval]
short_authors: Thoma et al.
---
Vision-based localization of an agent in a map is an important problem in
robotics and computer vision. In that context, localization by learning
matchable image features is gaining popularity due to recent advances in
machine learning. Features that uniquely describe the visual contents of images
have a wide range of applications, including image retrieval and understanding.
In this work, we propose a method that learns image features targeted for
image-retrieval-based localization. Retrieval-based localization has several
benefits, such as easy maintenance and quick computation. However, the
state-of-the-art features only provide visual similarity scores which do not
explicitly reveal the geometric distance between query and retrieved images.
Knowing this distance is highly desirable for accurate localization, especially
when the reference images are sparsely distributed in the scene. Therefore, we
propose a novel loss function for learning image features which are both
visually representative and geometrically relatable. This is achieved by
guiding the learning process such that the feature and geometric distances
between images are directly proportional. In our experiments we show that our
features not only offer significantly better localization accuracy, but also
allow to estimate the trajectory of a query sequence in absence of the
reference images.