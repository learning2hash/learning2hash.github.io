---
layout: publication
title: A Data-driven Approach For Tag Refinement And Localization In Web Videos
authors: Lamberto Ballan, Marco Bertini, Giuseppe Serra, Alberto del Bimbo
conference: Computer Vision and Image Understanding
year: 2015
bibkey: ballan2014data
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1407.0623'}]
tags: ["Video Retrieval"]
short_authors: Ballan et al.
---
Tagging of visual content is becoming more and more widespread as web-based
services and social networks have popularized tagging functionalities among
their users. These user-generated tags are used to ease browsing and
exploration of media collections, e.g. using tag clouds, or to retrieve
multimedia content. However, not all media are equally tagged by users. Using
the current systems is easy to tag a single photo, and even tagging a part of a
photo, like a face, has become common in sites like Flickr and Facebook. On the
other hand, tagging a video sequence is more complicated and time consuming, so
that users just tag the overall content of a video. In this paper we present a
method for automatic video annotation that increases the number of tags
originally provided by users, and localizes them temporally, associating tags
to keyframes. Our approach exploits collective knowledge embedded in
user-generated tags and web sources, and visual similarity of keyframes and
images uploaded to social sites like YouTube and Flickr, as well as web sources
like Google and Bing. Given a keyframe, our method is able to select on the fly
from these visual sources the training exemplars that should be the most
relevant for this test sample, and proceeds to transfer labels across similar
images. Compared to existing video tagging approaches that require training
classifiers for each tag, our system has few parameters, is easy to implement
and can deal with an open vocabulary scenario. We demonstrate the approach on
tag refinement and localization on DUT-WEBV, a large dataset of web videos, and
show state-of-the-art results.