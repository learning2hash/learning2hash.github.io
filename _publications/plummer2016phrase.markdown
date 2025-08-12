---
layout: publication
title: Phrase Localization And Visual Relationship Detection With Comprehensive Image-language
  Cues
authors: Bryan A. Plummer, Arun Mallya, Christopher M. Cervantes, Julia Hockenmaier,
  Svetlana Lazebnik
conference: 2017 IEEE International Conference on Computer Vision (ICCV)
year: 2017
bibkey: plummer2016phrase
citations: 177
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.06641'}]
tags: ["ICCV"]
short_authors: Plummer et al.
---
This paper presents a framework for localization or grounding of phrases in
images using a large collection of linguistic and visual cues. We model the
appearance, size, and position of entity bounding boxes, adjectives that
contain attribute information, and spatial relationships between pairs of
entities connected by verbs or prepositions. Special attention is given to
relationships between people and clothing or body part mentions, as they are
useful for distinguishing individuals. We automatically learn weights for
combining these cues and at test time, perform joint inference over all phrases
in a caption. The resulting system produces state of the art performance on
phrase localization on the Flickr30k Entities dataset and visual relationship
detection on the Stanford VRD dataset.