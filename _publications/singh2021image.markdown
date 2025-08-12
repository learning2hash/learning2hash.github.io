---
layout: publication
title: An Image Forensic Technique Based On JPEG Ghosts
authors: Divakar Singh
conference: Multimedia Tools and Applications
year: 2022
bibkey: singh2021image
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.06439'}]
tags: []
short_authors: Divakar Singh
---
The unprecedented growth in the easy availability of photo-editing tools has
endangered the power of digital images.An image was supposed to be worth more
than a thousand words,but now this can be said only if it can be authenticated
orthe integrity of the image can be proved to be intact. In thispaper, we
propose a digital image forensic technique for JPEG images. It can detect any
forgery in the image if the forged portion called a ghost image is having a
compression quality different from that of the cover image. It is based on
resaving the JPEG image at different JPEG qualities, and the detection of the
forged portion is maximum when it is saved at the same JPEG quality as the
cover image. Also, we can precisely predictthe JPEG quality of the cover image
by analyzing the similarity using Structural Similarity Index Measure (SSIM) or
the energyof the images. The first maxima in SSIM or the first minima inenergy
correspond to the cover image JPEG quality. We created adataset for varying
JPEG compression qualities of the ghost and the cover images and validated the
scalability of the experimental results.We also, experimented with varied
attack scenarios, e.g. high-quality ghost image embedded in low quality of
cover image,low-quality ghost image embedded in high-quality of cover image,and
ghost image and cover image both at the same quality.The proposed method is
able to localize the tampered portions accurately even for forgeries as small
as 10x10 sized pixel blocks.Our technique is also robust against other attack
scenarios like copy-move forgery, inserting text into image, rescaling
(zoom-out/zoom-in) ghost image and then pasting on cover image.