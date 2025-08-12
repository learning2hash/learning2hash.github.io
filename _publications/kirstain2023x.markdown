---
layout: publication
title: 'X&fuse: Fusing Visual Information In Text-to-image Generation'
authors: Yuval Kirstain, Omer Levy, Adam Polyak
conference: Arxiv
year: 2023
bibkey: kirstain2023x
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.01000'}]
tags: ["Evaluation"]
short_authors: Yuval Kirstain, Omer Levy, Adam Polyak
---
We introduce X&Fuse, a general approach for conditioning on visual
information when generating images from text. We demonstrate the potential of
X&Fuse in three different text-to-image generation scenarios. (i) When a bank
of images is available, we retrieve and condition on a related image
(Retrieve&Fuse), resulting in significant improvements on the MS-COCO
benchmark, gaining a state-of-the-art FID score of 6.65 in zero-shot settings.
(ii) When cropped-object images are at hand, we utilize them and perform
subject-driven generation (Crop&Fuse), outperforming the textual inversion
method while being more than x100 faster. (iii) Having oracle access to the
image scene (Scene&Fuse), allows us to achieve an FID score of 5.03 on MS-COCO
in zero-shot settings. Our experiments indicate that X&Fuse is an effective,
easy-to-adapt, simple, and general approach for scenarios in which the model
may benefit from additional visual information.