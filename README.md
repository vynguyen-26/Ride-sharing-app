# Ridee - Ride Sharing Application

## Overview

Ridee is an application that enables users to register as either drivers or riders, request or cancel rides, and manage ride operations and notifications through a real-time location tracking system. 

## Core Features

- **User Profiles:** Separate classes for riders and drivers.
- **Ride Management:** Manage ride requests and cancel flow, including ride status and positions.
- **Ride Sharing Platform:** Manage and facilitate rides between riders and drivers.

## The Classes and Their Core Functional Components

### `RideSharing`
This class serves as the main application class, managing riders, drivers, and rides.

- **Attributes:**
  - `riders`: List of registered riders.
  - `drivers`: List of registered drivers.
  - `rides`: List of ongoing completed rides.

### `User`
This class served as a base for both riders' and drivers' classes.

- **Attributes:**
  - `name`: Full name of the user
  - `email`: Email address
  - `phone`: Phone number
  - `current_location (latitude,longitude)`: Real-time location
 
### `Driver`
Extend user functionality with driver-specific attributes

- **Attributes:**
  - `availability_status`: ENUM(online, offline, busy)

- **Functions:**
  - Toggle availability status (online/offline)
  - Receive and accept/decline ride request
  - Navigate pickup and destination locations
  - Confirm rider pickup and trip complement


### `Rider`
Extend user functionality with rider-specific attributes

- **Attributes:**
  - `current_ride_status`: Real-time update of the ride (looking/found driver, est arrival, rider/driver location update)

- **Functions:**
  - Request a ride with pickup/dropoff locations
  - Track driver location in real time
  - Cancel ride request before driver pickup 
 
### `Ride`
This class manages the entire ride lifecycle between rider and driver

- **Attributes:**
  - `pickup/dropoff coordinates`: Location data
  - `ride_status`: ENUM(requested, accepted, started, completed, cancelled)
  - `distance_miles`: Trip distance

## Real-Time Architecture Components

### `Location Tracking System`
- Uses pyqtree to randomize the latitude and longitude for the coordinates of drivers and riders

### `Notification System`
- Multi-channel delivery (push, SMS, email, in-app)
- Real-time ride status updates
- Only send a notification for drivers within the radius and available

### `Matching Algorithm`
- Only match drivers within a certain radius for route optimization
