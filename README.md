# Spring 2026 CS 3200 Project - Apex Performance App - Tylor Chen, Ademide Odusanya, Tannop Tangpiroonthum, Deniz Kalkandelen 

## Overview

We are building an app that will track pro players and the matches that they play in(pro or competitive) in Apex Legends. This app is meant to track several aspects of what makes the pro scene in Apex Legends, which includes, but is not limited to:
 - Strategies
 - Team Compositions
 - Weapons
 - Viability rankings

While many tracker apps already aim to track player performance in ranked and unranked games, there aren't any trackers that effectively track professional matches and the performance of players playing in them. Since professional matches are naturally more competitive, the data from those matches should be more effective at indicating patterns in an ever changing meta, while also being able to indicate emerging trends. 

This tool is intended for:
 - Competitive Analysts
 - Coaches and Team Staff
 - Aspiring players
 - Esports Researchers

The app also features an audit system that notices unusual trends in player data, such as abnormally high accuracy, kill spikes, etc, which could interfere with data reliability and quality. This ensures that data will effectively reflect the state of the game with integrity. 

## Key Features of this tool:

**Player Match Tracking** - 
Performance metrics are stored for players per match, which include:
 - Kill/Death/Assist ratios
 - Damage dealt
 - Player Weapon Accuracy Percentage
 - Survival Time and Player Placements
 - Rank Point Changes

**Pro Match Tracking** - 
Each pro match performance includes:
 - Match Data
 - Selected Legend
 - Weapon Usage
 - Death Location

**Audit System** - 
The audit system flags suspicious performance, such as:
 - Abnormally high damage
 - Kill spikes inconsistent with regular match context
 - Abnormally high accuracy
 - Any other outliers compared to a baseline performance

Each flagged performance also includes:
 - Flag type
 - Reason for flag
 - Review Status
 - Timestamp

**Tech Stack** - 
| Category   | Technology        |
|------------|-------------------|
| Frontend   | Streamlit UI      |
| Backend    | Flask (REST API, Python)  |
| Database   | MySQL (RDBMS) |
| Deployment | Docker, GitHub Actions |


## Instructions on how to start Docker container

**Prerequisites**:
 - Docker installed and running (refer to https://www.docker.com/get-started if not)

**Instructions**: 
## How to Run the App

### Prerequisites
- Docker Desktop installed and running (https://www.docker.com/get-started)
- GitHub Desktop or Git installed

### Setup Instructions

1. **Clone the repository**
   - Open GitHub Desktop → File → Clone Repository
   - URL: `https://github.com/nbpolar/26S-Apex-Performance-App`

2. **Create the `.env` file**
   - Navigate to the `api/` folder in the cloned repo
   - Copy `.env.template` and rename the copy to `.env`
   - Open `.env` and update the following:
     - Change `DB_NAME=ngo_db` to `DB_NAME=apa_db`
     - Replace `<change-this-to-a-strong-password>` with any password (e.g. `password123`)
     - Replace `<change-this-to-a-random-secret>` with any string (e.g. `mysecretkey123`)

3. **Open a terminal in the project folder**
   - In GitHub Desktop: Repository → Open in Command Prompt

4. **Start all containers**
```bash
   docker compose up 
   - note: if the mysql_db container isn't available when checking the status through the command 'docker ps',
   go into docker desktop and manually enable the db container
```

5. **Open the app in your browser**
   - Streamlit UI: http://localhost:8501
   - Flask API: http://localhost:4000

6. **To stop the containers**
```bash
   docker compose down
```

7. **If you make changes to the database files, recreate the DB container**
```bash
   docker compose down db -v && docker compose up 
```
