---
layout: publication
title: 'Learning Artistic Signatures: Symmetry Discovery And Style Transfer'
authors: Emma Finn, T. Anderson Keller, Emmanouil Theodosis, Demba E. Ba
conference: Arxiv
year: 2024
bibkey: finn2024learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.04441'}]
tags: []
short_authors: Finn et al.
---
Despite nearly a decade of literature on style transfer, there is no
undisputed definition of artistic style. State-of-the-art models produce
impressive results but are difficult to interpret since, without a coherent
definition of style, the problem of style transfer is inherently ill-posed.
Early work framed style-transfer as an optimization problem but treated style
as a measure only of texture. This led to artifacts in the outputs of early
models where content features from the style image sometimes bled into the
output image. Conversely, more recent work with diffusion models offers
compelling empirical results but provides little theoretical grounding. To
address these issues, we propose an alternative definition of artistic style.
We suggest that style should be thought of as a set of global symmetries that
dictate the arrangement of local textures. We validate this perspective
empirically by learning the symmetries of a large dataset of paintings and
showing that symmetries are predictive of the artistic movement to which each
painting belongs. Finally, we show that by considering both local and global
features, using both Lie generators and traditional measures of texture, we can
quantitatively capture the stylistic similarity between artists better than
with either set of features alone. This approach not only aligns well with art
historians' consensus but also offers a robust framework for distinguishing
nuanced stylistic differences, allowing for a more interpretable, theoretically
grounded approach to style transfer.