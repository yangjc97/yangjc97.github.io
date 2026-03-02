---
title: "Efficient lattice field theory simulation using adaptive normalizing flow on a resistive memory-based neural differential equation solver"
collection: publications
category: manuscripts
permalink: /publication/1-NC-flow
date: 2025-09-16
venue: 'Under Review'
excerpt: 'Meng Xu†, <b>Jichang Yang†</b>, Ning Lin, Qundao Xu, Siqi Tang, Han Wang, Xiaojuan Qi, Zhongrui Wang, Ming Xu'
paperurl: 'https://arxiv.org/abs/2509.12812'
---

Lattice field theory (LFT) simulations underpin advances in classical statistical mechanics and quantum field theory, providing a unified computational framework across particle, nuclear, and condensed matter physics. However, the application of these methods to high-dimensional systems remains severely constrained by several challenges, including the prohibitive computational cost and limited parallelizability of conventional sampling algorithms such as hybrid Monte Carlo (HMC), the substantial training expense associated with traditional normalizing flow models, and the inherent energy inefficiency of digital hardware architectures. Here, we introduce a software-hardware co-design that integrates an adaptive normalizing flow (ANF) model with a resistive memory-based neural differential equation solver, enabling efficient generation of LFT configurations. Software-wise, ANF enables efficient parallel generation of statistically independent configurations, thereby reducing computational costs, while low-rank adaptation (LoRA) allows cost-effective fine-tuning across diverse simulation parameters. Hardware-wise, in-memory computing with resistive memory substantially enhances both parallelism and energy efficiency. We validate our approach on the scalar phi4 theory and the effective field theory of graphene wires, using a hybrid analog-digital neural differential equation solver equipped with a 180 nm resistive memory in-memory computing macro. Our co-design enables low-cost computation, achieving approximately 8.2-fold and 13.9-fold reductions in integrated autocorrelation time over HMC, while requiring fine-tuning of less than 8% of the weights via LoRA. Compared to state-of-the-art GPUs, our co-design achieves up to approximately 16.1- and 17.0-fold speedups for the two tasks, as well as 73.7- and 138.0-fold improvements in energy efficiency.
