---
layout: publication
title: 'Trufor: Leveraging All-round Clues For Trustworthy Image Forgery Detection
  And Localization'
authors: Fabrizio Guillaro, Davide Cozzolino, Avneesh Sud, Nicholas Dufour, Luisa
  Verdoliva
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: guillaro2023trufor
citations: 68
additional_links: [{name: Code, url: 'https://grip-unina.github.io/TruFor/'}, {name: Paper,
    url: 'https://arxiv.org/abs/2212.10957'}]
tags: ["CVPR"]
short_authors: Guillaro et al.
---
In this paper we present TruFor, a forensic framework that can be applied to
a large variety of image manipulation methods, from classic cheapfakes to more
recent manipulations based on deep learning. We rely on the extraction of both
high-level and low-level traces through a transformer-based fusion architecture
that combines the RGB image and a learned noise-sensitive fingerprint. The
latter learns to embed the artifacts related to the camera internal and
external processing by training only on real data in a self-supervised manner.
Forgeries are detected as deviations from the expected regular pattern that
characterizes each pristine image. Looking for anomalies makes the approach
able to robustly detect a variety of local manipulations, ensuring
generalization. In addition to a pixel-level localization map and a whole-image
integrity score, our approach outputs a reliability map that highlights areas
where localization predictions may be error-prone. This is particularly
important in forensic applications in order to reduce false alarms and allow
for a large scale analysis. Extensive experiments on several datasets show that
our method is able to reliably detect and localize both cheapfakes and
deepfakes manipulations outperforming state-of-the-art works. Code is publicly
available at https://grip-unina.github.io/TruFor/