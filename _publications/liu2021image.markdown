---
layout: publication
title: Image Retrieval On Real-life Images With Pre-trained Vision-and-language Models
authors: Zheyuan Liu, Cristian Rodriguez-opazo, Damien Teney, Stephen Gould
conference: Arxiv
year: 2021
citations: 97
bibkey: liu2021image
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.04024'}]
tags: [Applications, Tools and Libraries]
---
We extend the task of composed image retrieval, where an input query consists
of an image and short textual description of how to modify the image. Existing
methods have only been applied to non-complex images within narrow domains,
such as fashion products, thereby limiting the scope of study on in-depth
visual reasoning in rich image and language contexts. To address this issue, we
collect the Compose Image Retrieval on Real-life images (CIRR) dataset, which
consists of over 36,000 pairs of crowd-sourced, open-domain images with
human-generated modifying text. To extend current methods to the open-domain,
we propose CIRPLANT, a transformer based model that leverages rich pre-trained
vision-and-language (V&L) knowledge for modifying visual features conditioned
on natural language. Retrieval is then done by nearest neighbor lookup on the
modified features. We demonstrate that with a relatively simple architecture,
CIRPLANT outperforms existing methods on open-domain images, while matching
state-of-the-art accuracy on the existing narrow datasets, such as fashion.
Together with the release of CIRR, we believe this work will inspire further
research on composed image retrieval.