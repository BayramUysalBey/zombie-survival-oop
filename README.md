# Zombie Survival Simulator 🧟♂️⚔️

![Combat Screenshot](screenshots/combat-screenshot.png)

# Zombie Survival Simulator  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  

## Features
- 5 zombie types with unique abilities
- Score system & weapon randomization
- Performance logging (`@timer` decorator)

## Logging  
Zombie movements are logged to `zombie.log`:  

## How to Run
1. Install requirements:
```bash
pip install -r requirements.txt

## API Documentation 🚀

The Zombie Survival Simulator now includes a basic REST API to track game progress in real-time.

### Endpoints

#### GET `/scores`
**Returns current player stats**  
```json
{
  "player": "string",
  "health": int,
  "score": int,
  "active_zombies": int 
}

