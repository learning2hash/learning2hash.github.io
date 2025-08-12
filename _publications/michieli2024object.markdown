---
layout: publication
title: Object-conditioned Bag Of Instances For Few-shot Personalized Instance Recognition
authors: Umberto Michieli, Jijoong Moon, Daehyun Kim, Mete Ozay
conference: ICASSP 2024 - 2024 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2024
bibkey: michieli2024object
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.01397'}]
tags: ["Few Shot & Zero Shot", "ICASSP"]
short_authors: Michieli et al.
---
Nowadays, users demand for increased personalization of vision systems to
localize and identify personal instances of objects (e.g., my dog rather than
dog) from a few-shot dataset only. Despite outstanding results of deep networks
on classical label-abundant benchmarks (e.g., those of the latest YOLOv8 model
for standard object detection), they struggle to maintain within-class
variability to represent different instances rather than object categories
only. We construct an Object-conditioned Bag of Instances (OBoI) based on
multi-order statistics of extracted features, where generic object detection
models are extended to search and identify personal instances from the OBoI's
metric space, without need for backpropagation. By relying on multi-order
statistics, OBoI achieves consistent superior accuracy in distinguishing
different instances. In the results, we achieve 77.1% personal object
recognition accuracy in case of 18 personal instances, showing about 12%
relative gain over the state of the art.