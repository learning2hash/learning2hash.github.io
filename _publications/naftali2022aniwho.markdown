---
layout: publication
title: 'Aniwho : A Quick And Accurate Way To Classify Anime Character Faces In Images'
authors: Martinus Grady Naftali, Jason Sebastian Sulistyawan, Kelvin Julian
conference: Arxiv
year: 2022
bibkey: naftali2022aniwho
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.11012'}]
tags: []
short_authors: Martinus Grady Naftali, Jason Sebastian Sulistyawan, Kelvin Julian
---
In order to classify Japanese animation-style character faces, this paper
attempts to delve further into the many models currently available, including
InceptionV3, InceptionResNetV2, MobileNetV2, and EfficientNet, employing
transfer learning. This paper demonstrates that EfficientNet-B7, which achieves
a top-1 accuracy of 85.08%, has the highest accuracy rate. MobileNetV2, which
achieves a less accurate result with a top-1 accuracy of 81.92%, benefits from
a significantly faster inference time and fewer required parameters. However,
from the experiment, MobileNet-V2 is prone to overfitting; EfficienNet-B0 fixed
the overfitting issue but with a cost of a little slower in inference time than
MobileNet-V2 but a little more accurate result, top-1 accuracy of 83.46%. This
paper also uses a few-shot learning architecture called Prototypical Networks,
which offers an adequate substitute for conventional transfer learning
techniques.