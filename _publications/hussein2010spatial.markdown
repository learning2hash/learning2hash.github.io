---
layout: publication
title: Spatial Domain Watermarking Scheme For Colored Images Based On Log-average
  Luminance
authors: Jamal A. Hussein
conference: Journal of Computing Vol. 2 Issue 1 January 2010
year: 2010
bibkey: hussein2010spatial
citations: 40
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1001.3496'}]
tags: []
short_authors: Jamal A. Hussein
---
In this paper a new watermarking scheme is presented based on log-average
luminance. A colored-image is divided into blocks after converting the RGB
colored image to YCbCr color space. A monochrome image of 1024 bytes is used as
the watermark. To embed the watermark, 16 blocks of size 8X8 are selected and
used to embed the watermark image into the original image. The selected blocks
are chosen spirally (beginning form the center of the image) among the blocks
that have log-average luminance higher than or equal the log-average luminance
of the entire image. Each byte of the monochrome watermark is added by updating
a luminance value of a pixel of the image. If the byte of the watermark image
represented white color (255) a value <alpha> is added to the image pixel
luminance value, if it is black (0) the <alpha> is subtracted from the
luminance value. To extract the watermark, the selected blocks are chosen as
the above, if the difference between the luminance value of the watermarked
image pixel and the original image pixel is greater than 0, the watermark pixel
is supposed to be white, otherwise it supposed to be black. Experimental
results show that the proposed scheme is efficient against changing the
watermarked image to grayscale, image cropping, and JPEG compression.