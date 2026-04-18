.
This project implements a real-time autonomous driving system in the Webots simulation environment using computer vision and control logic. The goal is to enable a vehicle to drive autonomously by following road lanes and avoiding obstacles using only camera input.
2.
The system relies on a front-facing camera that continuously captures frames of the environment. These frames are processed in real time to extract useful information such as lane position and nearby obstacles, forming the foundation of the perception system.
3.
Lane detection is performed using OpenCV techniques. The captured image is converted to grayscale, blurred to reduce noise, and processed using edge detection. By focusing on the lower half of the image, the system isolates the road region for accurate lane analysis.
4.
From the detected edges, the system computes a weighted average of pixel positions to estimate the lane center. The difference between the lane center and the image center gives the lane offset, which indicates how far the vehicle has deviated from the center of the lane.
5.
Steering control is based on this lane offset using a proportional control strategy. The system applies smooth corrections to the steering angle, ensuring gradual adjustments that prevent sudden or unstable movements during driving.
6.
Speed control is dynamically adjusted based on road conditions. The vehicle accelerates on straight paths and slows down when navigating curves or when lane detection confidence is low, improving overall stability and control.
7.
For obstacle detection, the system integrates a YOLO model that identifies objects in real time. The model processes each frame and detects objects in the vehicle’s forward path, allowing the system to recognize potential hazards.
8.
When an obstacle is detected close to the vehicle, a safety mechanism is triggered. The system slows down or reverses while adjusting steering to avoid collisions, ensuring safe navigation even in dynamic environments.
9.
A recovery mechanism is implemented to handle failure cases such as lane loss or the vehicle getting stuck. The system detects lack of movement and initiates corrective actions like reversing and turning to regain proper orientation.
10.
Overall, the system combines perception, decision-making, and control into a continuous loop that enables stable and reliable autonomous driving. Its modular design allows easy integration of advanced techniques such as reinforcement learning, trajectory prediction, and multi-object tracking for future improvements.
