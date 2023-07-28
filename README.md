# timeCounter
A execution tie counter for python

# Getting Started
Download the code from this repo and Place it in your folder

# Docs
## Import 
from timeCounter.counter import *

## Creating Object of Counter class
cntr = Counter()

## Starting Counter
cntr.start()

## Marking a intermediate point 
cntr.mark()

## Marking a inetrmediate point with Unique Name
cntr.mark("Mark Name")
Mark Name is a unique name that can be use for identify the mark. If not provided it will autmatically generate and assign it. Try to keep the mark id less than 20 characters

## Stop the counter
cntr.end()

## Show the output
cntr.show()

## Show the output with Intermediate Marks
cntr.show(mark=True)

## Stop the counter with output
cntr.end(show=True)

## Stop the counter with output with Intermediate Marks
cntr.end(show=True, mark=True)
