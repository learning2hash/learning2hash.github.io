---
layout: publication
title: 'Imagesubject: A Large-scale Dataset For Subject Detection'
authors: Xin Miao, Jiayi Liu, Huayan Wang, Jun Fu
conference: Arxiv
year: 2022
bibkey: miao2022imagesubject
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.03101'}]
tags: ["Datasets"]
short_authors: Miao et al.
---
Main subjects usually exist in the images or videos, as they are the objects
that the photographer wants to highlight. Human viewers can easily identify
them but algorithms often confuse them with other objects. Detecting the main
subjects is an important technique to help machines understand the content of
images and videos. We present a new dataset with the goal of training models to
understand the layout of the objects and the context of the image then to find
the main subjects among them. This is achieved in three aspects. By gathering
images from movie shots created by directors with professional shooting skills,
we collect the dataset with strong diversity, specifically, it contains
107\,700 images from 21\,540 movie shots. We labeled them with the bounding box
labels for two classes: subject and non-subject foreground object. We present a
detailed analysis of the dataset and compare the task with saliency detection
and object detection. ImageSubject is the first dataset that tries to localize
the subject in an image that the photographer wants to highlight. Moreover, we
find the transformer-based detection model offers the best result among other
popular model architectures. Finally, we discuss the potential applications and
conclude with the importance of the dataset.