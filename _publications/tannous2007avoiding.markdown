---
layout: publication
title: Avoiding Rotated Bitboards With Direct Lookup
authors: Tannous Sam
conference: "ICGA Journal Vol."
year: 2007
bibkey: tannous2007avoiding
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/0704.3773"}
tags: []
---
This paper describes an approach for obtaining direct access to the attacked squares of sliding pieces without resorting to rotated bitboards. The technique involves creating four hash tables using the built in hash arrays from an interpreted, high level language. The rank, file, and diagonal occupancy are first isolated by masking the desired portion of the board. The attacked squares are then directly retrieved from the hash tables. Maintaining incrementally updated rotated bitboards becomes unnecessary as does all the updating, mapping and shifting required to access the attacked squares. Finally, rotated bitboard move generation speed is compared with that of the direct hash table lookup method.
