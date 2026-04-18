# =========================
# 🔧 MODEL PATHS
# =========================
YOLO_MODEL_PATH = "/Users/tejasy/Documents/rv uni hack/my_model/weights/best.pt"
LSTM_MODEL_PATH = "/Users/tejasy/Documents/rv uni hack/lstm_model.pth"
RL_MODEL_PATH   = "/Users/tejasy/Documents/webots_project/controllers/my_controller/rl_model.pth"

# =========================
# IMPORTS
# =========================
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import cv2
from collections import deque
from vehicle import Driver
from ultralytics import YOLO

print("🔄 Loading models...")

yolo = YOLO(YOLO_MODEL_PATH)

class LSTMModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(4, 128, 2, batch_first=True)
        self.fc = nn.Linear(128, 2)

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])

lstm = LSTMModel()
lstm.load_state_dict(torch.load(LSTM_MODEL_PATH))
lstm.eval()

class DQN(nn.Module):
    def __init__(self, n_obs, n_actions):
        super().__init__()
        self.fc1 = nn.Linear(n_obs, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, n_actions)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return self.fc3(x)

ACTIONS = np.array([-0.12, -0.06, -0.02, 0.0, 0.02, 0.06, 0.12])

policy = DQN(3, len(ACTIONS))
policy.load_state_dict(torch.load(RL_MODEL_PATH))
policy.eval()

print("✅ Models Loaded")

driver = Driver()
timestep = int(driver.getBasicTimeStep())

camera = driver.getDevice("camera")
camera.enable(timestep)

gps = driver.getDevice("gps")
gps.enable(timestep)

width = camera.getWidth()
height = camera.getHeight()

driver.setGear(1)

# ⚡ SPEED DOUBLED AGAIN
MAX_SPEED = 48.0

speed = 20.0
steering = 0.0

REVERSE_TIME = int(3000 / timestep)
TURN_TIME = int(1500 / timestep)

recovery_mode = False
recovery_timer = 0
escape_dir = 1
recovery_cooldown = 0

last_positions = []
stuck_counter = 0

track_history = deque(maxlen=20)

def get_lane_offset(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    mask = np.zeros_like(edges)
    mask[int(height * 0.5):, :] = 255
    edges = cv2.bitwise_and(edges, mask)

    ys, xs = np.where(edges > 0)
    if len(xs) < 100:
        return 0.0

    lane_x = np.average(xs, weights=ys)
    return (lane_x - width * 0.5) / (width * 0.5)

print("🚀 ULTRA FAST MODE")

while driver.step() != -1:

    if recovery_cooldown > 0:
        recovery_cooldown -= 1

    if recovery_mode:
        recovery_timer -= 1

        if recovery_timer > TURN_TIME:
            driver.setCruisingSpeed(-12.0)
            driver.setSteeringAngle(0.0)

        elif recovery_timer > 0:
            driver.setCruisingSpeed(20.0)
            driver.setSteeringAngle(0.6 * escape_dir)

        else:
            recovery_mode = False
            recovery_cooldown = 80
            print("✅ EXIT RECOVERY")

        continue

    image = camera.getImage()
    img = np.frombuffer(image, np.uint8).reshape((height, width, 4))[:, :, :3]

    results = yolo(img, verbose=False)[0]
    collision = 0

    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
        cx = (x1 + x2) / 2
        cy = (y1 + y2) / 2
        track_history.append((cx, cy))

        if len(track_history) >= 5:
            seq = []
            for i in range(-5, 0):
                x, y = track_history[i]
                if i > -5:
                    px, py = track_history[i-1]
                    vx, vy = x - px, y - py
                else:
                    vx, vy = 0, 0
                seq.append([x, y, vx, vy])

            seq = torch.tensor(seq, dtype=torch.float32).unsqueeze(0)

            with torch.no_grad():
                pred = lstm(seq).numpy()[0]

            if abs(pred[0] - width/2) < 60 and pred[1] > height * 0.6:
                collision = 1

    offset = get_lane_offset(img)

    target_steer = -offset * 0.9
    if abs(offset) > 0.3:
        target_steer *= 2.2

    steering = 0.6 * steering + 0.4 * target_steer

    # ⚡ SPEED DOUBLED AGAIN
    if collision:
        speed = 20.0
    elif abs(offset) > 0.4:
        speed = 20.0
    elif abs(offset) > 0.2:
        speed = 32.0
    else:
        speed = min(speed + 0.4, MAX_SPEED)

    state = torch.tensor([[offset, steering, speed/10.0]], dtype=torch.float32)

    with torch.no_grad():
        action_idx = policy(state).argmax().item()

    rl = ACTIONS[action_idx]
    steering += 0.3 * rl
    steering = max(min(steering, 0.6), -0.6)

    driver.setCruisingSpeed(speed)
    driver.setSteeringAngle(steering)

    pos = gps.getValues()
    last_positions.append(pos)

    if len(last_positions) > 20:
        last_positions.pop(0)

    if len(last_positions) == 20:
        dx = max(p[0] for p in last_positions) - min(p[0] for p in last_positions)
        dz = max(p[2] for p in last_positions) - min(p[2] for p in last_positions)

        movement = dx + dz

        if movement < 0.08 and speed < 3.0 and abs(steering) < 0.05:
            stuck_counter += 1
        else:
            stuck_counter = 0

    if stuck_counter > 8 and recovery_cooldown == 0:
        print("⚠️ REAL STUCK → RECOVERY")
        recovery_mode = True
        recovery_timer = REVERSE_TIME + TURN_TIME
        escape_dir *= -1
        stuck_counter = 0

    direction = "RIGHT ➡️" if rl <0 else "LEFT ⬅️" if rl > 0 else "STRAIGHT ⬆️"

    print(f"Offset:{offset:.2f} | Speed:{speed:.2f} | Steering:{steering:.2f} | RL:{direction} | Collision:{collision}")