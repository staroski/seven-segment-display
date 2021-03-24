# seven-segment-display
MicroPython implementation for showing numbers on a 7 segment display (common cathode or common anode).

First you need to import the `Display` class from the `seven_segment` module, this way:

```python
from seven_segment import Display
```

Then you can instantiate the `Display` class passing to its constructor the segments GPIOs, this way:

```python
# GPIOs from 0 to 6 correspondo to segments a, b, c, d, e, f, g
display = Display(0, 1, 2, 3, 4, 5, 6)
```

By default it's setup as an **common cathode** display, but you can change it's behavior to **common anode**, with the following method:

```python
display.common_anode()
```

And finally, to show a number, you just call the `show` method passing a number between `0` and `9`, this way:

```python
number = 5
display.show(number)
```
