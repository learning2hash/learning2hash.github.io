---
layout: publication
title: Style-transfer Via Texture-synthesis
authors: Michael Elad, Peyman Milanfar
conference: IEEE Transactions on Image Processing
year: 2017
bibkey: elad2016style
citations: 152
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1609.03057'}]
tags: ["Image Retrieval"]
short_authors: Michael Elad, Peyman Milanfar
---
Style-transfer is a process of migrating a style from a given image to the
content of another, synthesizing a new image which is an artistic mixture of
the two. Recent work on this problem adopting Convolutional Neural-networks
(CNN) ignited a renewed interest in this field, due to the very impressive
results obtained. There exists an alternative path towards handling the
style-transfer task, via generalization of texture-synthesis algorithms. This
approach has been proposed over the years, but its results are typically less
impressive compared to the CNN ones.
  In this work we propose a novel style-transfer algorithm that extends the
texture-synthesis work of Kwatra et. al. (2005), while aiming to get stylized
images that get closer in quality to the CNN ones. We modify Kwatra's algorithm
in several key ways in order to achieve the desired transfer, with emphasis on
a consistent way for keeping the content intact in selected regions, while
producing hallucinated and rich style in others. The results obtained are
visually pleasing and diverse, shown to be competitive with the recent CNN
style-transfer algorithms. The proposed algorithm is fast and flexible, being
able to process any pair of content + style images.