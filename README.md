# timeCounter
A execution tie counter for python

# Getting Started
Download the code from this repo and Place it in your folder

## Docs
> Import <br/>
`from timeCounter.counter import *`

> Creating Object of Counter class<br/>
`cntr = Counter()`

> Starting Counter<br/>
`cntr.start()`

> Marking a intermediate point <br/>
`cntr.mark()`

> Marking a inetrmediate point with Unique Name<br/>
`cntr.mark("Mark Name")` <br/>
Mark Name is a unique name that can be use for identify the mark. If not provided it will autmatically generate and assign it. Try to keep the mark id less than 20 characters

> Stop the counter<br/>
`cntr.end()`

> Show the output<br/>
`cntr.show()`

> Show the output with Intermediate Marks<br/>
`cntr.show(mark=True)`

> Stop the counter with output<br/>
`cntr.end(show=True)`

> Stop the counter with output with Intermediate Marks<br/>
`cntr.end(show=True, mark=True)`
