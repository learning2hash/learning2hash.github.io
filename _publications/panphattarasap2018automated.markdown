---
layout: publication
title: 'Automated Map Reading: Image Based Localisation In 2-D Maps Using Binary Semantic
  Descriptors'
authors: Pilailuck Panphattarasap, Andrew Calway
conference: 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems
  (IROS)
year: 2018
bibkey: panphattarasap2018automated
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.00788'}]
tags: ["Evaluation", "IROS", "Scalability"]
short_authors: Pilailuck Panphattarasap, Andrew Calway
---
We describe a novel approach to image based localisation in urban
environments using semantic matching between images and a 2-D map. It contrasts
with the vast majority of existing approaches which use image to image database
matching. We use highly compact binary descriptors to represent semantic
features at locations, significantly increasing scalability compared with
existing methods and having the potential for greater invariance to variable
imaging conditions. The approach is also more akin to human map reading, making
it more suited to human-system interaction. The binary descriptors indicate the
presence or not of semantic features relating to buildings and road junctions
in discrete viewing directions. We use CNN classifiers to detect the features
in images and match descriptor estimates with a database of location tagged
descriptors derived from the 2-D map. In isolation, the descriptors are not
sufficiently discriminative, but when concatenated sequentially along a route,
their combination becomes highly distinctive and allows localisation even when
using non-perfect classifiers. Performance is further improved by taking into
account left or right turns over a route. Experimental results obtained using
Google StreetView and OpenStreetMap data show that the approach has
considerable potential, achieving localisation accuracy of around 85% using
routes corresponding to approximately 200 meters.