---
layout: publication
title: '3D Gaussian Ray Tracing: Fast Tracing Of Particle Scenes'
authors: Nicolas Moenne-Loccoz, Ashkan Mirzaei, Or Perel, Riccardo de Lutio, Janick
  Martinez Esturo, Gavriel State, Sanja Fidler, Nicholas Sharp, Zan Gojcic
conference: ACM Transactions on Graphics
year: 2024
bibkey: moenneloccoz20243d
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.07090'}]
tags: []
short_authors: Moenne-Loccoz et al.
---
Particle-based representations of radiance fields such as 3D Gaussian
Splatting have found great success for reconstructing and re-rendering of
complex scenes. Most existing methods render particles via rasterization,
projecting them to screen space tiles for processing in a sorted order. This
work instead considers ray tracing the particles, building a bounding volume
hierarchy and casting a ray for each pixel using high-performance GPU ray
tracing hardware. To efficiently handle large numbers of semi-transparent
particles, we describe a specialized rendering algorithm which encapsulates
particles with bounding meshes to leverage fast ray-triangle intersections, and
shades batches of intersections in depth-order. The benefits of ray tracing are
well-known in computer graphics: processing incoherent rays for secondary
lighting effects such as shadows and reflections, rendering from
highly-distorted cameras common in robotics, stochastically sampling rays, and
more. With our renderer, this flexibility comes at little cost compared to
rasterization. Experiments demonstrate the speed and accuracy of our approach,
as well as several applications in computer graphics and vision. We further
propose related improvements to the basic Gaussian representation, including a
simple use of generalized kernel functions which significantly reduces particle
hit counts.