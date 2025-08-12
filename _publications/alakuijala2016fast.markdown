---
layout: publication
title: Fast Keyed Hash/pseudo-random Function Using SIMD Multiply And Permute
authors: Jyrki Alakuijala, Bill Cox, Jan Wassenberg
conference: Arxiv
year: 2016
bibkey: alakuijala2016fast
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.06257'}]
tags: ["Hashing Methods"]
short_authors: Jyrki Alakuijala, Bill Cox, Jan Wassenberg
---
HighwayHash is a new pseudo-random function based on SIMD multiply and
permute instructions for thorough and fast hashing. It is 5.2 times as fast as
SipHash for 1 KiB inputs. An open-source implementation is available under a
permissive license. We discuss design choices and provide statistical analysis,
speed measurements and preliminary cryptanalysis. Assuming it withstands
further analysis, strengthened variants may also substantially accelerate file
checksums and stream ciphers.