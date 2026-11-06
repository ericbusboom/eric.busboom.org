---
title: "Carvera Bed Scan"
date: 2026-11-05T12:00:00-08:00
draft: false
url: "/projects/carvera-bed-scan/"
author: "eric"
project: true
summary: "A line laser and two cameras on my Carvera CNC's head turn the machine into a 3D scanner: it measures 1-2-3 blocks and setup bars on the bed to about a tenth of a millimetre."
image: "/projects/carvera-bed-scan/thumb.jpg"
---

<!-- DRAFT text, written from the project notes; pictures marked "placeholder"
are to be replaced with real photos. -->

As I've incorporated AI into more of my workflow, I've gotten to feel the
limitations of the traditional CAD/CAM/Controller process for machining parts,
so I've been looking for ways to automate the process more. This project adds
stereo cameras and a line laser to the Carvera CNC's head, turning the machine
into a 3D scanner for its own bed.The goal is to allow the machine to scan its
bed for stock and have Claude pick the location on the stock for Z axis probing
and cutting. 

The goal is to not use any external software for making metal parts or laser
cuts; I want to be able to just talk to Claude to design a part, review it in a
3D viewer, and send it to the CNC for cutting. I've already got this process for
3D printing, because my printers have a built in camera, so I want to ad those
features to my CNC mill. 


The 3D view below is the result. Drag to orbit, scroll to zoom, and switch
between the photo-draped surface, the raw point cloud and height colours.

{{< app-embed src="https://carvera.busboom.org/" title="Carvera bed scan, 2026-11-05: 1-2-3 blocks and setup bars" height="640" >}}

## How it works

Hardware for the system is a 3D printed mount that holds the cameras and laser
in place on the Carvera CNC's head. These are USB cameras, and the laser has a
USB power tether, and all three connect to a USB hub mounted inside the cabinet. 

<CAD model of the scanning rig>

- **Calibration from known motion.** Before scanning, the head steps up and
  down over bare spoilboard. The machine's Z moves give the true distance for
  each laser-line position, so the camera needs no separate calibration target.
- **A cross of two laser lines at 45°** reaches surfaces that one line would
  miss in shadow, and two cameras see each line from different sides.
- **Sweeps.** The head makes continuous passes over the bed, a quarter of a
  millimetre per frame, with the work light off so the line stays crisp.
- **Merge and clean.** Every camera and laser arm makes its own point cloud;
  these are merged (23 million points), checked against each other, and
  gridded into a 0.5 mm surface. A photo mosaic from the same cameras is
  draped over it.

![Photo mosaic of the bed from the scanning cameras](/projects/carvera-bed-scan/ortho.jpg)

## How accurate is it?

The test pieces are a set of 1-2-3 blocks and parallel setup bars, all with
known sizes. Measured height above the spoilboard against the size on the
label:

| Piece | Label | Measured | Error |
|---|---|---|---|
| 3" block | 76.20 mm | 76.14 mm | −0.06 mm |
| 2" block | 50.80 mm | 50.71 mm | −0.09 mm |
| 1" block | 25.40 mm | 25.26 mm | −0.14 mm |
| 1/2" bar | 12.70 mm | 12.83 mm | +0.13 mm |
| 1/4" bar | 6.35 mm | 6.36 mm | +0.01 mm |
| 3/16" bar | 4.76 mm | 4.80 mm | +0.04 mm |
| 1/8" bar | 3.17 mm | 3.29 mm | +0.11 mm |
| 5/32" bar | 3.97 mm | 4.23 mm | +0.26 mm |
| 3/32" bar | 2.38 mm | 2.54 mm | +0.16 mm |
| 1/16" bar | 1.59 mm | 1.88 mm | +0.30 mm |

The blocks and the thicker bars come in within about 0.15 mm. The thin bars
read high, probably because they were not lying quite flat on the bed.

![Height map of the bed with each piece labelled, measured against nominal](/projects/carvera-bed-scan/relief.jpg)

## What's next

Turning the scripts into a package that runs the whole scan from the
machine, and using the scans to find and measure stock before cutting.
