DROP DATABASE IF EXISTS apa_db;
CREATE DATABASE IF NOT EXISTS apa_db;

USE apa_db;

CREATE TABLE IF NOT EXISTS Team (
	team_id INT AUTO_INCREMENT PRIMARY KEY,
	team_name VARCHAR(50),
	total_earnings VARCHAR(50)
);

insert into Team (team_id, team_name, total_earnings) values (1, 'TSM', '$67437.59');
insert into Team (team_id, team_name, total_earnings) values (2, 'NRG', '$42898.44');
insert into Team (team_id, team_name, total_earnings) values (3, 'Alliance', '$52337.03');
insert into Team (team_id, team_name, total_earnings) values (4, 'Team Liquid', '$56108.27');
insert into Team (team_id, team_name, total_earnings) values (5, 'Sentinels', '$36634.09');
insert into Team (team_id, team_name, total_earnings) values (6, 'Spacestation Gaming', '$10569.15');
insert into Team (team_id, team_name, total_earnings) values (7, 'Cloud9', '$72595.35');
insert into Team (team_id, team_name, total_earnings) values (8, 'Counter Logic Gaming', '$42348.74');
insert into Team (team_id, team_name, total_earnings) values (9, 'Kungarna EU', '$78129.40');
insert into Team (team_id, team_name, total_earnings) values (10, 'ZETA DIVISION', '$5881.94');
insert into Team (team_id, team_name, total_earnings) values (11, 'Aqualix', '$54173.28');
insert into Team (team_id, team_name, total_earnings) values (12, 'REJECT', '$18794.46');
insert into Team (team_id, team_name, total_earnings) values (13, 'REIGNITE', '$51421.02');
insert into Team (team_id, team_name, total_earnings) values (14, 'ENTER FORCE.36', '$72931.69');
insert into Team (team_id, team_name, total_earnings) values (15, 'Gaimin Gladiators', '$81639.71');
insert into Team (team_id, team_name, total_earnings) values (16, 'Aurora Gaming', '$15908.80');
insert into Team (team_id, team_name, total_earnings) values (17, 'Citadel Gaming', '$94180.11');
insert into Team (team_id, team_name, total_earnings) values (18, 'Made in Heaven', '$82280.15');
insert into Team (team_id, team_name, total_earnings) values (19, 'SJP2', '$67793.24');
insert into Team (team_id, team_name, total_earnings) values (20, 'TheHorde', '$90564.53');
insert into Team (team_id, team_name, total_earnings) values (21, 'Shopify Rebellion', '$56235.55');
insert into Team (team_id, team_name, total_earnings) values (22, 'JD Gaming', '$74646.77');
insert into Team (team_id, team_name, total_earnings) values (23, 'LEGACY', '$88747.37');
insert into Team (team_id, team_name, total_earnings) values (24, 'LeaveNoWitness', '$78761.74');
insert into Team (team_id, team_name, total_earnings) values (25, 'Fennel', '$52603.20');
insert into Team (team_id, team_name, total_earnings) values (26, 'Fnatic', '$41553.26');
insert into Team (team_id, team_name, total_earnings) values (27, 'TIE', '$41453.29');
insert into Team (team_id, team_name, total_earnings) values (28, 'Gen.G Esports', '$91783.70');
insert into Team (team_id, team_name, total_earnings) values (29, 'Wolves Esports', '$87578.39');
insert into Team (team_id, team_name, total_earnings) values (30, 'Weibo Gaming', '$23055.31');
insert into Team (team_id, team_name, total_earnings) values (31, '789', '$25195.42');
insert into Team (team_id, team_name, total_earnings) values (32, 'Acend', '$8780.68');
insert into Team (team_id, team_name, total_earnings) values (33, 'Forge', '$81465.50');
insert into Team (team_id, team_name, total_earnings) values (34, 'Outplayed', '$81065.45');
insert into Team (team_id, team_name, total_earnings) values (35, '100T', '$47692.13');

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
(1,  'Bangalore', 'Assault'),
(2,  'Fuse', 'Assault'),
(3,  'Ash', 'Assault'),
(4,  'Mad Maggie', 'Assault'),
(5,  'Ballistic', 'Assault'),
(6,  'Wraith', 'Skirmisher'),
(7,  'Octane', 'Skirmisher'),
(8,  'Pathfinder', 'Skirmisher'),
(9,  'Horizon', 'Skirmisher'),
(10, 'Valkyrie', 'Skirmisher'),
(11, 'Revenant', 'Skirmisher'),
(12, 'Alter', 'Skirmisher'),
(13, 'Bloodhound', 'Recon'),
(14, 'Crypto', 'Recon'),
(15, 'Seer', 'Recon'),
(16, 'Vantage', 'Recon'),
(17, 'Sparrow', 'Recon'),
(18, 'Lifeline', 'Support'),
(19, 'Gibraltar', 'Support'),
(20, 'Loba', 'Support'),
(21, 'Newcastle', 'Support'),
(22, 'Conduit', 'Support'),
(23, 'Caustic', 'Controller'),
(24, 'Wattson', 'Controller'),
(25, 'Rampart', 'Controller'),
(26, 'Catalyst', 'Controller'),
(27, 'Mirage', 'Controller');

CREATE TABLE IF NOT EXISTS DataSource (
   source_id INT PRIMARY KEY,
   source_name VARCHAR(255),
   source_type VARCHAR(100),
   api_endpoint VARCHAR(255),
   status VARCHAR(50),
   added_date DATE
);

INSERT INTO DataSource (source_id, source_name, source_type, api_endpoint, status) VALUES
(1, 'Apex Legends Official API', 'API', 'https://api.ea.com/apex/v1/stats', 'Active'),
(2, 'Tracker Network', 'API', 'https://api.tracker.gg/apex/v2/profile', 'Active'),
(3, 'Apex Legends Status', 'API', 'https://api.apexlegendsstat.us/v1/player', 'Active'),
(4, 'EA Player Data Export', 'CSV', NULL, 'Inactive'),
(5, 'Community Stats Sheet', 'CSV', NULL, 'Inactive'),
(6, 'Ranked Data Webhook', 'Webhook', 'https://hooks.apex-stats.io/ranked/ingest', 'Active'),
(7, 'Match History Webhook', 'Webhook', 'https://hooks.apex-stats.io/matches/ingest', 'Active'),
(8, 'Kill Feed Stream', 'Webhook', 'https://hooks.apex-stats.io/killfeed/stream', 'Error'),
(9, 'Manual Entry Portal', 'Manual', NULL, 'Active'),
(10, 'Tournament Organizer Feed', 'API', 'https://api.algs.gg/v1/tournament/results', 'Active'),
(11, 'ALGS Event Data', 'API', 'https://api.algs.gg/v1/events', 'Active'),
(12, 'Third Party Stat Aggregator', 'API', 'https://api.apexstat.io/v3/aggregate', 'Pending'),
(13, 'Season Archive Dump', 'CSV', NULL, 'Inactive'),
(14, 'Patch Notes Scraper', 'API', 'https://api.ea.com/apex/v1/patchnotes', 'Active'),
(15, 'Legend Pick Rate Feed', 'API', 'https://api.apexlegendsmeta.com/v1/pickrates', 'Active'),
(16, 'Weapon Meta Feed', 'API', 'https://api.apexlegendsmeta.com/v1/weapons', 'Active'),
(17, 'Player Region Feed', 'API', 'https://api.ea.com/apex/v1/region/players', 'Pending'),
(18, 'Damage Report Webhook', 'Webhook', 'https://hooks.apex-stats.io/damage/report', 'Active'),
(19, 'Squad Performance Export', 'CSV', NULL, 'Inactive'),
(20, 'Ranked Season Summary', 'CSV', NULL, 'Inactive'),
(21, 'Community Leaderboard API', 'API', 'https://api.apexleaderboard.gg/v1/ranked', 'Active'),
(22, 'Streamer Stats Feed', 'API', 'https://api.twitchstats.io/apex/streamers', 'Error'),
(23, 'Map Rotation API', 'API', 'https://api.apexlegendsstat.us/v1/maprotation', 'Active'),
(24, 'Event Schedule Feed', 'API', 'https://api.algs.gg/v1/schedule', 'Active'),
(25, 'Battle Pass Tracker', 'API', 'https://api.ea.com/apex/v1/battlepass', 'Inactive'),
(26, 'Audit Log Webhook', 'Webhook', 'https://hooks.apex-stats.io/audit/flags', 'Active'),
(27, 'Player Goal Sync', 'API', 'https://api.apexstat.io/v3/goals', 'Pending'),
(28, 'Historical Match Archive', 'CSV', NULL, 'Inactive'),
(29, 'Real Time Rank Tracker', 'Webhook', 'https://hooks.apex-stats.io/rank/realtime', 'Active'),
(30, 'Weapon Accuracy Feed', 'API', 'https://api.apexlegendsmeta.com/v1/accuracy', 'Active'),
(31, 'Team Composition Tracker', 'API', 'https://api.apexstat.io/v3/teamcomp', 'Pending'),
(32, 'Placement Stats Feed', 'API', 'https://api.tracker.gg/apex/v2/placement', 'Active'),
(33, 'Survival Time Export', 'CSV', NULL, 'Inactive'),
(34, 'Manual Tournament Entry', 'Manual', NULL, 'Active'),
(35, 'Cross Region Aggregator', 'API', 'https://api.apexleaderboard.gg/v1/regions', 'Error'),
(36, 'Season Meta Snapshot', 'API', 'https://api.apexlegendsmeta.com/v1/snapshot', 'Active'),
(37, 'Knockdown Analytics Feed', 'Webhook', 'https://hooks.apex-stats.io/knockdowns/feed', 'Active'),
(38, 'Death Location Heatmap API', 'API', 'https://api.apexstat.io/v3/deathlocation', 'Pending'),
(39, 'Import Batch Monitor', 'API', 'https://api.apexstat.io/v3/batchmonitor', 'Active'),
(40, 'Legacy Data Migration Export', 'CSV', NULL, 'Inactive');

CREATE TABLE IF NOT EXISTS Weapon (
   weapon_id INT PRIMARY KEY,
   weapon_name VARCHAR(100),
   weapon_type VARCHAR(100),
   ammo_type VARCHAR(100)
);

INSERT INTO Weapon (weapon_id, weapon_name, weapon_type, ammo_type) VALUES
(1, 'R-301 Carbine', 'AR', 'Light'),
(2, 'Flatline', 'AR', 'Heavy'),
(3, 'Hemlok Burst AR', 'AR', 'Heavy'),
(4, 'Havoc Rifle', 'AR', 'Energy'),
(5, 'Nemesis Burst AR', 'AR', 'Energy'),
(6, 'R-99 SMG', 'SMG', 'Light'),
(7, 'Alternator SMG', 'SMG', 'Light'),
(8, 'Prowler Burst PDW', 'SMG', 'Heavy'),
(9, 'C.A.R. SMG', 'SMG', 'Heavy'),
(10, 'Volt SMG', 'SMG', 'Energy'),
(11, 'Spitfire', 'LMG', 'Light'),
(12, 'Devotion LMG', 'LMG', 'Energy'),
(13, 'L-STAR EMG', 'LMG', 'Energy'),
(14, 'Rampage LMG', 'LMG', 'Heavy'),
(15, 'G7 Scout', 'Marksman', 'Light'),
(16, 'Triple Take', 'Marksman', 'Energy'),
(17, '30-30 Repeater', 'Marksman', 'Heavy'),
(18, 'Bocek Compound Bow', 'Marksman', 'Arrows'),
(19, 'Longbow DMR', 'Sniper', 'Sniper'),
(20, 'Charge Rifle', 'Sniper', 'Energy'),
(21, 'Sentinel', 'Sniper', 'Sniper'),
(22, 'Kraber .50-Cal', 'Sniper', 'Mythic'),
(23, 'Peacekeeper', 'Shotgun', 'Shotgun'),
(24, 'EVA-8 Auto', 'Shotgun', 'Shotgun'),
(25, 'Mastiff Shotgun', 'Shotgun', 'Shotgun'),
(26, 'Mozambique Shotgun', 'Shotgun', 'Shotgun'),
(27, 'P2020', 'Pistol', 'Light'),
(28, 'RE-45 Auto', 'Pistol', 'Light'),
(29, 'Wingman', 'Pistol', 'Heavy');

CREATE TABLE IF NOT EXISTS MapLocation (
   location_id INT PRIMARY KEY,
   map_name VARCHAR(100),
   location_name VARCHAR(100),
   x_coord FLOAT,
   y_coord FLOAT
);

INSERT INTO MapLocation (location_id, location_name, x_coord, y_coord) VALUES
(1, 'Skull Town', -122.4194, 37.7749),
(2, 'Bunker', -122.3917, 37.7831),
(3, 'Swamps', -122.4501, 37.7602),
(4, 'Relay', -122.3762, 37.7943),
(5, 'Thunderdome', -122.4312, 37.8012),
(6, 'Market', -122.4089, 37.7689),
(7, 'Hydro Dam', -122.3654, 37.8102),
(8, 'Artillery', -122.4423, 37.8201),
(9, 'Bridges', -122.3891, 37.7512),
(10, 'Repulsor', -122.4678, 37.8311),
(11, 'Fragment East', -104.9903, 39.7392),
(12, 'Fragment West', -105.0023, 39.7441),
(13, 'Lava City', -104.9712, 39.7198),
(14, 'The Tree', -105.0312, 39.7601),
(15, 'Countdown', -104.9534, 39.7823),
(16, 'Sorting Factory', -105.0198, 39.7312),
(17, 'Epicenter', -104.9823, 39.8012),
(18, 'Thermal Station', -105.0445, 39.7891),
(19, 'Skyhook', -104.9601, 39.8201),
(20, 'Survey Camp', -105.0567, 39.7102),
(21, 'Oasis', -73.9857, 40.7484),
(22, 'Gardens', -73.9712, 40.7612),
(23, 'Rift', -74.0023, 40.7391),
(24, 'Hammond Labs', -73.9534, 40.7823),
(25, 'Grow Towers', -74.0145, 40.7201),
(26, 'Estates', -73.9891, 40.7934),
(27, 'Orbital Cannon', -74.0312, 40.7512),
(28, 'Energy Depot', -73.9678, 40.8012),
(29, 'Bonsai Plaza', -74.0089, 40.7689),
(30, 'Docks', -73.9423, 40.8123),
(31, 'Checkpoint', -80.1918, 25.7617),
(32, 'Barometer', -80.2134, 25.7823),
(33, 'Lightning Rod', -80.1756, 25.8012),
(34, 'North Pad', -80.2312, 25.7391),
(35, 'Cascade Falls', -80.1534, 25.8201),
(36, 'Antenna', -80.2489, 25.7512),
(37, 'The Wall', -80.1912, 25.8312),
(38, 'IMC Armories', -80.2678, 25.7689),
(39, 'Trident', -80.1345, 25.7934),
(40, 'Devastated Coast', -80.2891, 25.8102),
(41, 'Eternal Garden', -87.6298, 41.8781),
(42, 'Terraformer', -87.6512, 41.8934),
(43, 'Bionomics', -87.6089, 41.9012),
(44, 'The Divide', -87.6734, 41.8601),
(45, 'Commons', -87.5923, 41.9201),
(46, 'Stasis Array', -87.6945, 41.8391),
(47, 'Catapult', -87.6156, 41.9312),
(48, 'Alpha Base', -87.7112, 41.8512),
(49, 'Jumpdriver', -87.5712, 41.8823),
(50, 'Backup Moon Base', -87.7289, 41.9102);

CREATE TABLE IF NOT EXISTS Player (
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

INSERT INTO Player (player_id, username, region, join_date, current_rank, current_rank_points, current_rank_position, total_matches, current_win_rate, overall_accuracy, team_id, rank_tier_id, created_at, updated_at) VALUES
(1,  'ImperialHal',   'NA',   '2019-03-01', 'Predator', 15420, 3,    4821, 34.21, 67.45, 1,    5, '2019-03-01', '2024-11-15'),
(2,  'Sweetdreams',   'NA',   '2019-04-12', 'Predator', 12800, 11,   4201, 31.45, 64.23, 2,    5, '2019-04-12', '2024-11-14'),
(3,  'Hakis',         'EU',   '2019-05-20', 'Predator', 13540, 7,    3987, 32.67, 65.89, 3,    5, '2019-05-20', '2024-11-15'),
(4,  'Alive',         'EU',   '2019-06-15', 'Predator', 14210, 5,    4102, 33.12, 66.34, 4,    5, '2019-06-15', '2024-11-13'),
(5,  'Dezignful',     'NA',   '2020-01-10', 'Predator', 11980, 18,   3654, 29.87, 62.11, 5,    5, '2020-01-10', '2024-11-12'),
(6,  'Reps',          'NA',   '2019-08-22', 'Master',   5820,  142,  3201, 27.34, 60.78, 6,    7, '2019-08-22', '2024-11-10'),
(7,  'Fyde',          'NA',   '2019-03-15', 'Predator', 16320, 1,    5102, 36.45, 69.12, 7,    5, '2019-03-15', '2024-11-15'),
(8,  'Poach',         'NA',   '2019-07-04', 'Master',   5410,  198,  3102, 26.78, 59.34, 8,    7, '2019-07-04', '2024-11-09'),
(9,  'Knoqd',         'EU',   '2019-09-11', 'Predator', 14890, 4,    4567, 33.89, 66.78, 9,    5, '2019-09-11', '2024-11-15'),
(10, 'Daidou',        'APAC', '2020-03-08', 'Diamond',  4210,  512,  2876, 23.45, 55.67, 10,   4, '2020-03-08', '2024-11-08'),
(11, 'Flux',          'EU',   '2020-06-17', 'Master',   5640,  167,  3312, 27.89, 61.23, 11,   7, '2020-06-17', '2024-11-11'),
(12, 'Shiimada',      'APAC', '2020-08-25', 'Diamond',  4560,  423,  2654, 22.34, 54.89, 12,   4, '2020-08-25', '2024-11-07'),
(13, 'Verhulst',      'EU',   '2019-11-30', 'Predator', 12340, 14,   3876, 30.12, 63.45, 13,   5, '2019-11-30', '2024-11-14'),
(14, 'Diegosaurs',    'EU',   '2020-02-14', 'Predator', 13120, 9,    4023, 31.78, 64.67, 14,   5, '2020-02-14', '2024-11-13'),
(15, 'Olsen',         'EU',   '2019-12-01', 'Predator', 15120, 2,    4712, 35.23, 68.34, 15,   5, '2019-12-01', '2024-11-15'),
(16, 'Monsoon',       'SA',   '2021-01-19', 'Diamond',  4820,  389,  2543, 21.67, 53.78, 16,   4, '2021-01-19', '2024-11-06'),
(17, 'Dropped',       'NA',   '2019-10-05', 'Predator', 13780, 6,    4234, 32.34, 65.12, 17,   5, '2019-10-05', '2024-11-15'),
(18, 'Rogue',         'EU',   '2020-04-22', 'Predator', 12560, 13,   3945, 30.67, 63.89, 18,   5, '2020-04-22', '2024-11-14'),
(19, 'Naughty',       'NA',   '2020-09-13', 'Master',   5230,  221,  3045, 26.12, 58.90, 19,   7, '2020-09-13', '2024-11-10'),
(20, 'Verhext',       'EU',   '2019-07-28', 'Predator', 13980, 8,    4312, 32.89, 65.56, 20,   5, '2019-07-28', '2024-11-15'),
(21, 'Snip3down',     'NA',   '2019-03-05', 'Predator', 12100, 16,   3823, 29.45, 62.34, 21,   5, '2019-03-05', '2024-11-12'),
(22, 'GarrettG',      'APAC', '2020-05-11', 'Master',   5780,  151,  3267, 27.56, 61.01, 22,   7, '2020-05-11', '2024-11-11'),
(23, 'Bobz',          'NA',   '2019-06-30', 'Predator', 11760, 21,   3712, 28.78, 61.78, 23,   5, '2019-06-30', '2024-11-13'),
(24, 'Mande',         'EU',   '2019-09-22', 'Predator', 13340, 10,   4089, 31.23, 64.45, 24,   5, '2019-09-22', '2024-11-14'),
(25, 'Noko',          'APAC', '2020-07-14', 'Diamond',  4390,  478,  2712, 22.89, 54.34, 25,   4, '2020-07-14', '2024-11-07'),
(26, 'Scrubba',       'EU',   '2020-01-28', 'Master',   5120,  234,  3023, 25.67, 58.12, 26,   7, '2020-01-28', '2024-11-09'),
(27, 'Shivfps',       'EU',   '2019-05-07', 'Predator', 12890, 12,   3934, 30.34, 63.23, 27,   5, '2019-05-07', '2024-11-13'),
(28, 'Aceu',          'NA',   '2019-03-20', 'Predator', 13560, 7,    4156, 32.12, 65.34, 28,   5, '2019-03-20', '2024-11-15'),
(29, 'Extesyy',       'EU',   '2019-08-14', 'Predator', 14450, 4,    4423, 33.56, 66.89, 29,   5, '2019-08-14', '2024-11-15'),
(30, 'Xiaowu',        'APAC', '2021-02-09', 'Diamond',  4670,  401,  2589, 21.23, 53.12, 30,   4, '2021-02-09', '2024-11-06'),
(31, 'Wingsofdeath',  'NA',   '2021-05-03', 'Platinum', 3210,  1823, 2134, 18.45, 49.78, 31,   6, '2021-05-03', '2024-11-04'),
(32, 'Vaxlon',        'EU',   '2021-08-19', 'Gold',     2450,  3412, 1876, 15.67, 46.23, 32,   1, '2021-08-19', '2024-11-03'),
(33, 'Craftsman',     'NA',   '2020-11-07', 'Predator', 11540, 24,   3634, 28.12, 60.89, 33,   5, '2020-11-07', '2024-11-12'),
(34, 'Teetow',        'EU',   '2020-03-25', 'Predator', 12670, 13,   3801, 29.78, 62.56, 34,   5, '2020-03-25', '2024-11-13'),
(35, 'Rambeau',       'NA',   '2020-06-01', 'Master',   5340,  209,  3112, 26.45, 59.67, 35,   7, '2020-06-01', '2024-11-10'),
(36, 'Phenoxyz',      'NA',   '2021-03-14', 'Predator', 11200, 28,   3456, 27.34, 60.12, 1,    5, '2021-03-14', '2024-11-12'),
(37, 'LmaDrop',       'EU',   '2021-06-22', 'Master',   5050,  267,  2987, 25.12, 57.89, 2,    7, '2021-06-22', '2024-11-10'),
(38, 'Koloblex',      'APAC', '2021-09-10', 'Diamond',  4780,  345,  2634, 22.67, 54.12, 3,    4, '2021-09-10', '2024-11-08'),
(39, 'Unlucky',       'NA',   '2022-01-05', 'Platinum', 3450,  1654, 2213, 19.23, 50.34, NULL, 6, '2022-01-05', '2024-11-05'),
(40, 'Zelatrix',      'EU',   '2022-02-18', 'Diamond',  4120,  534,  2512, 21.45, 53.67, 4,    4, '2022-02-18', '2024-11-07'),
(41, 'Paradoxine',    'SA',   '2022-03-30', 'Platinum', 3780,  1423, 2089, 18.90, 49.56, NULL, 6, '2022-03-30', '2024-11-04'),
(42, 'Clutchfactor',  'NA',   '2021-11-15', 'Master',   5890,  134,  3378, 28.23, 61.45, 5,    7, '2021-11-15', '2024-11-11'),
(43, 'Ghostpeak',     'EU',   '2022-04-07', 'Diamond',  4340,  489,  2601, 22.12, 53.90, NULL, 4, '2022-04-07', '2024-11-06'),
(44, 'Toxicore',      'APAC', '2022-05-19', 'Gold',     2780,  2987, 1934, 16.34, 47.12, 6,    1, '2022-05-19', '2024-11-03'),
(45, 'Frostbyte',     'NA',   '2022-06-11', 'Predator', 11890, 22,   3589, 28.67, 61.23, 7,    5, '2022-06-11', '2024-11-13'),
(46, 'Arcaneveil',    'EU',   '2021-12-03', 'Master',   5670,  158,  3234, 27.12, 60.45, NULL, 7, '2021-12-03', '2024-11-10'),
(47, 'Noxflare',      'NA',   '2022-07-25', 'Diamond',  4890,  312,  2723, 23.56, 55.34, 8,    4, '2022-07-25', '2024-11-08'),
(48, 'Solstrike',     'SA',   '2022-08-14', 'Silver',   1450,  5234, 1623, 13.45, 43.78, NULL, 2, '2022-08-14', '2024-11-02'),
(49, 'Driftwood',     'APAC', '2022-09-01', 'Gold',     2340,  3123, 1812, 15.23, 45.89, 9,    1, '2022-09-01', '2024-11-03'),
(50, 'Voidstep',      'EU',   '2022-10-17', 'Predator', 12450, 15,   3712, 29.34, 62.67, 10,   5, '2022-10-17', '2024-11-14'),
(51, 'Ciphershot',    'NA',   '2022-11-28', 'Master',   5120,  243,  3089, 25.78, 58.56, NULL, 7, '2022-11-28', '2024-11-09'),
(52, 'Blazerunner',   'EU',   '2023-01-09', 'Diamond',  4230,  521,  2567, 21.89, 53.45, 11,   4, '2023-01-09', '2024-11-07'),
(53, 'Krathos',       'APAC', '2023-02-22', 'Platinum', 3560,  1589, 2145, 19.12, 50.12, NULL, 6, '2023-02-22', '2024-11-04'),
(54, 'Nullbyte',      'NA',   '2023-03-14', 'Gold',     2670,  3056, 1867, 15.89, 46.78, 12,   1, '2023-03-14', '2024-11-03'),
(55, 'Wrenchpilot',   'EU',   '2023-04-05', 'Predator', 11340, 26,   3523, 27.89, 60.34, 13,   5, '2023-04-05', '2024-11-12'),
(56, 'Axiomshift',    'SA',   '2023-05-18', 'Silver',   1780,  4987, 1712, 14.12, 44.56, NULL, 2, '2023-05-18', '2024-11-02'),
(57, 'Ragepulse',     'NA',   '2023-06-30', 'Diamond',  4560,  432,  2645, 22.45, 54.67, 14,   4, '2023-06-30', '2024-11-07'),
(58, 'Emberclad',     'EU',   '2023-07-12', 'Master',   5450,  189,  3156, 26.78, 59.89, NULL, 7, '2023-07-12', '2024-11-10'),
(59, 'Frostmantle',   'APAC', '2023-08-24', 'Bronze',   780,   7234, 1234, 10.23, 38.45, NULL, 3, '2023-08-24', '2024-11-01'),
(60, 'Staticwulf',    'NA',   '2023-09-06', 'Platinum', 3890,  1312, 2234, 19.67, 51.23, 15,   6, '2023-09-06', '2024-11-05');

CREATE TABLE IF NOT EXISTS ImportBatch (
   batch_id INT PRIMARY KEY,
   source_id INT,
   import_date DATE,
   records_imported INT,
   import_status VARCHAR(50),
   FOREIGN KEY (source_id) REFERENCES DataSource(source_id)
);

insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (1, 21, '2025-06-05', 452, 'completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (2, 34, '2025-12-04', 201, 'pending');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (3, 38, '2025-11-25', 124, 'not completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (4, 19, '2026-03-02', 420, 'completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (5, 1, '2025-11-25', 478, 'pending');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (6, 16, '2025-06-28', 269, 'not completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (7, 17, '2025-08-20', 362, 'completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (8, 39, '2025-12-19', 239, 'pending');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (9, 18, '2025-09-17', 174, 'not completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (10, 9, '2026-01-26', 97, 'completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (11, 26, '2025-05-02', 127, 'pending');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (12, 7, '2025-07-07', 35, 'not completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (13, 38, '2025-09-01', 102, 'completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (14, 24, '2026-03-26', 437, 'pending');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (15, 24, '2026-04-04', 320, 'not completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (16, 15, '2025-12-31', 110, 'completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (17, 4, '2025-04-19', 491, 'pending');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (18, 23, '2025-05-14', 486, 'not completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (19, 17, '2025-11-01', 425, 'completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (20, 13, '2025-08-19', 212, 'pending');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (21, 30, '2025-05-31', 124, 'not completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (22, 13, '2026-01-15', 325, 'completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (23, 37, '2025-07-28', 32, 'pending');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (24, 36, '2025-11-18', 372, 'not completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (25, 12, '2025-09-30', 112, 'completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (26, 11, '2025-12-14', 96, 'pending');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (27, 2, '2025-06-04', 31, 'not completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (28, 21, '2025-08-06', 456, 'completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (29, 1, '2025-12-13', 376, 'pending');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (30, 17, '2025-11-01', 483, 'not completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (31, 20, '2026-01-06', 280, 'completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (32, 21, '2026-01-22', 21, 'pending');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (33, 32, '2026-03-03', 400, 'not completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (34, 2, '2026-01-13', 253, 'completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (35, 35, '2026-03-13', 428, 'pending');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (36, 5, '2025-04-20', 80, 'not completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (37, 21, '2025-12-15', 112, 'completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (38, 20, '2025-06-28', 310, 'pending');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (39, 3, '2026-01-17', 436, 'not completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (40, 7, '2025-12-27', 161, 'completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (41, 25, '2026-02-02', 387, 'pending');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (42, 19, '2025-09-21', 251, 'not completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (43, 33, '2026-01-23', 26, 'completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (44, 34, '2026-04-05', 245, 'pending');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (45, 23, '2025-05-15', 412, 'not completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (46, 25, '2026-02-26', 407, 'completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (47, 34, '2025-07-20', 160, 'pending');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (48, 4, '2025-11-07', 81, 'not completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (49, 1, '2025-06-06', 321, 'completed');
insert into ImportBatch (batch_id, source_id, import_date, records_imported, import_status) values (50, 40, '2025-06-20', 498, 'pending');

CREATE TABLE IF NOT EXISTS `Match` (
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

INSERT INTO `Match` (match_id, match_date, season_name, map_name, mode, match_duration, tournament_name, source_id) VALUES
(1,  '2023-02-14', 'Season 16', 'Kings Canyon',  'Ranked',     1823, 'ALGS Pro League Split 1 2023',  10),
(2,  '2023-02-15', 'Season 16', 'World''s Edge', 'Ranked',     2134, 'ALGS Pro League Split 1 2023',  10),
(3,  '2023-02-16', 'Season 16', 'Olympus',       'Ranked',     1956, 'ALGS Pro League Split 1 2023',  10),
(4,  '2023-02-17', 'Season 16', 'Storm Point',   'Ranked',     2287, 'ALGS Pro League Split 1 2023',  10),
(5,  '2023-02-18', 'Season 16', 'Kings Canyon',  'Tournament', 1734, 'ALGS Pro League Split 1 2023',  10),
(6,  '2023-02-19', 'Season 16', 'World''s Edge', 'Tournament', 2045, 'ALGS Pro League Split 1 2023',  10),
(7,  '2023-02-20', 'Season 16', 'Storm Point',   'Tournament', 1867, 'ALGS Pro League Split 1 2023',  10),
(8,  '2023-03-01', 'Season 16', 'Olympus',       'Tournament', 2312, 'ALGS Pro League Split 1 2023',  10),
(9,  '2023-03-05', 'Season 16', 'Kings Canyon',  'Tournament', 1978, 'ALGS Pro League Split 1 2023',  10),
(10, '2023-03-10', 'Season 16', 'World''s Edge', 'Tournament', 2156, 'ALGS Pro League Split 1 2023',  10),
(11, '2023-03-15', 'Season 16', 'Storm Point',   'Tournament', 1823, 'ALGS Pro League Split 1 2023',  10),
(12, '2023-03-19', 'Season 16', 'Olympus',       'Tournament', 2089, 'ALGS Pro League Split 1 2023',  10),
(13, '2023-04-22', 'Season 17', 'Kings Canyon',  'Tournament', 1945, 'ALGS Pro League Split 2 2023',  10),
(14, '2023-04-23', 'Season 17', 'World''s Edge', 'Tournament', 2234, 'ALGS Pro League Split 2 2023',  10),
(15, '2023-04-24', 'Season 17', 'Storm Point',   'Tournament', 1867, 'ALGS Pro League Split 2 2023',  10),
(16, '2023-04-25', 'Season 17', 'Broken Moon',   'Tournament', 2123, 'ALGS Pro League Split 2 2023',  10),
(17, '2023-05-01', 'Season 17', 'Kings Canyon',  'Tournament', 1756, 'ALGS Pro League Split 2 2023',  10),
(18, '2023-05-08', 'Season 17', 'World''s Edge', 'Tournament', 2034, 'ALGS Pro League Split 2 2023',  10),
(19, '2023-05-15', 'Season 17', 'Storm Point',   'Tournament', 1912, 'ALGS Pro League Split 2 2023',  10),
(20, '2023-05-22', 'Season 17', 'Broken Moon',   'Tournament', 2267, 'ALGS Pro League Split 2 2023',  10),
(21, '2023-06-01', 'Season 17', 'Kings Canyon',  'Tournament', 1834, 'ALGS Pro League Split 2 2023',  10),
(22, '2023-06-10', 'Season 17', 'World''s Edge', 'Tournament', 2145, 'ALGS Pro League Split 2 2023',  10),
(23, '2023-06-18', 'Season 17', 'Storm Point',   'Tournament', 1978, 'ALGS Pro League Split 2 2023',  10),
(24, '2023-07-13', 'Season 17', 'Broken Moon',   'Tournament', 2312, 'ALGS Year 3 Championships',     10),
(25, '2023-07-13', 'Season 17', 'Kings Canyon',  'Tournament', 2089, 'ALGS Year 3 Championships',     10),
(26, '2023-07-14', 'Season 17', 'world''s Edge', 'Tournament', 1956, 'ALGS Year 3 Championships',     10),
(27, '2023-07-14', 'Season 17', 'Storm Point',   'Tournament', 2234, 'ALGS Year 3 Championships',     10),
(28, '2023-07-15', 'Season 17', 'Broken Moon',   'Tournament', 1867, 'ALGS Year 3 Championships',     10),
(29, '2023-07-15', 'Season 17', 'Kings Canyon',  'Tournament', 2123, 'ALGS Year 3 Championships',     10),
(30, '2023-07-16', 'Season 17', 'world''s Edge', 'Tournament', 1978, 'ALGS Year 3 Championships',     10),
(31, '2023-07-16', 'Season 17', 'Storm Point',   'Tournament', 2289, 'ALGS Year 3 Championships',     10),
(32, '2023-08-01', 'Season 18', 'Broken Moon',   'Tournament', 1834, 'ALGS LAN Stockholm',            10),
(33, '2023-08-02', 'Season 18', 'Kings Canyon',  'Tournament', 2156, 'ALGS LAN Stockholm',            10),
(34, '2023-08-03', 'Season 18', 'world''s Edge', 'Tournament', 1923, 'ALGS LAN Stockholm',            10),
(35, '2024-01-13', 'Season 20', 'Storm Point',   'Tournament', 2078, 'ALGS Pro League Split 1 2024',  10),
(36, '2024-01-14', 'Season 20', 'Broken Moon',   'Tournament', 1845, 'ALGS Pro League Split 1 2024',  10),
(37, '2024-01-20', 'Season 20', 'Kings Canyon',  'Tournament', 2234, 'ALGS Pro League Split 1 2024',  10),
(38, '2024-01-27', 'Season 20', 'world''s Edge', 'Tournament', 1967, 'ALGS Pro League Split 1 2024',  10),
(39, '2024-02-03', 'Season 20', 'Storm Point',   'Tournament', 2145, 'ALGS Pro League Split 1 2024',  10),
(40, '2024-02-10', 'Season 20', 'Broken Moon',   'Tournament', 1878, 'ALGS Pro League Split 1 2024',  10),
(41, '2024-02-17', 'Season 20', 'Kings Canyon',  'Tournament', 2312, 'ALGS Pro League Split 1 2024',  10),
(42, '2024-02-24', 'Season 20', 'world''s Edge', 'Tournament', 1989, 'ALGS Pro League Split 1 2024',  10),
(43, '2024-03-02', 'Season 20', 'Storm Point',   'Tournament', 2056, 'ALGS Pro League Split 1 2024',  10),
(44, '2024-03-17', 'Season 20', 'Broken Moon',   'Tournament', 1923, 'ALGS Pro League Split 1 2024',  10),
(45, '2024-04-20', 'Season 21', 'Kings Canyon',  'Tournament', 2189, 'ALGS Pro League Split 2 2024',  10),
(46, '2024-04-27', 'Season 21', 'world''s Edge', 'Tournament', 1856, 'ALGS Pro League Split 2 2024',  10),
(47, '2024-05-04', 'Season 21', 'Storm Point',   'Tournament', 2234, 'ALGS Pro League Split 2 2024',  10),
(48, '2024-05-11', 'Season 21', 'Broken Moon',   'Tournament', 1978, 'ALGS Pro League Split 2 2024',  10),
(49, '2024-05-18', 'Season 21', 'Kings Canyon',  'Tournament', 2067, 'ALGS Pro League Split 2 2024',  10),
(50, '2024-05-25', 'Season 21', 'world''s Edge', 'Tournament', 1845, 'ALGS Pro League Split 2 2024',  10),
(51, '2024-06-01', 'Season 21', 'Storm Point',   'Tournament', 2156, 'ALGS Pro League Split 2 2024',  10),
(52, '2024-06-08', 'Season 21', 'Broken Moon',   'Tournament', 1923, 'ALGS Pro League Split 2 2024',  10),
(53, '2024-06-16', 'Season 21', 'Kings Canyon',  'Tournament', 2289, 'ALGS Pro League Split 2 2024',  10),
(54, '2024-06-20', 'Season 21', 'world''s Edge', 'Tournament', 1967, 'ALGS Year 4 Championships',     10),
(55, '2024-06-20', 'Season 21', 'Storm Point',   'Tournament', 2134, 'ALGS Year 4 Championships',     10),
(56, '2024-06-21', 'Season 21', 'Broken Moon',   'Tournament', 1856, 'ALGS Year 4 Championships',     10),
(57, '2024-06-21', 'Season 21', 'Kings Canyon',  'Tournament', 2312, 'ALGS Year 4 Championships',     10),
(58, '2024-06-22', 'Season 21', 'world''s Edge', 'Tournament', 1989, 'ALGS Year 4 Championships',     10),
(59, '2024-06-22', 'Season 21', 'Storm Point',   'Tournament', 2078, 'ALGS Year 4 Championships',     10),
(60, '2024-06-23', 'Season 21', 'Broken Moon',   'Tournament', 1934, 'ALGS Year 4 Championships',     10),
(61, '2024-06-23', 'Season 21', 'Kings Canyon',  'Tournament', 2245, 'ALGS Year 4 Championships',     10),
(62, '2024-03-22', 'Season 20', 'world''s Edge', 'Tournament', 1878, 'ALGS LAN Birmingham',           10),
(63, '2024-03-23', 'Season 20', 'Storm Point',   'Tournament', 2156, 'ALGS LAN Birmingham',           10),
(64, '2024-03-24', 'Season 20', 'Broken Moon',   'Tournament', 1967, 'ALGS LAN Birmingham',           10),
(65, '2022-07-07', 'Season 13', 'Kings Canyon',  'Tournament', 2089, 'ALGS Year 2 Championships',     10),
(66, '2022-07-07', 'Season 13', 'world''s Edge', 'Tournament', 1923, 'ALGS Year 2 Championships',     10),
(67, '2022-07-08', 'Season 13', 'Storm Point',   'Tournament', 2234, 'ALGS Year 2 Championships',     10),
(68, '2022-07-08', 'Season 13', 'Kings Canyon',  'Tournament', 1856, 'ALGS Year 2 Championships',     10),
(69, '2022-07-09', 'Season 13', 'world''s Edge', 'Tournament', 2145, 'ALGS Year 2 Championships',     10),
(70, '2022-07-09', 'Season 13', 'Storm Point',   'Tournament', 1978, 'ALGS Year 2 Championships',     10),
(71, '2022-07-10', 'Season 13', 'Kings Canyon',  'Tournament', 2312, 'ALGS Year 2 Championships',     10),
(72, '2022-07-10', 'Season 13', 'world''s Edge', 'Tournament', 1867, 'ALGS Year 2 Championships',     10),
(73, '2022-09-02', 'Season 14', 'Storm Point',   'Tournament', 2056, 'ALGS LAN London',               10),
(74, '2022-09-03', 'Season 14', 'Kings Canyon',  'Tournament', 1934, 'ALGS LAN London',               10),
(75, '2022-09-04', 'Season 14', 'world''s Edge', 'Tournament', 2189, 'ALGS LAN London',               10);

CREATE TABLE IF NOT EXISTS PlayerMatchPerformance (
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


CREATE TABLE IF NOT EXISTS PlayerWeaponPerformance (
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


CREATE TABLE IF NOT EXISTS PlayerLegendPerformance (
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


CREATE TABLE IF NOT EXISTS TeamComposition (
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


CREATE TABLE IF NOT EXISTS MetaTrend (
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


CREATE TABLE IF NOT EXISTS GameEvent (
   event_id INT PRIMARY KEY,
   event_name VARCHAR(255),
   event_type VARCHAR(100),
   start_date DATE,
   end_date DATE,
   description VARCHAR(255)
);


INSERT INTO GameEvent (event_id, event_name, event_type, start_date, end_date, description) VALUES
(1, 'Fight or Fright', 'Seasonal', '2021-10-19', '2021-11-02', 'Halloween themed seasonal event with limited LTMs and cosmetics'),
(2, 'Holo-Day Bash', 'Seasonal', '2021-12-07', '2022-01-04', 'Winter holiday event featuring festive skins and game modes'),
(3, 'Fight or Fright', 'Seasonal', '2022-10-18', '2022-11-01', 'Halloween themed seasonal event with limited LTMs and cosmetics'),
(4, 'Holo-Day Bash', 'Seasonal', '2022-12-06', '2023-01-03', 'Winter holiday event featuring festive skins and game modes'),
(5, 'Fight or Fright', 'Seasonal', '2023-10-17', '2023-10-31', 'Halloween themed seasonal event with limited LTMs and cosmetics'),
(6, 'Holo-Day Bash', 'Seasonal', '2023-12-05', '2024-01-02', 'Winter holiday event featuring festive skins and game modes'),
(7, 'Fight or Fright', 'Seasonal', '2024-10-15', '2024-10-29', 'Halloween themed seasonal event with limited LTMs and cosmetics'),
(8, 'Holo-Day Bash', 'Seasonal', '2024-12-03', '2025-01-07', 'Winter holiday event featuring festive skins and game modes'),
(9, 'Raiders Collection Event', 'Collection', '2021-12-07', '2021-12-21', 'Limited time collection event with exclusive legendary cosmetics'),
(10, 'Awakening Collection Event', 'Collection', '2022-06-21', '2022-07-05', 'Limited time collection event with exclusive legendary cosmetics'),
(11, 'Beast of Prey Collection Event', 'Collection', '2022-09-20', '2022-10-04', 'Limited time collection event with exclusive legendary cosmetics'),
(12, 'Harbingers Collection Event', 'Collection', '2023-03-07', '2023-03-21', 'Limited time collection event with exclusive legendary cosmetics'),
(13, 'Veiled Collection Event', 'Collection', '2023-08-08', '2023-08-22', 'Limited time collection event with exclusive legendary cosmetics'),
(14, 'Dressed to Kill Collection Event', 'Collection', '2024-02-13', '2024-02-27', 'Limited time collection event with exclusive legendary cosmetics'),
(15, 'Celestial Sunrise Collection Event', 'Collection', '2024-07-09', '2024-07-23', 'Limited time collection event with exclusive legendary cosmetics'),
(16, 'Warriors Event', 'Takeover', '2022-03-29', '2022-04-12', 'Limited time takeover event with modified gameplay and rewards'),
(17, 'Evolution Collection Event', 'Takeover', '2021-09-14', '2021-09-28', 'Evolution themed takeover with map changes and exclusive rewards'),
(18, 'Dark Depths Event', 'Takeover', '2022-01-11', '2022-01-25', 'Underwater themed takeover event with unique cosmetics'),
(19, 'Genesis Collection Event', 'Takeover', '2021-06-29', '2021-07-13', 'Throwback event featuring classic Kings Canyon and Kings Canyon After Dark'),
(20, 'Emergence Event', 'Takeover', '2021-08-03', '2021-08-17', 'Emergence themed takeover with new LTM and exclusive rewards'),
(21, 'ALGS Year 2 Championships', 'Tournament', '2022-07-07', '2022-07-10', 'ALGS global championship tournament for Year 2 pro league teams'),
(22, 'ALGS Year 3 Championships', 'Tournament', '2023-07-13', '2023-07-16', 'ALGS global championship tournament for Year 3 pro league teams'),
(23, 'ALGS Year 4 Championships', 'Tournament', '2024-06-20', '2024-06-23', 'ALGS global championship tournament for Year 4 pro league teams'),
(24, 'ALGS Pro League Split 1 2023', 'Tournament', '2023-01-14', '2023-03-19', 'First split of the ALGS Pro League 2023 competitive season'),
(25, 'ALGS Pro League Split 2 2023', 'Tournament', '2023-04-22', '2023-06-18', 'Second split of the ALGS Pro League 2023 competitive season'),
(26, 'ALGS Pro League Split 1 2024', 'Tournament', '2024-01-13', '2024-03-17', 'First split of the ALGS Pro League 2024 competitive season'),
(27, 'ALGS Pro League Split 2 2024', 'Tournament', '2024-04-20', '2024-06-16', 'Second split of the ALGS Pro League 2024 competitive season'),
(28, 'ALGS LAN London', 'Tournament', '2022-09-02', '2022-09-04', 'ALGS LAN event held in London with top regional teams competing'),
(29, 'ALGS LAN Stockholm', 'Tournament', '2023-03-31', '2023-04-02', 'ALGS LAN event held in Stockholm with top regional teams competing'),
(30, 'ALGS LAN Birmingham', 'Tournament', '2024-03-22', '2024-03-24', 'ALGS LAN event held in Birmingham with top regional teams competing'),
(31, 'Anniversary Celebration Year 3', 'Anniversary', '2022-02-08', '2022-02-22', 'Celebrating 3 years of Apex Legends with exclusive rewards and challenges'),
(32, 'Anniversary Celebration Year 4', 'Anniversary', '2023-02-07', '2023-02-21', 'Celebrating 4 years of Apex Legends with exclusive rewards and challenges'),
(33, 'Anniversary Celebration Year 5', 'Anniversary', '2024-02-06', '2024-02-20', 'Celebrating 5 years of Apex Legends with exclusive rewards and challenges'),
(34, 'Anniversary Celebration Year 6', 'Anniversary', '2025-02-04', '2025-02-18', 'Celebrating 6 years of Apex Legends with exclusive rewards and challenges'),
(35, 'Ranked Series 1 2022', 'Ranked', '2022-02-08', '2022-05-03', 'First ranked series of 2022 with updated ranking system and rewards'),
(36, 'Ranked Series 2 2022', 'Ranked', '2022-05-10', '2022-08-09', 'Second ranked series of 2022 with updated ranking system and rewards'),
(37, 'Ranked Series 1 2023', 'Ranked', '2023-02-14', '2023-05-09', 'First ranked series of 2023 with updated ranking system and rewards'),
(38, 'Ranked Series 2 2023', 'Ranked', '2023-05-09', '2023-08-08', 'Second ranked series of 2023 with updated ranking system' );

CREATE TABLE IF NOT EXISTS Notification (
   notification_id INT PRIMARY KEY,
   player_id INT,
   event_id INT,
   notification_type VARCHAR(100),
   sent_date DATE,
   read_status BOOLEAN,
   FOREIGN KEY (player_id) REFERENCES Player(player_id),
   FOREIGN KEY (event_id) REFERENCES GameEvent(event_id)
);


CREATE TABLE IF NOT EXISTS Goal (
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


CREATE TABLE IF NOT EXISTS TrackedStatEntry (
   stat_entry_id INT PRIMARY KEY,
   player_id INT,
   stat_type VARCHAR(100),
   stat_value DECIMAL(8,2),
   recorded_date DATE,
   is_visible BOOLEAN,
   FOREIGN KEY (player_id) REFERENCES Player(player_id)
);


CREATE TABLE IF NOT EXISTS AuditFlag (
   audit_flag_id INT PRIMARY KEY,
   performance_id INT,
   flag_type VARCHAR(100),
   flag_reason VARCHAR(255),
   flag_date DATE,
   review_status VARCHAR(50),
   FOREIGN KEY (performance_id) REFERENCES PlayerMatchPerformance(performance_id)
);


CREATE TABLE IF NOT EXISTS ArchivedMatch (
   archived_match_id INT AUTO_INCREMENT PRIMARY KEY,
   original_match_id INT,
   season_name VARCHAR(100),
   match_date DATE,
   archived_date DATE
);


CREATE TABLE IF NOT EXISTS ArchivedPerformance (
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


CREATE TABLE IF NOT EXISTS SystemReport (
   report_id INT PRIMARY KEY,
   report_type VARCHAR(100),
   generated_date DATE,
   report_scope VARCHAR(255),
   created_by VARCHAR(100),
   output_format VARCHAR(50)
);

