---
layout: publication
title: 'Xcloth: Extracting Template-free Textured 3D Clothes From A Monocular Image'
authors: Astitva Srivastava, Chandradeep Pokhariya, Sai Sagar Jinka, Avinash Sharma
conference: Arxiv
year: 2022
bibkey: srivastava2022xcloth
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.12934'}]
tags: []
short_authors: Srivastava et al.
---
Existing approaches for 3D garment reconstruction either assume a predefined
template for the garment geometry (restricting them to fixed clothing styles)
or yield vertex colored meshes (lacking high-frequency textural details). Our
novel framework co-learns geometric and semantic information of garment surface
from the input monocular image for template-free textured 3D garment
digitization. More specifically, we propose to extend PeeledHuman
representation to predict the pixel-aligned, layered depth and semantic maps to
extract 3D garments. The layered representation is further exploited to UV
parametrize the arbitrary surface of the extracted garment without any human
intervention to form a UV atlas. The texture is then imparted on the UV atlas
in a hybrid fashion by first projecting pixels from the input image to UV space
for the visible region, followed by inpainting the occluded regions. Thus, we
are able to digitize arbitrarily loose clothing styles while retaining
high-frequency textural details from a monocular image. We achieve
high-fidelity 3D garment reconstruction results on three publicly available
datasets and generalization on internet images.