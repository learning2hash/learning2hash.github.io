---
layout: publication
title: Number Parsing At A Gigabyte Per Second
authors: Daniel Lemire
conference: 'Software: Practice and Experience'
year: 2021
bibkey: lemire2021number
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.11408'}]
tags: []
short_authors: Daniel Lemire
---
With disks and networks providing gigabytes per second, parsing decimal
numbers from strings becomes a bottleneck. We consider the problem of parsing
decimal numbers to the nearest binary floating-point value. The general problem
requires variable-precision arithmetic. However, we need at most 17 digits to
represent 64-bit standard floating-point numbers (IEEE 754). Thus we can
represent the decimal significand with a single 64-bit word. By combining the
significand and precomputed tables, we can compute the nearest floating-point
number using as few as one or two 64-bit multiplications. Our implementation
can be several times faster than conventional functions present in standard C
libraries on modern 64-bit systems (Intel, AMD, ARM and POWER9). Our work is
available as open source software used by major systems such as Apache Arrow
and Yandex ClickHouse. The Go standard library has adopted a version of our
approach.