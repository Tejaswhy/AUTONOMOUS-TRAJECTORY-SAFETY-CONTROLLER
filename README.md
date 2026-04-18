Autonomous Driving System (Webots + AI)
Overview
This project presents a real-time autonomous driving system developed in the Webots simulation environment using Python.
The system focuses on achieving stable lane following and reliable obstacle avoidance through a combination of computer vision and control logic.
A front-facing camera is used as the primary sensor to perceive the environment, making the system lightweight and adaptable.
The approach emphasizes simplicity, robustness, and real-time performance rather than heavy end-to-end learning, ensuring predictable behavior.
The controller continuously processes visual input, extracts meaningful features, and translates them into steering and speed commands.
The design follows a modular pipeline, making it easy to extend with advanced AI techniques such as reinforcement learning or trajectory prediction.
Core Objectives
To build a stable lane-following system that keeps the vehicle centered on the road.
To ensure smooth steering without abrupt oscillations or overcorrection.
To dynamically adjust speed based on road conditions for safety and efficiency.
To detect obstacles in real time and prevent collisions using a safety override mechanism.
To maintain continuous operation without the vehicle getting stuck or deviating significantly from the lane.
Perception System
Camera-Based Input
The system relies on a forward-facing camera mounted on the vehicle.
Each simulation step captures an image frame representing the vehicle’s current view.
This frame acts as the primary input for both lane detection and object detection modules.
Lane Detection Using OpenCV
The captured image is first converted to grayscale to reduce computational complexity.
Gaussian blurring is applied to remove noise and smooth the image.
Canny edge detection is used to highlight lane boundaries and significant edges.
A region of interest is defined, focusing on the lower half of the image where the road is most visible.
This reduces unnecessary processing and improves detection accuracy.
Edge pixels are extracted, and their coordinates are analyzed.
A weighted average of pixel positions is computed, giving more importance to pixels closer to the vehicle.
This results in an estimated lane center position.
The difference between the lane center and the image center gives the lane offset.
Lane Offset Interpretation
A positive offset indicates deviation to one side, while a negative offset indicates the opposite direction.
The magnitude of the offset reflects how far the vehicle is from the center of the lane.
This offset is the key input for steering control.
Control System
Steering Control
Steering is calculated using a proportional control approach.
The steering angle is directly proportional to the lane offset.
Larger offsets result in stronger steering corrections.
A smoothing factor is applied to prevent sudden changes in steering.
This helps maintain stable motion and avoids oscillations.
Steering values are clamped within safe limits to prevent unrealistic or unstable behavior.
Speed Control
Speed is dynamically adjusted based on the lane offset.
When the vehicle is well-centered, speed is gradually increased.
When the vehicle deviates significantly, speed is reduced to maintain control.
If lane detection confidence is low, the system slows down to avoid errors.
This adaptive approach ensures stability across different road conditions.
Obstacle Detection
YOLO-Based Detection
The system integrates a YOLO (You Only Look Once) model for real-time object detection.
Each camera frame is passed through the YOLO model to detect objects.
Bounding boxes are generated for detected objects along with confidence scores.
Only objects within a defined forward region are considered relevant.
Collision Detection Logic
The system checks if detected objects lie near the center of the image.
It also verifies whether objects are close to the bottom of the frame, indicating proximity.
If both conditions are satisfied, the system identifies a potential collision.
This acts as a safety trigger for immediate action.
Safety and Recovery Mechanisms
Collision Avoidance
When an obstacle is detected in the vehicle’s path:
The vehicle slows down or stops.
A reverse maneuver is initiated if the obstacle is too close.
Steering is adjusted slightly during reverse to avoid repeated collisions.
This ensures the vehicle does not crash into obstacles or remain stuck.
Lane Loss Handling
If lane detection fails (insufficient edge pixels):
The system reduces speed.
Steering corrections are minimized.
The vehicle attempts to regain lane visibility gradually.
Stuck Detection
The system monitors the vehicle’s position over time using GPS.
If the vehicle shows minimal movement over multiple steps, it is considered stuck.
A recovery sequence is triggered involving reverse and directional steering.
This prevents the vehicle from remaining stationary indefinitely.
System Pipeline
Capture frame from camera sensor
Process image using OpenCV
Detect lane and compute offset
Detect objects using YOLO
Evaluate collision conditions
Apply control logic for speed and steering
Send commands to vehicle actuators
Repeat continuously in real time
Key Features
Real-time perception and control loop
Robust lane detection using classical computer vision
Smooth and stable steering control
Adaptive speed management
Reliable obstacle detection and avoidance
Recovery system for handling failures and edge cases
Modular design enabling easy upgrades
Performance Characteristics
The system runs efficiently in real time within the Webots simulation environment.
Lane following remains stable under normal conditions with minimal oscillations.
Speed adapts effectively to road curvature and visibility.
Obstacle detection is responsive, allowing timely avoidance actions.
Recovery mechanisms ensure continuous operation without manual intervention.
Project Structure
controllers/
Contains the main control script for the vehicle
models/
Stores trained YOLO, LSTM, or RL models
worlds/
Includes Webots simulation world files
requirements.txt
Lists all dependencies required to run the project
README.md
Project documentation
Applications
Autonomous driving simulation and research
Robotics navigation systems
Advanced Driver Assistance Systems (ADAS) prototyping
AI-based control and perception experiments
Academic and educational projects in computer vision and robotics
Limitations
Lane detection relies on edge-based methods, which may fail in poor lighting or complex environments.
The system does not perform full path planning or global navigation.
Object detection is limited to the trained YOLO model’s dataset.
Reinforcement learning is not fully integrated into the control loop in this version.
Future Improvements
Integration of reinforcement learning (DQN, PPO) for adaptive decision-making
Trajectory prediction using LSTM or sequence models
Multi-object tracking using ByteTrack or similar algorithms
Deep learning-based lane segmentation for improved accuracy
Advanced path planning and route optimization
Sensor fusion with LiDAR or radar for enhanced perception
High-speed stability improvements for racing scenarios
Conclusion
This project demonstrates a complete pipeline for autonomous driving using vision-based perception and control.
It successfully combines lane detection, object detection, and control logic into a cohesive system.
The design prioritizes stability, modularity, and real-time performance.
It serves as a strong foundation for further development in autonomous systems, robotics, and AI-based navigation.
