---
layout: publication
title: 'Look At Here : Utilizing Supervision To Attend Subtle Key Regions'
authors: Changhwan Lee, Yeesuk Kim, Bong Gun Lee, Doosup Kim, Jongseong Jang
conference: Arxiv
year: 2021
bibkey: lee2021look
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.13233'}]
tags: ["Supervised"]
short_authors: Lee et al.
---
Despite the success of deep learning in computer vision, algorithms to
recognize subtle and small objects (or regions) is still challenging. For
example, recognizing a baseball or a frisbee on a ground scene or a bone
fracture in an X-ray image can easily result in overfitting, unless a huge
amount of training data is available. To mitigate this problem, we need a way
to force a model should identify subtle regions in limited training data. In
this paper, we propose a simple but efficient supervised augmentation method
called Cut\&Remain. It achieved better performance on various medical image
domain (internally sourced- and public dataset) and a natural image domain
(MS-COCO\(_s\)) than other supervised augmentation and the explicit guidance
methods.
  In addition, using the class activation map, we identified that the
Cut\&Remain methods drive a model to focus on relevant subtle and small regions
efficiently. We also show that the performance monotonically increased along
the Cut\&Remain ratio, indicating that a model can be improved even though only
limited amount of Cut\&Remain is applied for, so that it allows low supervising
(annotation) cost for improvement.