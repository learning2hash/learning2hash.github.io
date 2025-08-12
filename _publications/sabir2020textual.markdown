---
layout: publication
title: Textual Visual Semantic Dataset For Text Spotting
authors: "Ahmed Sabir, Francesc Moreno-Noguer, Llu\xEDs Padr\xF3"
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2020
bibkey: sabir2020textual
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.10349'}]
tags: ["CVPR", "Datasets"]
short_authors: "Ahmed Sabir, Francesc Moreno-Noguer, Llu\xEDs Padr\xF3"
---
Text Spotting in the wild consists of detecting and recognizing text
appearing in images (e.g. signboards, traffic signals or brands in clothing or
objects). This is a challenging problem due to the complexity of the context
where texts appear (uneven backgrounds, shading, occlusions, perspective
distortions, etc.). Only a few approaches try to exploit the relation between
text and its surrounding environment to better recognize text in the scene. In
this paper, we propose a visual context dataset for Text Spotting in the wild,
where the publicly available dataset COCO-text [Veit et al. 2016] has been
extended with information about the scene (such as objects and places appearing
in the image) to enable researchers to include semantic relations between texts
and scene in their Text Spotting systems, and to offer a common framework for
such approaches. For each text in an image, we extract three kinds of context
information: objects in the scene, image location label and a textual image
description (caption). We use state-of-the-art out-of-the-box available tools
to extract this additional information. Since this information has textual
form, it can be used to leverage text similarity or semantic relation methods
into Text Spotting systems, either as a post-processing or in an end-to-end
training strategy. Our data is publicly available at https://git.io/JeZTb.