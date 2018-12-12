MYSQL_UPGRADE = """
CREATE TABLE account (
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name NVARCHAR(80) NOT NULL
);

CREATE TABLE person (
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    account_id INTEGER UNSIGNED NOT NULL,
    google_id_token_sub NVARCHAR(32) NOT NULL,
    name NVARCHAR(80) NOT NULL,
    meet_freq INTEGER UNSIGNED NOT NULL DEFAULT 15,
    match_randomizer NVARCHAR(32)
);
ALTER TABLE person ADD INDEX account_id (account_id);
ALTER TABLE person ADD INDEX meet_freq (meet_freq);

CREATE TABLE topic (
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    account_id INTEGER UNSIGNED NOT NULL,
    name NVARCHAR(32) NOT NULL
);
ALTER TABLE topic ADD INDEX account_id (account_id);

CREATE TABLE reading (
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    account_id INTEGER UNSIGNED NOT NULL,
    url NVARCHAR(2048) NOT NULL
);
ALTER TABLE reading ADD INDEX account_id (account_id);

CREATE TABLE reading_topic (
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    reading_id INTEGER UNSIGNED NOT NULL,
    topic_id INTEGER UNSIGNED NOT NULL
);
ALTER TABLE reading_topic ADD UNIQUE reading_topic (reading_id, topic_id);

CREATE TABLE person_topic (
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    person_id INTEGER UNSIGNED NOT NULL,
    topic_id INTEGER UNSIGNED NOT NULL
);
ALTER TABLE person_topic ADD UNIQUE person_topic (person_id, topic_id);

CREATE TABLE meeting (
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    reading_id INTEGER UNSIGNED NOT NULL,
    calendar_event_id NVARCHAR(1024) NOT NULL
);
ALTER TABLE meeting ADD INDEX reading_id (reading_id);

CREATE TABLE meeting_person (
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    meeting_id INTEGER UNSIGNED NOT NULL,
    person_id INTEGER UNSIGNED NOT NULL
);
ALTER TABLE meeting_person ADD UNIQUE meeting_person (meeting_id, person_id);
"""

MYSQL_DOWNGRADE = """
DROP TABLE meeting_person;
DROP TABLE meeting;
DROP TABLE person_topic;
DROP TABLE reading_topic;
DROP TABLE reading;
DROP TABLE topic;
DROP TABLE person;
DROP TABLE account;
"""
