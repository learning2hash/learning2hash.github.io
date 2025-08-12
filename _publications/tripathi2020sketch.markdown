---
layout: publication
title: Sketch-guided Object Localization In Natural Images
authors: Aditay Tripathi, Rajath R Dani, Anand Mishra, Anirban Chakraborty
conference: Lecture Notes in Computer Science
year: 2020
bibkey: tripathi2020sketch
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.06551'}]
tags: ["Image Retrieval"]
short_authors: Tripathi et al.
---
We introduce the novel problem of localizing all the instances of an object
(seen or unseen during training) in a natural image via sketch query. We refer
to this problem as sketch-guided object localization. This problem is
distinctively different from the traditional sketch-based image retrieval task
where the gallery set often contains images with only one object. The
sketch-guided object localization proves to be more challenging when we
consider the following: (i) the sketches used as queries are abstract
representations with little information on the shape and salient attributes of
the object, (ii) the sketches have significant variability as they are
hand-drawn by a diverse set of untrained human subjects, and (iii) there exists
a domain gap between sketch queries and target natural images as these are
sampled from very different data distributions. To address the problem of
sketch-guided object localization, we propose a novel cross-modal attention
scheme that guides the region proposal network (RPN) to generate object
proposals relevant to the sketch query. These object proposals are later scored
against the query to obtain final localization. Our method is effective with as
little as a single sketch query. Moreover, it also generalizes well to object
categories not seen during training and is effective in localizing multiple
object instances present in the image. Furthermore, we extend our framework to
a multi-query setting using novel feature fusion and attention fusion
strategies introduced in this paper. The localization performance is evaluated
on publicly available object detection benchmarks, viz. MS-COCO and PASCAL-VOC,
with sketch queries obtained from `Quick, Draw!'. The proposed method
significantly outperforms related baselines on both single-query and
multi-query localization tasks.