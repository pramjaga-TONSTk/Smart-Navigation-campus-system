# 🚀 Smart Campus Navigation, Facility Monitoring & Resource Analytics (SCN-FMRA)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?logo=fastapi)
![IoT](https://img.shields.io/badge/Technology-IoT-orange)
![Status](https://img.shields.io/badge/Status-Development-yellow)
![License](https://img.shields.io/badge/License-Academic-lightgrey)

## 📌 Abstract

The **Smart Campus Navigation, Facility Monitoring & Resource Analytics (SCN-FMRA)** system is designed to improve the efficiency, usability, and management of modern educational campuses by integrating **Internet of Things (IoT), real-time monitoring, and data analytics**.

Large campuses often face challenges such as difficulty in navigation for students and visitors, lack of real-time monitoring of facilities, and inefficient utilization of available resources. SCN-FMRA addresses these challenges through a unified smart-campus solution.

## 🎯 Objectives

- 🗺️ Provide accurate campus navigation for students, faculty, staff, and visitors.
- 📡 Enable real-time monitoring of classrooms, laboratories, and other facilities.
- 🌡️ Monitor environmental parameters such as temperature, humidity, air quality, and occupancy.
- 📊 Analyze resource usage and identify high-demand facilities.
- ⚡ Reduce unnecessary energy consumption.
- 📈 Support data-driven decision-making for campus administrators.

## 🧩 Main Modules

### 1. 🗺️ Smart Campus Navigation

The navigation module helps users locate important campus facilities such as:

- 🏫 Classrooms
- 🔬 Laboratories
- 🏢 Administrative offices
- 📚 Library
- 🎤 Seminar halls
- 🍴 Cafeteria
- 📍 Other campus facilities

The system provides a route and estimated travel time between selected locations.

### 2. 📡 Facility Monitoring

The facility monitoring module uses IoT sensors to monitor campus conditions in real time.

Possible parameters include:

- 🌡️ Temperature
- 💧 Humidity
- 🌫️ Air quality
- 👥 Occupancy
- 🔧 Facility status

This can help improve comfort, safety, and energy efficiency.

### 3. 📊 Resource Analytics

The resource analytics module analyzes resource usage and provides information such as:

- 🏢 Total rooms
- 👥 Occupied rooms
- 📈 Resource utilization percentage
- 🔥 High-demand resources
- ⏰ Peak occupancy patterns
- 🛠️ Maintenance requirements

These insights can help administrators optimize resource allocation and plan future infrastructure improvements.

### 4. 👨‍🏫 Faculty Monitoring

The system can maintain faculty information including:

- 🆔 Faculty ID
- 👤 Faculty name
- 🏛️ Department
- 📌 Current status
- 📍 Current location

Example statuses include **Available, In Class, and In Meeting**.

## ✨ Features

- 🗺️ Accurate campus navigation
- 👨‍🏫 Faculty status monitoring
- 🏢 Facility monitoring
- 📊 Resource utilization analysis
- 📡 Real-time IoT data collection
- 🔗 REST API backend
- 📖 Interactive API documentation through FastAPI
- 📱 Support for future mobile/web application integration

## 🛠️ Technology Stack

### Backend

- 🐍 Python
- ⚡ FastAPI
- ✅ Pydantic
- 🚀 Uvicorn

### IoT / Embedded Systems

- Arduino UNO
- NodeMCU / ESP8266
- IR Sensor
- Ultrasonic Sensor
- Temperature Sensor
- LDR

### Communication

- 📶 Wi-Fi / ESP8266

### Database / IoT Platforms

- MySQL
- Firebase Realtime Database
- Blynk / Firebase

### User Interface

- 🌐 Web Application
- 📱 Mobile Application

## 🔌 API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Returns the welcome message |
| POST | `/navigation/route` | Calculates a campus route |
| GET | `/faculty/status` | Returns all faculty status information |
| GET | `/faculty/status/{faculty_id}` | Returns faculty information by ID |
| GET | `/analytics/resources` | Returns resource usage analytics |

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/SCN-FMRA.git
cd SCN-FMRA
