
# Seoul-si Artificial Intelligence Internet of Things Hackerton
___

![image](https://github.com/user-attachments/assets/ef3e50af-bed8-4aa6-830e-b774d2e2f436)


## SafeScape - Detect potential harzards in parks
> **Competition** , **Sep. 2024 ~ Oct. 2024**

---

## Software Stacks
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

---

## Competition Topic

- Developing software to improve convenience in Seoul's parks
- **Our software : SafeScape- Detect potential hazards in parks**
- The competition took place overnight on October 10th and 11th.

---

## Implementation

### 1. Dataset
- [Aging facility images Dataset - AIhub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=166)

### 2. Aging facility object detection
- with [Yolo v7](https://github.com/WongKinYiu/yolov7) , Raspberry Pi, Arduino UNO
- Detecting bounding box for aging facilities and output to user interface.
![image](https://github.com/user-attachments/assets/c4afc303-fa34-4de8-9881-06cf036fc65a)

### 3. Physical Deformation detection
- with Arduino Nano 33 BLE
- Detect physical deformations(falling, bending, breaking) with accelerometers
![image](https://github.com/user-attachments/assets/2311b1f1-8938-4407-ae7f-acdc9c7958a3)


### 4. User Interface Implementation
- Used FastAPI(backend), HTML/JS(frontend) , Google Map API(Marker)
- AIoT device information is updated in real time
![image](https://github.com/user-attachments/assets/9ca93035-2b97-4720-96c8-c9f91ab5f765)

---

## Result & Outputs

- Advance to finals, no Prize (15 teams)
