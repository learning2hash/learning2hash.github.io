---
layout: publication
title: 'Towards Large-scale Building Attribute Mapping Using Crowdsourced Images:
  Scene Text Recognition On Flickr And Problems To Be Solved'
authors: Yao Sun, Anna Kruspe, Liqiu Meng, Yifan Tian, Eike J Hoffmann, Stefan Auer,
  Xiao Xiang Zhu
conference: The International Archives of the Photogrammetry, Remote Sensing and Spatial
  Information Sciences
year: 2023
bibkey: sun2023towards
citations: 1
additional_links: [{name: Code, url: 'https://github.com/ya0-sun/STR-Berlin'}, {name: Paper,
    url: 'https://arxiv.org/abs/2309.08042'}]
tags: ["Datasets", "Scalability"]
short_authors: Sun et al.
---
Crowdsourced platforms provide huge amounts of street-view images that
contain valuable building information. This work addresses the challenges in
applying Scene Text Recognition (STR) in crowdsourced street-view images for
building attribute mapping. We use Flickr images, particularly examining texts
on building facades. A Berlin Flickr dataset is created, and pre-trained STR
models are used for text detection and recognition. Manual checking on a subset
of STR-recognized images demonstrates high accuracy. We examined the
correlation between STR results and building functions, and analysed instances
where texts were recognized on residential buildings but not on commercial
ones. Further investigation revealed significant challenges associated with
this task, including small text regions in street-view images, the absence of
ground truth labels, and mismatches in buildings in Flickr images and building
footprints in OpenStreetMap (OSM). To develop city-wide mapping beyond urban
hotspot locations, we suggest differentiating the scenarios where STR proves
effective while developing appropriate algorithms or bringing in additional
data for handling other cases. Furthermore, interdisciplinary collaboration
should be undertaken to understand the motivation behind building photography
and labeling. The STR-on-Flickr results are publicly available at
https://github.com/ya0-sun/STR-Berlin.