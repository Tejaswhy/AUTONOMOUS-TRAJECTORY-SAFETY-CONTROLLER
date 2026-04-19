🚀 Building a Risk-Aware Autonomous Driving System

Autonomous vehicles operate in highly dynamic and uncertain environments, where surrounding traffic, pedestrians, and road obstacles make future trajectory prediction extremely challenging. Even small prediction errors can lead to lane deviation, delayed braking, or collision risks. Traditional systems often struggle with transparency, making it difficult to explain decisions like braking or lane changes.

To address this, I worked on designing a **safe, explainable, and uncertainty-aware trajectory controller** suitable for real-time ADAS deployment. The goal was to ensure collision-aware safety, precise path tracking, and intelligent decision-making under uncertainty.

The system follows a full AI pipeline. It uses Webots for realistic simulation and YOLO for real-time perception of vehicles and obstacles. ByteTrack enables continuous object tracking across frames, while LSTM predicts short-term future motion of surrounding objects. These inputs are combined into a structured state vector including lane offset, speed, steering, and obstacle data. A DQN-based reinforcement learning agent then learns optimal driving actions such as steering, acceleration, and braking. On top of this, a safety control layer ensures stability through reverse recovery, adaptive speed control, and corrective maneuvers.

Compared to traditional approaches, this system introduces major improvements. Instead of basic lane detection, it uses advanced perception for accurate environmental understanding. Tracking is no longer frame-by-frame but continuous, enabling better motion awareness. The system moves from reactive behavior to predictive intelligence using LSTM. Decision-making evolves from fixed rules to adaptive learning through reinforcement learning. All of this is validated in a realistic simulation environment, making it closer to real-world deployment.

The architecture integrates perception, tracking, prediction, and control into a unified pipeline, enabling real-time decision-making with mathematically reliable safety bounds. The system is designed to be scalable, robust, and suitable for safety-critical automotive applications.

Looking ahead, this work can be extended to multi-agent traffic scenarios, real-world ADAS deployment, edge optimization for low latency, and advanced RL algorithms like PPO or DDPG.

This project strengthened my understanding of combining computer vision, sequence modeling, and reinforcement learning into a single intelligent system for autonomous driving.

Would love to hear your thoughts!

