DROP DATABASE IF EXISTS apa_db;
CREATE DATABASE IF NOT EXISTS apa_db;

USE apa_db;

CREATE TABLE IF NOT EXISTS Team (
	team_id INT AUTO_INCREMENT PRIMARY KEY,
	team_name VARCHAR(50),
	total_earnings VARCHAR(50)
);

insert into Team (team_id, team_name, total_earnings) values (1, 'Reinger-Hand', '$67437.59');
insert into Team (team_id, team_name, total_earnings) values (2, 'Kessler-Roberts', '$42898.44');
insert into Team (team_id, team_name, total_earnings) values (3, 'Watsica-Lowe', '$52337.03');
insert into Team (team_id, team_name, total_earnings) values (4, 'Medhurst, Donnelly and Mante', '$56108.27');
insert into Team (team_id, team_name, total_earnings) values (5, 'Predovic-Buckridge', '$36634.09');
insert into Team (team_id, team_name, total_earnings) values (6, 'Grimes-Klocko', '$10569.15');
insert into Team (team_id, team_name, total_earnings) values (7, 'Schiller and Sons', '$72595.35');
insert into Team (team_id, team_name, total_earnings) values (8, 'Jerde LLC', '$42348.74');
insert into Team (team_id, team_name, total_earnings) values (9, 'Witting-Feest', '$78129.40');
insert into Team (team_id, team_name, total_earnings) values (10, 'Kunze-Senger', '$5881.94');
insert into Team (team_id, team_name, total_earnings) values (11, 'Moore-Sawayn', '$54173.28');
insert into Team (team_id, team_name, total_earnings) values (12, 'Romaguera Inc', '$18794.46');
insert into Team (team_id, team_name, total_earnings) values (13, 'Moore, Maggio and Emmerich', '$51421.02');
insert into Team (team_id, team_name, total_earnings) values (14, 'Herzog-Collins', '$72931.69');
insert into Team (team_id, team_name, total_earnings) values (15, 'Sipes, Reichert and Raynor', '$81639.71');
insert into Team (team_id, team_name, total_earnings) values (16, 'Weber-Block', '$15908.80');
insert into Team (team_id, team_name, total_earnings) values (17, 'Larkin-Hegmann', '$94180.11');
insert into Team (team_id, team_name, total_earnings) values (18, 'Hilpert-Mills', '$82280.15');
insert into Team (team_id, team_name, total_earnings) values (19, 'Walker-Keeling', '$67793.24');
insert into Team (team_id, team_name, total_earnings) values (20, 'Veum-Schowalter', '$90564.53');
insert into Team (team_id, team_name, total_earnings) values (21, 'Keebler LLC', '$56235.55');
insert into Team (team_id, team_name, total_earnings) values (22, 'Champlin, Abernathy and Monahan', '$74646.77');
insert into Team (team_id, team_name, total_earnings) values (23, 'Beatty and Sons', '$88747.37');
insert into Team (team_id, team_name, total_earnings) values (24, 'Bergstrom, Murphy and Schumm', '$78761.74');
insert into Team (team_id, team_name, total_earnings) values (25, 'Beier, Reilly and Davis', '$52603.20');
insert into Team (team_id, team_name, total_earnings) values (26, 'Roberts-Luettgen', '$41553.26');
insert into Team (team_id, team_name, total_earnings) values (27, 'Hills Inc', '$41453.29');
insert into Team (team_id, team_name, total_earnings) values (28, 'Lowe-Murazik', '$91783.70');
insert into Team (team_id, team_name, total_earnings) values (29, 'Goldner, Zboncak and Lynch', '$87578.39');
insert into Team (team_id, team_name, total_earnings) values (30, 'Little-Huel', '$23055.31');
insert into Team (team_id, team_name, total_earnings) values (31, 'Mayer Group', '$25195.42');
insert into Team (team_id, team_name, total_earnings) values (32, 'Kling-Baumbach', '$8780.68');
insert into Team (team_id, team_name, total_earnings) values (33, 'Mills, Emmerich and Franecki', '$81465.50');
insert into Team (team_id, team_name, total_earnings) values (34, 'Heathcote-MacGyver', '$81065.45');
insert into Team (team_id, team_name, total_earnings) values (35, 'Runolfsson Group', '$47692.13');

CREATE TABLE IF NOT EXISTS RankTier (
	rank_tier_id INT AUTO_INCREMENT PRIMARY KEY,
	tier_name VARCHAR(8),
	division_name VARCHAR(3),
	min_points INT,
	max_points INT
);
insert into RankTier (rank_tier_id, tier_name, division_name, min_points, max_points) values (1, 'Gold', 'IV', 2000, 2999);
insert into RankTier (rank_tier_id, tier_name, division_name, min_points, max_points) values (2, 'Silver', 'IV', 1000, 1999);
insert into RankTier (rank_tier_id, tier_name, division_name, min_points, max_points) values (3, 'Bronze', 'IV', 0, 999);
insert into RankTier (rank_tier_id, tier_name, division_name, min_points, max_points) values (4, 'Diamond', 'IV', 4000, 4999);
insert into RankTier (rank_tier_id, tier_name, division_name, min_points, max_points) values (5, 'Predator', 'IV', 6000, 999999);
insert into RankTier (rank_tier_id, tier_name, division_name, min_points, max_points) values (6, 'Platinum', 'IV', 3000, 3999);
insert into RankTier (rank_tier_id, tier_name, division_name, min_points, max_points) values (7, 'Master', 'IV', 5000, 5999);

CREATE TABLE IF NOT EXISTS Legend (
  legend_id INT PRIMARY KEY,
  legend_name VARCHAR(50),
  class_type VARCHAR(20)
);

INSERT INTO Legend (legend_id, legend_name, class_type) VALUES
(1,  'Bangalore',  'Assault'),
(2,  'Fuse',       'Assault'),
(3,  'Ash',        'Assault'),
(4,  'Mad Maggie', 'Assault'),
(5,  'Ballistic',  'Assault'),
(6,  'Wraith',     'Skirmisher'),
(7,  'Octane',     'Skirmisher'),
(8,  'Pathfinder', 'Skirmisher'),
(9,  'Horizon',    'Skirmisher'),
(10, 'Valkyrie',   'Skirmisher'),
(11, 'Revenant',   'Skirmisher'),
(12, 'Alter',      'Skirmisher'),
(13, 'Bloodhound', 'Recon'),
(14, 'Crypto',     'Recon'),
(15, 'Seer',       'Recon'),
(16, 'Vantage',    'Recon'),
(17, 'Sparrow',    'Recon'),
(18, 'Lifeline',   'Support'),
(19, 'Gibraltar',  'Support'),
(20, 'Loba',       'Support'),
(21, 'Newcastle',  'Support'),
(22, 'Conduit',    'Support'),
(23, 'Caustic',    'Controller'),
(24, 'Wattson',    'Controller'),
(25, 'Rampart',    'Controller'),
(26, 'Catalyst',   'Controller'),
(27, 'Mirage',     'Controller');

CREATE TABLE DataSource (
   source_id INT PRIMARY KEY,
   source_name VARCHAR(255),
   source_type VARCHAR(100),
   api_endpoint VARCHAR(255),
   status VARCHAR(50),
   added_date DATE
);

CREATE TABLE Weapon (
   weapon_id INT PRIMARY KEY,
   weapon_name VARCHAR(100),
   weapon_type VARCHAR(100),
   ammo_type VARCHAR(100)
);


CREATE TABLE MapLocation (
   location_id INT PRIMARY KEY,
   map_name VARCHAR(100),
   location_name VARCHAR(100),
   x_coord FLOAT,
   y_coord FLOAT
);


CREATE TABLE Player (
   player_id INT PRIMARY KEY,
   username VARCHAR(100),
   region VARCHAR(100),
   join_date DATE,
   current_rank VARCHAR(100),
   current_rank_points INT,
   current_rank_position INT,
   total_matches INT,
   current_win_rate DECIMAL(5,2),
   overall_accuracy DECIMAL(5,2),
   team_id INT,
   rank_tier_id INT,
   created_at DATE,
   updated_at DATE,
   FOREIGN KEY (team_id) REFERENCES Team(team_id),
   FOREIGN KEY (rank_tier_id) REFERENCES RankTier(rank_tier_id)
);


CREATE TABLE ImportBatch (
   batch_id INT PRIMARY KEY,
   source_id INT,
   import_date DATE,
   records_imported INT,
   import_status VARCHAR(50),
   FOREIGN KEY (source_id) REFERENCES DataSource(source_id)
);


CREATE TABLE `Match` (
   match_id INT PRIMARY KEY,
   match_date DATE,
   season_name VARCHAR(100),
   map_name VARCHAR(100),
   mode VARCHAR(100),
   match_duration INT,
   tournament_name VARCHAR(255),
   source_id INT,
   FOREIGN KEY (source_id) REFERENCES DataSource(source_id)
);


CREATE TABLE PlayerMatchPerformance (
   performance_id INT PRIMARY KEY,
   player_id INT,
   match_id INT,
   legend_id INT NULL,
   death_location_id INT NULL,
   weapon_id INT NULL,
   kills INT,
   deaths INT,
   assists INT,
   damage FLOAT,
   win_flag BOOLEAN,
   accuracy_pct DECIMAL(5,2),
   placement INT,
   knockdowns INT,
   survival_time INT,
   rank_points_change INT,
   is_included_in_analysis BOOLEAN,
   is_active BOOLEAN,
   FOREIGN KEY (player_id) REFERENCES Player(player_id),
   FOREIGN KEY (match_id) REFERENCES `Match`(match_id),
   FOREIGN KEY (legend_id) REFERENCES Legend(legend_id),
   FOREIGN KEY (death_location_id) REFERENCES MapLocation(location_id),
   FOREIGN KEY (weapon_id) REFERENCES Weapon(weapon_id)
);


CREATE TABLE PlayerWeaponPerformance (
   player_weapon_perf_id INT PRIMARY KEY,
   player_id INT,
   weapon_id INT,
   matches_used INT,
   total_kills INT,
   avg_damage DECIMAL(8,2),
   avg_accuracy_pct DECIMAL(5,2),
   avg_damage_per_match DECIMAL(8,2),
   usage_rate DECIMAL(5,2),
   kd_ratio DECIMAL(6,2),
   FOREIGN KEY (player_id) REFERENCES Player(player_id),
   FOREIGN KEY (weapon_id) REFERENCES Weapon(weapon_id)
);


CREATE TABLE PlayerLegendPerformance (
   player_legend_perf_id INT PRIMARY KEY,
   player_id INT,
   legend_id INT,
   matches_played INT,
   wins INT,
   win_rate DECIMAL(5,2),
   avg_damage DECIMAL(8,2),
   kd_ratio DECIMAL(6,2),
   FOREIGN KEY (player_id) REFERENCES Player(player_id),
   FOREIGN KEY (legend_id) REFERENCES Legend(legend_id)
);


CREATE TABLE TeamComposition (
   composition_id INT PRIMARY KEY,
   match_id INT,
   team_id INT,
   legend_1 INT,
   legend_2 INT,
   legend_3 INT,
   FOREIGN KEY (match_id) REFERENCES `Match`(match_id),
   FOREIGN KEY (team_id) REFERENCES Team(team_id),
   FOREIGN KEY (legend_1) REFERENCES Legend(legend_id),
   FOREIGN KEY (legend_2) REFERENCES Legend(legend_id),
   FOREIGN KEY (legend_3) REFERENCES Legend(legend_id)
);


CREATE TABLE MetaTrend (
   meta_trend_id INT PRIMARY KEY,
   season_name VARCHAR(100),
   patch_version VARCHAR(50),
   weapon_id INT NULL,
   legend_id INT NULL,
   usage_rate DECIMAL(5,2),
   win_rate DECIMAL(5,2),
   pick_rate DECIMAL(5,2),
   trend_date DATE,
   FOREIGN KEY (weapon_id) REFERENCES Weapon(weapon_id),
   FOREIGN KEY (legend_id) REFERENCES Legend(legend_id)
);


CREATE TABLE GameEvent (
   event_id INT PRIMARY KEY,
   event_name VARCHAR(255),
   event_type VARCHAR(100),
   start_date DATE,
   end_date DATE,
   description VARCHAR(255)
);


CREATE TABLE Notification (
   notification_id INT PRIMARY KEY,
   player_id INT,
   event_id INT,
   notification_type VARCHAR(100),
   sent_date DATE,
   read_status BOOLEAN,
   FOREIGN KEY (player_id) REFERENCES Player(player_id),
   FOREIGN KEY (event_id) REFERENCES GameEvent(event_id)
);


CREATE TABLE Goal (
   goal_id INT PRIMARY KEY,
   player_id INT,
   goal_type VARCHAR(100),
   target_value INT,
   current_value INT,
   start_date DATE,
   end_date DATE,
   goal_status VARCHAR(50),
   FOREIGN KEY (player_id) REFERENCES Player(player_id)
);


CREATE TABLE TrackedStatEntry (
   stat_entry_id INT PRIMARY KEY,
   player_id INT,
   stat_type VARCHAR(100),
   stat_value DECIMAL(8,2),
   recorded_date DATE,
   is_visible BOOLEAN,
   FOREIGN KEY (player_id) REFERENCES Player(player_id)
);


CREATE TABLE AuditFlag (
   audit_flag_id INT PRIMARY KEY,
   performance_id INT,
   flag_type VARCHAR(100),
   flag_reason VARCHAR(255),
   flag_date DATE,
   review_status VARCHAR(50),
   FOREIGN KEY (performance_id) REFERENCES PlayerMatchPerformance(performance_id)
);


CREATE TABLE ArchivedMatch (
   archived_match_id INT AUTO_INCREMENT PRIMARY KEY,
   original_match_id INT,
   season_name VARCHAR(100),
   match_date DATE,
   archived_date DATE
);


CREATE TABLE ArchivedPerformance (
   archived_performance_id INT PRIMARY KEY,
   original_performance_id INT,
   archived_match_id INT,
   player_id INT,
   kills INT,
   assists INT,
   damage FLOAT,
   accuracy_pct DECIMAL(5,2),
   placement INT,
   FOREIGN KEY (archived_match_id) REFERENCES ArchivedMatch(archived_match_id)
);


CREATE TABLE SystemReport (
   report_id INT PRIMARY KEY,
   report_type VARCHAR(100),
   generated_date DATE,
   report_scope VARCHAR(255),
   created_by VARCHAR(100),
   output_format VARCHAR(50)
);

