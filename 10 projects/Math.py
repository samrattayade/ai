import numpy as np

# Scalar example: speed
speed = 60  # km/h
print("Speed (scalar):", speed)

# Vector example: velocity
velocity = np.array([30, 40])  # 30 km/h East, 40 km/h North
print("Velocity (vector):", velocity)

# Magnitude of velocity (overall speed)
magnitude = np.linalg.norm(velocity)
print("Magnitude of velocity:", magnitude)

# Direction of velocity (unit vector)
direction = velocity / magnitude
print("Direction of velocity:", direction)
