---
layout: publication
title: Inner-scene Similarities As A Contextual Cue For Object Detection
authors: Noa Arbel, Tamar Avraham, Michael Lindenbaum
conference: Arxiv
year: 2017
bibkey: arbel2017inner
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.04406'}]
tags: []
short_authors: Noa Arbel, Tamar Avraham, Michael Lindenbaum
---
Using image context is an effective approach for improving object detection.
Previously proposed methods used contextual cues that rely on semantic or
spatial information. In this work, we explore a different kind of contextual
information: inner-scene similarity. We present the CISS (Context by Inner
Scene Similarity) algorithm, which is based on the observation that two
visually similar sub-image patches are likely to share semantic identities,
especially when both appear in the same image. CISS uses base-scores provided
by a base detector and performs as a post-detection stage. For each candidate
sub-image (denoted anchor), the CISS algorithm finds a few similar sub-images
(denoted supporters), and, using them, calculates a new enhanced score for the
anchor. This is done by utilizing the base-scores of the supporters and a
pre-trained dependency model. The new scores are modeled as a linear function
of the base scores of the anchor and the supporters and is estimated using a
minimum mean square error optimization. This approach results in: (a) improved
detection of partly occluded objects (when there are similar non-occluded
objects in the scene), and (b) fewer false alarms (when the base detector
mistakenly classifies a background patch as an object). This work relates to
Duncan and Humphreys' "similarity theory," a psychophysical study. which
suggested that the human visual system perceptually groups similar image
regions and that the classification of one region is affected by the estimated
identity of the other. Experimental results demonstrate the enhancement of a
base detector's scores on the PASCAL VOC dataset.