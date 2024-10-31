---
title: Peer_to_peer_network
tags: [networks]
created: Friday, August 09, 2024
---

# Peer to peer network

A decentralised network model where each participant (peer) acts as both a
client and a server.

Resources are shared directly between peers rather than being coordinated via a
server.

Under a server architecture, multiple requests are made from different hosts for
resources. The server manages this load and is in control of what is being
shared, to whom, and when. With P2P there is no central authority equivalent to
this. Each peer both shares and consumes resources and in this sense is both a
client and a server.

A practical example of this is [torrenting](Torrenting.md) - an applicaton of
P2P technology to file sharing.

## Benefits

- Decentralisation, no central authority, also means no single point of failure.
- Scalable: the network capacity grows with the number of users (contrast
  servers)
- Efficiency: idle resources of peers are put to use
- Improved performance for popular content

## Drawbacks

- Security: potential for malicious peers and content
- Inconsistent availability of resources
