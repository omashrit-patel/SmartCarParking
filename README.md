# Smart Parking Simulator

Welcome to the **Smart Parking Simulator**, a Pygame-based interactive simulation of a parking lot, focusing on visualizing slot management and car movements. This README provides an overview, setup instructions, user controls, and highlights the Data Structures and Algorithms (DSA) concepts implemented in the project.

---

## 🚗 Features

- **Animated Car Parking and Leaving** – Cars smoothly enter and leave parking spots with realistic movement sequences.
- **Manual and Auto Modes** – Toggle between manually adding/removing cars and auto simulation.
- **Slot Allocation Visualization** – Clearly defined slots show parking availability and occupancy.
- **Intuitive Start Screen** – Simple and user-friendly interface using Pygame.
- **Pygame-based Animation** – Utilizes Pygame’s graphics, image transformation, and event handling.

---

---

## 🎮 Controls

- **A** – Add a car to the nearest available slot
- **R** – Remove a randomly selected parked car
- **T** – Toggle Auto Mode (automatic car arrivals/departures)
- **SPACE** – Start the simulator from the title screen
- **Close window** – Exit the program

---

## 📚 Data Structures & Algorithms Concepts Used

### 1. 2D Arrays (Lists of Lists)
- **Parking Slot Management**  
The parking lot is represented by:
slots = [[None for _ in range(COLS)] for _ in range(ROWS)]

This allows quick lookups, insertions, and removals.

- **Nearest Free Slot Search**  
Loops through the 2D array (column-wise) to find available spots.

### 2. Class-based Object Management
- **OOP Principles**  
Each car is an instance of the `Car` class with:
- Attributes: position, state, parking slot location
- Methods: `update()` and `draw()`

### 3. State Machine for Car Animation
- **Phased Movement Logic**  
Each car’s movement is controlled by a phase system:
- Driving in
- Adjusting position
- Parking or leaving

### 4. Randomization
- **Car Departure Selection**  
Random choice of which parked car will leave:
random.choice(parked_cars)

### 5. Event-Driven Simulation
- **Pygame Event Queue**  
Handles key presses and quit events to update simulation state in real-time.

---

## 🎨 Pygame Features Used

- **`pygame.display`** – Window creation & rendering
- **`pygame.event`** – Keyboard input & quit handling
- **`pygame.image`** – Loading and scaling images
- **`pygame.draw`** – Drawing parking spots & visuals
- **`pygame.time`** – Frame rate control & timed events
- **`pygame.font`** – Rendering text on the screen

---

## 📸 Screenshots
*(<img width="984" height="521" alt="image" src="https://github.com/user-attachments/assets/0b41b86a-11ef-4b39-9169-c0ed0c540ae8" />
)*

---

## 🔧 Customization

- **Slot Layout** – Change variables:  
`ROWS`, `COLS`, `SLOT_WIDTH`, `SLOT_HEIGHT`
- **Car Image** – Replace `car.png` for different designs.

---

## 📜 License

This project is for educational purposes only.  
Please check the `LICENSE` file for usage terms.

