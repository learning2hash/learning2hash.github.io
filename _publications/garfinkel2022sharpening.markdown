---
layout: publication
title: 'Sharpening Your Tools: Updating Bulk_extractor For The 2020s'
authors: Simson Garfinkel, Jonathan Stewart
conference: Arxiv
year: 2022
bibkey: garfinkel2022sharpening
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.01639'}]
tags: ["Tools & Libraries"]
short_authors: Simson Garfinkel, Jonathan Stewart
---
Bulk_extractor is a high-performance digital forensics tool written in C++.
Between 2018 and 2022 we updated the program from C++98 to C++17, performed a
complete code refactoring, and adopted a unit test framework. The new version
typically runs with 75% more throughput than the previous version, which we
attribute to improved multithreading. We provide lessons and recommendations
for other digital forensics tool maintainers.