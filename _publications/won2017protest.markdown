---
layout: publication
title: Protest Activity Detection And Perceived Violence Estimation From Social Media
  Images
authors: Donghyeon Won, Zachary C. Steinert-Threlkeld, Jungseock Joo
conference: Proceedings of the 25th ACM international conference on Multimedia
year: 2017
bibkey: won2017protest
citations: 95
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.06204'}]
tags: ["Datasets"]
short_authors: Donghyeon Won, Zachary C. Steinert-Threlkeld, Jungseock Joo
---
We develop a novel visual model which can recognize protesters, describe
their activities by visual attributes and estimate the level of perceived
violence in an image. Studies of social media and protests use natural language
processing to track how individuals use hashtags and links, often with a focus
on those items' diffusion. These approaches, however, may not be effective in
fully characterizing actual real-world protests (e.g., violent or peaceful) or
estimating the demographics of participants (e.g., age, gender, and race) and
their emotions. Our system characterizes protests along these dimensions. We
have collected geotagged tweets and their images from 2013-2017 and analyzed
multiple major protest events in that period. A multi-task convolutional neural
network is employed in order to automatically classify the presence of
protesters in an image and predict its visual attributes, perceived violence
and exhibited emotions. We also release the UCLA Protest Image Dataset, our
novel dataset of 40,764 images (11,659 protest images and hard negatives) with
various annotations of visual attributes and sentiments. Using this dataset, we
train our model and demonstrate its effectiveness. We also present experimental
results from various analysis on geotagged image data in several prevalent
protest events. Our dataset will be made accessible at
https://www.sscnet.ucla.edu/comm/jjoo/mm-protest/.