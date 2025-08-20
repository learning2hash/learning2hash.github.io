---
layout: publication
title: Fractional Local Neighborhood Intensity Pattern For Image Retrieval Using Genetic
  Algorithm
authors: Shuvozit Ghose, Abhirup Das, Ayan Kumar Bhunia, Partha Pratim Roy
conference: Multimedia Tools and Applications
year: 2020
bibkey: ghose2017fractional
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.00187'}]
tags: [Image Retrieval, Evaluation]
short_authors: Ghose et al.
---
In this paper, a new texture descriptor named "Fractional Local Neighborhood
Intensity Pattern" (FLNIP) has been proposed for content based image retrieval
(CBIR). It is an extension of the Local Neighborhood Intensity Pattern
(LNIP)[1]. FLNIP calculates the relative intensity difference between a
particular pixel and the center pixel of a 3x3 window by considering the
relationship with adjacent neighbors. In this work, the fractional change in
the local neighborhood involving the adjacent neighbors has been calculated
first with respect to one of the eight neighbors of the center pixel of a 3x3
window. Next, the fractional change has been calculated with respect to the
center itself. The two values of fractional change are next compared to
generate a binary bit pattern. Both sign and magnitude information are encoded
in a single descriptor as it deals with the relative change in magnitude in the
adjacent neighborhood i.e., the comparison of the fractional change. The
descriptor is applied on four multi-resolution images -- one being the raw
image and the other three being filtered gaussian images obtained by applying
gaussian filters of different standard deviations on the raw image to signify
the importance of exploring texture information at different resolutions in an
image. The four sets of distances obtained between the query and the target
image are then combined with a genetic algorithm based approach to improve the
retrieval performance by minimizing the distance between similar class images.
The performance of the method has been tested for image retrieval on four
popular databases. The precision and recall values observed on these databases
have been compared with recent state-of-art local patterns. The proposed method
has shown a significant improvement over many other existing methods.