---
layout: publication
title: 'Shotit: Compute-efficient Image-to-video Search Engine For The Cloud'
authors: Leslie Wong
conference: Arxiv
year: 2024
bibkey: wong2024shotit
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.12169'}]
tags: ["Datasets", "Image Retrieval", "Video Retrieval"]
short_authors: Leslie Wong
---
With the rapid growth of information technology, users are exposed to a
massive amount of data online, including image, music, and video. This has led
to strong needs to provide effective corresponsive search services such as
image, music, and video search services. Most of them are operated based on
keywords, namely using keywords to find related image, music, and video.
Additionally, there are image-to-image search services that enable users to
find similar images using one input image. Given that videos are essentially
composed of image frames, then similar videos can be searched by one input
image or screenshot. We want to target this scenario and provide an efficient
method and implementation in this paper.
  We present Shotit, a cloud-native image-to-video search engine that tailors
this search scenario in a compute-efficient approach. One main limitation faced
in this scenario is the scale of its dataset. A typical image-to-image search
engine only handles one-to-one relationships, colloquially, one image
corresponds to another single image. But image-to-video proliferates. Take a
24-min length video as an example, it will generate roughly 20,000 image
frames. As the number of videos grows, the scale of the dataset explodes
exponentially. In this case, a compute-efficient approach ought to be
considered, and the system design should cater to the cloud-native trend.
Choosing an emerging technology - vector database as its backbone, Shotit fits
these two metrics performantly. Experiments for two different datasets, a 50
thousand-scale Blender Open Movie dataset, and a 50 million-scale proprietary
TV genre dataset at a 4 Core 32GB RAM Intel Xeon Gold 6271C cloud machine with
object storage reveal the effectiveness of Shotit. A demo regarding the Blender
Open Movie dataset is illustrated within this paper.