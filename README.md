# Campus Route Optimization System

## 📌 Overview

The Campus Route Optimization System is a project designed to find the shortest path between locations inside a college campus building.

The system uses graph-based pathfinding (Dijkstra’s Algorithm) to compute optimal routes between rooms, labs, and facilities across multiple floors.

---

## 🎯 Objective

* To solve indoor navigation problems in campus buildings
* To implement shortest path algorithms using Python
* To visualize navigation using a 3D model (Blender)

---

## 🛠️ Technologies Used

* Python (Graph + Dijkstra Algorithm)
* Blender (3D Floor Plan Modeling)
* GLB Export (for 3D visualization)

---

## 🧠 Core Concept

* The campus is modeled as a **graph**
* Each location (room, corridor junction, stairs) is a **node**
* Connections between them are **edges with weights (distance)**
* Dijkstra’s Algorithm is used to find the **shortest path**

---

## 🏗️ Project Structure

* `models/` → Blender files and exported GLB model
* `images/` → Floor plan screenshots (PNG)
* `scripts/` → Python implementation (Dijkstra & graph logic)

---

## 🚀 Features

* Multi-floor navigation support
* Shortest path calculation using Dijkstra Algorithm
* Structured node system (rooms + corridors + stairs)
* 3D modeled campus environment

---

## ⚠️ Limitations

* No live web interface (static project only)
* Navigation visualization not deployed online
* Requires manual execution of Python logic

---

## 🔮 Future Improvements

* Web integration using Three.js
* Interactive UI for selecting source and destination
* Real-time path visualization
* Mobile-friendly navigation system

---

## 👨‍💻 Author

Deva Krishna Jayan
Deril k shaju
Dawn Reji
BTech Computer Science (KTU)
@ Adi shankara college (kalady)

---

## 📌 Note

This project focuses on **algorithm implementation and system design**, not full deployment.
