---
layout: publication
title: Resolving Referring Expressions In Images With Labeled Elements
authors: Nevan Wichers, Dilek Hakkani-Tur, Jindong Chen
conference: 2018 IEEE Spoken Language Technology Workshop (SLT)
year: 2018
bibkey: wichers2018resolving
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.10165'}]
tags: []
short_authors: Nevan Wichers, Dilek Hakkani-Tur, Jindong Chen
---
Images may have elements containing text and a bounding box associated with
them, for example, text identified via optical character recognition on a
computer screen image, or a natural image with labeled objects. We present an
end-to-end trainable architecture to incorporate the information from these
elements and the image to segment/identify the part of the image a natural
language expression is referring to. We calculate an embedding for each element
and then project it onto the corresponding location (i.e., the associated
bounding box) of the image feature map. We show that this architecture gives an
improvement in resolving referring expressions, over only using the image, and
other methods that incorporate the element information. We demonstrate
experimental results on the referring expression datasets based on COCO, and on
a webpage image referring expression dataset that we developed.