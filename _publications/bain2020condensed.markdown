---
layout: publication
title: 'Condensed Movies: Story Based Retrieval With Contextual Embeddings'
authors: Max Bain, Arsha Nagrani, Andrew Brown, Andrew Zisserman
conference: Lecture Notes in Computer Science
year: 2020
bibkey: bain2020condensed
citations: 42
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.04208'}]
tags: ["Datasets", "Evaluation", "Video Retrieval"]
short_authors: Bain et al.
---
Our objective in this work is long range understanding of the narrative
structure of movies. Instead of considering the entire movie, we propose to
learn from the `key scenes' of the movie, providing a condensed look at the
full storyline. To this end, we make the following three contributions: (i) We
create the Condensed Movies Dataset (CMD) consisting of the key scenes from
over 3K movies: each key scene is accompanied by a high level semantic
description of the scene, character face-tracks, and metadata about the movie.
The dataset is scalable, obtained automatically from YouTube, and is freely
available for anybody to download and use. It is also an order of magnitude
larger than existing movie datasets in the number of movies; (ii) We provide a
deep network baseline for text-to-video retrieval on our dataset, combining
character, speech and visual cues into a single video embedding; and finally
(iii) We demonstrate how the addition of context from other video clips
improves retrieval performance.