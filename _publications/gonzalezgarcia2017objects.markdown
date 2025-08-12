---
layout: publication
title: Objects As Context For Detecting Their Semantic Parts
authors: Abel Gonzalez-garcia, Davide Modolo, Vittorio Ferrari
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: gonzalezgarcia2017objects
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.09529'}]
tags: ["CVPR"]
short_authors: Abel Gonzalez-garcia, Davide Modolo, Vittorio Ferrari
---
We present a semantic part detection approach that effectively leverages
object information.We use the object appearance and its class as indicators of
what parts to expect. We also model the expected relative location of parts
inside the objects based on their appearance. We achieve this with a new
network module, called OffsetNet, that efficiently predicts a variable number
of part locations within a given object. Our model incorporates all these cues
to detect parts in the context of their objects. This leads to considerably
higher performance for the challenging task of part detection compared to using
part appearance alone (+5 mAP on the PASCAL-Part dataset). We also compare to
other part detection methods on both PASCAL-Part and CUB200-2011 datasets.