---
layout: publication
title: Evaluating Text-to-image Matching Using Binary Image Selection (BISON)
authors: Hexiang Hu, Ishan Misra, Laurens van Der Maaten
conference: 2019 IEEE/CVF International Conference on Computer Vision Workshop (ICCVW)
year: 2019
bibkey: hu2019evaluating
citations: 15
additional_links: [{name: Code, url: 'http://hexianghu.com/bison/'}, {name: Paper,
    url: 'https://arxiv.org/abs/1901.06595'}]
tags: ["Evaluation", "ICCV", "Image Retrieval"]
short_authors: Hexiang Hu, Ishan Misra, Laurens van Der Maaten
---
Providing systems the ability to relate linguistic and visual content is one
of the hallmarks of computer vision. Tasks such as text-based image retrieval
and image captioning were designed to test this ability but come with
evaluation measures that have a high variance or are difficult to interpret. We
study an alternative task for systems that match text and images: given a text
query, the system is asked to select the image that best matches the query from
a pair of semantically similar images. The system's accuracy on this Binary
Image SelectiON (BISON) task is interpretable, eliminates the reliability
problems of retrieval evaluations, and focuses on the system's ability to
understand fine-grained visual structure. We gather a BISON dataset that
complements the COCO dataset and use it to evaluate modern text-based image
retrieval and image captioning systems. Our results provide novel insights into
the performance of these systems. The COCO-BISON dataset and corresponding
evaluation code are publicly available from http://hexianghu.com/bison/.