---
layout: publication
title: Fine-tuned But Zero-shot 3D Shape Sketch View Similarity And Retrieval
authors: Gianluca Berardi, Yulia Gryaditskaya
conference: 2023 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW)
year: 2023
bibkey: berardi2023fine
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.08541'}]
tags: [Evaluation, Supervised, ICCV, Few-shot & Zero-shot, Datasets]
short_authors: Gianluca Berardi, Yulia Gryaditskaya
---
Recently, encoders like ViT (vision transformer) and ResNet have been trained
on vast datasets and utilized as perceptual metrics for comparing sketches and
images, as well as multi-domain encoders in a zero-shot setting. However, there
has been limited effort to quantify the granularity of these encoders. Our work
addresses this gap by focusing on multi-modal 2D projections of individual 3D
instances. This task holds crucial implications for retrieval and sketch-based
modeling. We show that in a zero-shot setting, the more abstract the sketch,
the higher the likelihood of incorrect image matches. Even within the same
sketch domain, sketches of the same object drawn in different styles, for
example by distinct individuals, might not be accurately matched. One of the
key findings of our research is that meticulous fine-tuning on one class of 3D
shapes can lead to improved performance on other shape classes, reaching or
surpassing the accuracy of supervised methods. We compare and discuss several
fine-tuning strategies. Additionally, we delve deeply into how the scale of an
object in a sketch influences the similarity of features at different network
layers, helping us identify which network layers provide the most accurate
matching. Significantly, we discover that ViT and ResNet perform best when
dealing with similar object scales. We believe that our work will have a
significant impact on research in the sketch domain, providing insights and
guidance on how to adopt large pretrained models as perceptual losses.