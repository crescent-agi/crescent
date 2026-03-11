Updated clamping thresholds with tighter bounds to handle extreme inputs:
```python
# New clamping logic
if activation > 100:
    activation = 100
elif activation < -100:
    activation = -100
return activation
```