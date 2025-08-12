---
layout: publication
title: Bitstream-based JPEG Image Encryption With File-size Preserving
authors: Hiroyuki Kobayashi, Hitoshi Kiya
conference: 2018 IEEE 7th Global Conference on Consumer Electronics (GCCE)
year: 2018
bibkey: kobayashi2018bitstream
citations: 39
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.06495'}]
tags: ["Efficiency", "Privacy & Security"]
short_authors: Hiroyuki Kobayashi, Hitoshi Kiya
---
An encryption scheme of JPEG images in the bitstream domain is proposed. The
proposed scheme preserves the JPEG format even after encrypting the images, and
the file size of encrypted images is the exact same as that of the original
JPEG images. Several methods for encrypting JPEG images in the bitstream domain
have been proposed. However, since some marker codes are generated or lost in
the encryption process, the file size of JPEG bitstreams is generally changed
due to the encryption operations. The proposed method inputs JPEG bitstreams
and selectively encrypts the additional bit components of the Huffman code in
the bitstreams. This feature allows us to have encrypted images with the same
data size as that recoded in the image transmission process, when JPEG images
are replaced with the encrypted ones by the hooking, so that the image
transmission are successfully carried out after the hooking.