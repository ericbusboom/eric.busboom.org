---
title: "CD Robot, Version 1"
date: 2009-07-21T08:08:41+00:00
draft: false
author: "eric"
project: true
summary: "A project to put all of my music online, with a CD-ripping robot, a heavily hacked internet appliance, and a lot of hard drives."
image: "musicjukebox-rev3-oblique-300x225.png"
---

Joining two households into one when I married my wife was a simple affair; she
had all of the dishes, furniture and towels, and I had all of the tools. But,
we both had CDs. Even on the day after our wedding, when our apartment was
clogged with wedding gifts and necessities for our new house, the stack of CDs
towered over it all.

We are proud of the music we have collected, and naturally, we like listening
to it. But storing and protecting it is a complex problem. And there are discs
that we have not listened to in years, because we’ve forgotten we have them.
The emergence of MP3 pointed to a solution, and in 1998 I started planning a
digital music server.

## Ripping robots

{{< fig src="musicjukebox-cdrobot.jpg" float="right" caption="The original sketch: lift CDs from an input stack into a PC’s CD player, then onto an output stack." >}}

The first problem to solve was ripping the discs. I figured that with
diligence, I could manually rip 4 or 5 a day, consigning me to a year of
slavery. Clearly I needed a robot. The original idea, sometime in 1998, was to
lift CDs from one stack into the CD tray in a computer, and after ripping, put
the CD in another tray. Good idea, but I could do better, since I should not
have to open the CD cases myself either. Here begins a several year detour.

The first experiments used a Lynxmotion 5-axis robotic arm. These robot arm
kits use RC servos and a serial servo controller to connect via a serial port
to a computer. This arm was a lot of fun, but it did not have the power
required to remove a CD from a case.

### The vertical axis

{{< fig-row >}}
{{< fig src="musicjukebox-rev1-vert.png" caption="First vertical axis: a garage-door-opener lead screw, with a shower-rod slide." >}}
{{< fig src="musicjukebox-rev2-vert.png" caption="Second version: aluminum C-channel, ¾″ threaded rod and Teflon shim, with the horizontal arm attached." >}}
{{< /fig-row >}}

My second idea was to build a tall CD rack to hold cases. Then a vertical robot
arm would remove each case, open it, remove the CD from the case, and put the
CD into a CD-ROM drive. The vertical axis was initially built from the lead
screw from a garage door opener. The linear slide opposite the lead screw uses
a stainless steel shower rod and six in-line skate wheels, glued side-to-side
in pairs, as bearings. This assembly worked – the carriage moves up and down –
but with the feeble steppers I have it is so slow that I would be better
shuffling CDs about manually.

A later version of the same idea used an entirely custom assembly composed of
aluminum C-channel extrusion, a 3/4” threaded rod, and a bit of Teflon shim
stock. This linear slide is also functional, but slow and underpowered. In this
view, you can see an oblique view of the horizontal arm with the gripper that
grabs the CD case. The gripper is powered by an air cylinder that is connected
to the gripper by a cable.

### The horizontal axis and the case opener

{{< fig src="musicjukebox-rev1-arm.png" caption="The horizontal axis: a linear bearing from a printer and the acme lead screw from a drill-press table." >}}

The horizontal axis of the robot is made from a linear bearing from a printer,
and the acme lead screw from a cheap Chinese drill-press table. Like the other
linear slides, it is functional but slow.

{{< fig src="musicjukebox-opener.png" float="left" caption="The case opener, an exoskeleton that fits around the CD case." >}}

This assembly opens the CD case. This is essentially an exoskeleton that fits
around the CD. Hidden inside are two spring-loaded washers that engage the
slots on the side of the cover of a CD case.

### The disc remover

{{< fig src="musicjukebox-rev1-minirobot.png" float="right" caption="The mini robot that lifts the disc out of the case, built from brass tubing and RC servos." >}}

This smaller robot would remove the CD from the case. It is made from
telescoping brass tubing and RC servos. The end-effector is a two-part hook
that fits in the slots in the rose in the middle of a CD case that engages the
hole in the CD. Each hook on the end effector is attached to a square tube that
has a rack that engages a pinion on a servo. When the pinion gear turns, the
hooks move in opposite directions, either coming together or moving apart.
Although the end-effector is dodgy, the remainder of this mini robot works
surprisingly well.

## The final design

After a year of building bits of the robot and not coming any closer to
assembling the whole, I realized that I was tackling too much. I’d only be
able to finish this project if I abandoned the idea of having the robot open
the case. Within a few hours, I had settled on a design that was functionally
equivalent to my original sketches. In the intervening years between the
original idea and the beginning of actual progress I had learned a lot about
machine shop work, and more importantly, the price of hard drives had dropped
to where I could afford to store all of the data I was about to collect.

{{< fig-row >}}
{{< fig src="musicjukebox-rev3-oblique.png" caption="The final robot: a cylindrical arm with a suction-cup effector." >}}
{{< fig src="musicjukebox-rev3-side.png" caption="Side view. The rotary table is a cast iron timing gear." >}}
{{< /fig-row >}}

The final design is a cylindrical robot with a suction-cup effector. It simply
shuttles CDs from one stack to the CD tray and finally to an output stack.
Nearly all of the parts were salvaged from around the shop. The vertical axis
is built from the horizontal axis on earlier versions. The rotary table is made
from a cast iron timing gear. The vacuum pump is one of several that have been
hiding in dark corners of the shop for years.

If I had bothered to do any time and motion studies, this design would have
been obvious from the start; it takes 20 hours for this robot to rip a stack of
100 CDs, and only a few minutes for me to remove the same CDs from their cases.
With this much effort in the project, I did not ever want to do this again.
So, I saved all of the CD data as WAV and losslessly compressed the files with
FLAC. In the end, it took about a week to rip my entire collection to 250 GB of
hard drive space.

## Playing the music

Of course, music data on a hard drive is not a music server. Now I needed
something to play the CDs. I figured if I had all of the data as WAV files, I
should play them that way – no need to suffer the degradation of MP3
conversion. I just need to hack the SliMP3 server to decompress FLAC and send
the WAV data to the SliMP3 head unit, right? Er, no. The SliMP3 decodes MP3 in
hardware.

Next, I tried to hack an old i-Opener. These failed Internet appliances run
Linux and have USB ports, so I could connect it to the net, use a Stereo-Link
to actually play the music, and use XMMS as a decoder. Even describing the
ordeal exhausts me, so I will quit by saying that none of the guides for
hacking an i-Opener were any help with getting my two devices to boot. By the
time I did load Linux on them, through a combination of unusual hardware,
trial and error and luck, I decided that the SliMP3 sounds fine playing MP3 at
320 kb/s. So, all I have yet to do is pull Ethernet cable to the stereo and I
will be in digital music bliss.
