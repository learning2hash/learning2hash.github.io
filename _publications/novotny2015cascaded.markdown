---
layout: publication
title: Cascaded Sparse Spatial Bins For Efficient And Effective Generic Object Detection
authors: David Novotny, Jiri Matas
conference: 2015 IEEE International Conference on Computer Vision (ICCV)
year: 2015
bibkey: novotny2015cascaded
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1504.07029'}]
tags: ["Efficiency", "ICCV"]
short_authors: David Novotny, Jiri Matas
---
A novel efficient method for extraction of object proposals is introduced.
Its "objectness" function exploits deep spatial pyramid features, a novel
fast-to-compute HoG-based edge statistic and the EdgeBoxes score. The
efficiency is achieved by the use of spatial bins in a novel combination with
sparsity-inducing group normalized SVM. State-of-the-art recall performance is
achieved on Pascal VOC07, significantly outperforming methods with comparable
speed. Interestingly, when only 100 proposals per image are considered the
method attains 78% recall on VOC07. The method improves mAP of the RCNN
state-of-the-art class-specific detector, increasing it by 10 points when only
50 proposals are used in each image. The system trained on twenty classes
performs well on the two hundred class ILSVRC2013 set confirming generalization
capability.