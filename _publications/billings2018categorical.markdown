---
layout: publication
title: Categorical Mixture Models On Vggnet Activations
authors: Sean Billings
conference: Arxiv
year: 2018
bibkey: billings2018categorical
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.02446'}]
tags: ["Unsupervised"]
short_authors: Sean Billings
---
In this project, I use unsupervised learning techniques in order to cluster a
set of yelp restaurant photos under meaningful topics. In order to do this, I
extract layer activations from a pre-trained implementation of the popular
VGGNet convolutional neural network. First, I explore using LDA with the
activations of convolutional layers as features. Secondly, I explore using the
object-recognition powers of VGGNet trained on ImageNet in order to extract
meaningful objects from the photos, and then perform LDA to group the photos
under topic-archetypes. I find that this second approach finds meaningful
archetypes, which match the human intuition for photo topics such as
restaurant, food, and drinks. Furthermore, these clusters align well and
distinctly with the actual yelp photo labels.