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
1. Build the Docker image
   ```bash
   docker build -t apex-performance-app . 
   ```
2. Run the Docker container
   ```bash
   docker run -d --name apa-container -p 3306:3306 \ 
   -e MYSQL_ROOT_PASSWORD=rootpassword \ 
   apex-performance-app
   ```
3. Verify the container is running
   ```bash
   docker ps
   ```
4. Access the container
   ```bash
   docker exec -it apa-container mysql -u root -p
   ```
5. Stop the container
   ```bash
   docker stop apa-container
   ``` 
6. Clean up the container
   ```bash
   docker rm apa-container
   ```
