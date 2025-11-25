---
layout: publication
title: 'Avlnet: Learning Audio-visual Language Representations From Instructional
  Videos'
authors: Andrew Rouditchenko, Angie Boggust, David Harwath, Brian Chen, Dhiraj Joshi,
  Samuel Thomas, Kartik Audhkhasi, Hilde Kuehne, Rameswar Panda, Rogerio Feris, Brian
  Kingsbury, Michael Picheny, Antonio Torralba, James Glass
conference: Arxiv
year: 2020
bibkey: rouditchenko2020avlnet
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.09199'}]
tags: ["Image Retrieval", "Multimodal Retrieval", "Self-Supervised", "Video Retrieval"]
short_authors: Rouditchenko et al.
---
Current methods for learning visually grounded language from videos often
rely on text annotation, such as human generated captions or machine generated
automatic speech recognition (ASR) transcripts. In this work, we introduce the
Audio-Video Language Network (AVLnet), a self-supervised network that learns a
shared audio-visual embedding space directly from raw video inputs. To
circumvent the need for text annotation, we learn audio-visual representations
from randomly segmented video clips and their raw audio waveforms. We train
AVLnet on HowTo100M, a large corpus of publicly available instructional videos,
and evaluate on image retrieval and video retrieval tasks, achieving
state-of-the-art performance. We perform analysis of AVLnet's learned
representations, showing our model utilizes speech and natural sounds to learn
audio-visual concepts. Further, we propose a tri-modal model that jointly
processes raw audio, video, and text captions from videos to learn a
multi-modal semantic embedding space useful for text-video retrieval. Our code,
data, and trained models will be released at avlnet.csail.mit.edu