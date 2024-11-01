---
title: Turing_Completeness
tags: [theory-of-computation, Turing]
created: Friday, September 13, 2024
---

# Turing Completeness
We know that a [Turing machine](Turing_machines.md) is a theoretical construct
of a computer that:

> contains mutable state, executes sequences of simple instructions that read
> and write that state, and can pick different execution paths depending on the
> state (via conditional branch instructions.)

A Turing Complete (TC) system is a system that abides by, or can be reduced to,
the above description.

TC also serves as a _definition of computability_ and provides a formal basis
for conceiving of computation at a theoretical level.

All Turing Complete systems are functionally equivalent. This means they can
simulate each other given enough time and memory. Similarly a TC system can in
principle perform any computation that any other programmable computer can
perform. This is true for _other_ TC systems and also those that are not TC
however the inverse doesn't hold: a non-TC system cannot emulate a TS system.
For instance a calculator cannot do what a TC smart phone can do. But a smart
phone can act as a calculator.

Completeness applies to the hardware of computers as well as their software.

Turing Completeness is the theoretical basis of the practical concept of a
"general-purpose computer": a general-purpose computer is such because it is
TC - it can in theory compute anything that is computable.

Most modern programming languages are Turing Complete in that they can, in
theory, be used to compute anything that is computable.

What about Universal Turing Machines eh?


Within the [hierarchy of the OS](./Basic_model_of_the_operating_system.md), the
kernel acts as the primary mediator between the hardware (CPU, memory) and
[user](./User_Space.md) [processes](Processes.md). Let's look at each of its
responsibilities in greater depth:

