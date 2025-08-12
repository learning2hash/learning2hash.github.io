---
layout: publication
title: Lyric Video Analysis Using Text Detection And Tracking
authors: Shota Sakaguchi, Jun Kato, Masataka Goto, Seiichi Uchida
conference: Lecture Notes in Computer Science
year: 2020
bibkey: sakaguchi2020lyric
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.11933'}]
tags: ["Video Retrieval"]
short_authors: Sakaguchi et al.
---
We attempt to recognize and track lyric words in lyric videos. Lyric video is
a music video showing the lyric words of a song. The main characteristic of
lyric videos is that the lyric words are shown at frames synchronously with the
music. The difficulty of recognizing and tracking the lyric words is that (1)
the words are often decorated and geometrically distorted and (2) the words
move arbitrarily and drastically in the video frame. The purpose of this paper
is to analyze the motion of the lyric words in lyric videos, as the first step
of automatic lyric video generation. In order to analyze the motion of lyric
words, we first apply a state-of-the-art scene text detector and recognizer to
each video frame. Then, lyric-frame matching is performed to establish the
optimal correspondence between lyric words and the frames. After fixing the
motion trajectories of individual lyric words from correspondence, we analyze
the trajectories of the lyric words by k-medoids clustering and dynamic time
warping (DTW).