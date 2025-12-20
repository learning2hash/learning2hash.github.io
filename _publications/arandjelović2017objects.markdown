---
layout: publication
title: Objects That Sound
authors: "Relja Arandjelovi\u0107, Andrew Zisserman"
conference: Arxiv
year: 2017
bibkey: "arandjelovi\u01072017objects"
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.06651'}]
tags: ["Multimodal Retrieval"]
short_authors: "Relja Arandjelovi\u0107, Andrew Zisserman"
---
In this paper our objectives are, first, networks that can embed audio and
visual inputs into a common space that is suitable for cross-modal retrieval;
and second, a network that can localize the object that sounds in an image,
given the audio signal. We achieve both these objectives by training from
unlabelled video using only audio-visual correspondence (AVC) as the objective
function. This is a form of cross-modal self-supervision from video.
  To this end, we design new network architectures that can be trained for
cross-modal retrieval and localizing the sound source in an image, by using the
AVC task. We make the following contributions: (i) show that audio and visual
embeddings can be learnt that enable both within-mode (e.g. audio-to-audio) and
between-mode retrieval; (ii) explore various architectures for the AVC task,
including those for the visual stream that ingest a single image, or multiple
images, or a single image and multi-frame optical flow; (iii) show that the
semantic object that sounds within an image can be localized (using only the
sound, no motion or flow information); and (iv) give a cautionary tale on how
to avoid undesirable shortcuts in the data preparation.