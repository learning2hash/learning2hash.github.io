---
layout: publication
title: 'PIGEON: Predicting Image Geolocations'
authors: Lukas Haas, Michal Skreta, Silas Alberti, Chelsea Finn
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: haas2023pigeon
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.05845'}]
tags: ["CVPR"]
short_authors: Haas et al.
---
Planet-scale image geolocalization remains a challenging problem due to the
diversity of images originating from anywhere in the world. Although approaches
based on vision transformers have made significant progress in geolocalization
accuracy, success in prior literature is constrained to narrow distributions of
images of landmarks, and performance has not generalized to unseen places. We
present a new geolocalization system that combines semantic geocell creation,
multi-task contrastive pretraining, and a novel loss function. Additionally,
our work is the first to perform retrieval over location clusters for guess
refinements. We train two models for evaluations on street-level data and
general-purpose image geolocalization; the first model, PIGEON, is trained on
data from the game of Geoguessr and is capable of placing over 40% of its
guesses within 25 kilometers of the target location globally. We also develop a
bot and deploy PIGEON in a blind experiment against humans, ranking in the top
0.01% of players. We further challenge one of the world's foremost professional
Geoguessr players to a series of six matches with millions of viewers, winning
all six games. Our second model, PIGEOTTO, differs in that it is trained on a
dataset of images from Flickr and Wikipedia, achieving state-of-the-art results
on a wide range of image geolocalization benchmarks, outperforming the previous
SOTA by up to 7.7 percentage points on the city accuracy level and up to 38.8
percentage points on the country level. Our findings suggest that PIGEOTTO is
the first image geolocalization model that effectively generalizes to unseen
places and that our approach can pave the way for highly accurate, planet-scale
image geolocalization systems. Our code is available on GitHub.