---
layout: publication
title: 'Tenacious Tagging Of Images Via Mellin Monomials'
authors: Kieran G. Larkin, Peter A. Fletcher, Stephen J. Hardy
conference: "Arxiv"
year: 2012
citations: 2
bibkey: larkin2012tenacious
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1208.5842'}
tags: ['Quantization and Compression', 'ANN Search']
---
We describe a method for attaching persistent metadata to an image. The
method can be interpreted as a template-based blind watermarking scheme, robust
to common editing operations, namely: cropping, rotation, scaling, stretching,
shearing, compression, printing, scanning, noise, and color removal. Robustness
is achieved through the reciprocity of the embedding and detection invariants.
The embedded patterns are real onedimensional Mellin monomial patterns
distributed over two-dimensions. The embedded patterns are scale invariant and
can be directly embedded in an image by simple pixel addition. Detection
achieves rotation and general affine invariance by signal projection using
implicit Radon transformation. Embedded signals contract to one-dimension in
the two-dimensional Fourier polar domain. The real signals are detected by
correlation with complex Mellin monomial templates. Using a unique template of
4 chirp patterns we detect the affine signature with exquisite sensitivity and
moderate security. The practical implementation achieves efficiencies through
fast Fourier transform (FFT) correspondences such as the projection-slice
theorem, the FFT correlation relation, and fast resampling via the chirp-z
transform. The overall method utilizes orthodox spread spectrum patterns for
the payload and performs well in terms of the classic
robustness-capacity-visibility performance triangle. Tags are entirely
imperceptible with a mean SSIM greater than 0.988 in all cases tested.
Watermarked images survive almost all Stirmark attacks. The method is ideal for
attaching metadata robustly to both digital and analogue images.
