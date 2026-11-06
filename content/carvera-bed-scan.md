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

My Makera Carvera C1 already knows exactly where its head is. This project
uses that: a line laser and two small global-shutter cameras ride on the head,
and the machine sweeps them across the bed. The laser draws a line on whatever
is below it, and the height of each point shifts the line sideways in the
camera image. Because the machine reports the head's position for every frame,
the frames stitch into one height map of the whole bed, in the machine's own
coordinates.

The 3D view below is the result. Drag to orbit, scroll to zoom, and switch
between the photo-draped surface, the raw point cloud and height colours.

{{< app-embed src="https://carvera.busboom.org/" title="Carvera bed scan, 2026-11-05: 1-2-3 blocks and setup bars" height="640" >}}

## How it works

![Placeholder: the scanning rig](/projects/carvera-bed-scan/rig-placeholder.svg)

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
