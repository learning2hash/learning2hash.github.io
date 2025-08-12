---
layout: publication
title: Selecting Relevant Web Trained Concepts For Automated Event Retrieval
authors: Bharat Singh, Xintong Han, Zhe Wu, Vlad I. Morariu, Larry S. Davis
conference: 2015 IEEE International Conference on Computer Vision (ICCV)
year: 2015
bibkey: singh2015selecting
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1509.07845'}]
tags: ["ICCV"]
short_authors: Singh et al.
---
Complex event retrieval is a challenging research problem, especially when no
training videos are available. An alternative to collecting training videos is
to train a large semantic concept bank a priori. Given a text description of an
event, event retrieval is performed by selecting concepts linguistically
related to the event description and fusing the concept responses on unseen
videos. However, defining an exhaustive concept lexicon and pre-training it
requires vast computational resources. Therefore, recent approaches automate
concept discovery and training by leveraging large amounts of weakly annotated
web data. Compact visually salient concepts are automatically obtained by the
use of concept pairs or, more generally, n-grams. However, not all visually
salient n-grams are necessarily useful for an event query--some combinations of
concepts may be visually compact but irrelevant--and this drastically affects
performance. We propose an event retrieval algorithm that constructs pairs of
automatically discovered concepts and then prunes those concepts that are
unlikely to be helpful for retrieval. Pruning depends both on the query and on
the specific video instance being evaluated. Our approach also addresses
calibration and domain adaptation issues that arise when applying concept
detectors to unseen videos. We demonstrate large improvements over other vision
based systems on the TRECVID MED 13 dataset.