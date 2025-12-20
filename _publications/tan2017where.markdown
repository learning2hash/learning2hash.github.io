---
layout: publication
title: Where And Who? Automatic Semantic-aware Person Composition
authors: Fuwen Tan, Crispin Bernier, Benjamin Cohen, Vicente Ordonez, Connelly Barnes
conference: Arxiv
year: 2017
bibkey: tan2017where
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.01021'}]
tags: ["Uncategorized"]
short_authors: Tan et al.
---
Image compositing is a method used to generate realistic yet fake imagery by
inserting contents from one image to another. Previous work in compositing has
focused on improving appearance compatibility of a user selected foreground
segment and a background image (i.e. color and illumination consistency). In
this work, we instead develop a fully automated compositing model that
additionally learns to select and transform compatible foreground segments from
a large collection given only an input image background. To simplify the task,
we restrict our problem by focusing on human instance composition, because
human segments exhibit strong correlations with their background and because of
the availability of large annotated data. We develop a novel branching
Convolutional Neural Network (CNN) that jointly predicts candidate person
locations given a background image. We then use pre-trained deep feature
representations to retrieve person instances from a large segment database.
Experimental results show that our model can generate composite images that
look visually convincing. We also develop a user interface to demonstrate the
potential application of our method.