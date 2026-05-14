
-- ============================================
-- DevLog Database Schema (FINAL WORKING)
-- ============================================

CREATE DATABASE IF NOT EXISTS devlog_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE devlog_db;

-- ============================================
-- USERS TABLE
-- ============================================
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    avatar_initials VARCHAR(5) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- ACTIVITIES TABLE
-- ============================================
CREATE TABLE IF NOT EXISTS activities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    tag ENUM(
        'Deploy',
        'Build',
        'Learn',
        'Fix',
        'Research',
        'Other'
    ) DEFAULT 'Build',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- ============================================
-- KUDOS TABLE
-- ============================================
CREATE TABLE IF NOT EXISTS kudos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    activity_id INT NOT NULL,
    user_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY unique_kudos (activity_id, user_id),
    FOREIGN KEY (activity_id) REFERENCES activities(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- ============================================
-- SAMPLE USERS
-- Password for all users = demo123
-- bcrypt hashes
-- ============================================

INSERT INTO users (username, password_hash, avatar_initials) VALUES
('keerti', '$2b$12$EWFmGrX2jFkI7h8HX4q5uuLQ7U8kQhR3z0L2gCb9Mw6NxA4O1JNPC', 'KT'),
('arjun',  '$2b$12$EWFmGrX2jFkI7h8HX4q5uuLQ7U8kQhR3z0L2gCb9Mw6NxA4O1JNPC', 'AR'),
('meera',  '$2b$12$EWFmGrX2jFkI7h8HX4q5uuLQ7U8kQhR3z0L2gCb9Mw6NxA4O1JNPC', 'MS');

-- ============================================
-- SAMPLE ACTIVITIES
-- ============================================

INSERT INTO activities (user_id, title, description, tag) VALUES
(1, 'Deployed Flask App on AWS',
 'Used Docker + EC2. Configured Nginx reverse proxy and SSL.', 'Deploy'),

(2, 'Completed Redis Caching Module',
 'Reduced database queries by 60% using Redis caching.', 'Learn'),

(3, 'Built REST API with JWT Auth',
 'Created secure token auth with refresh tokens.', 'Build'),

(1, 'Fixed Critical Login Bug',
 'Resolved logout session token issue.', 'Fix'),

(2, 'Research on Microservices',
 'Compared gRPC vs REST communication.', 'Research'),

(3, 'Docker Compose Multi-Service Setup',
 'Flask + MySQL + Redis + Nginx using docker compose.', 'Deploy');

-- ============================================
-- SAMPLE KUDOS
-- ============================================

INSERT INTO kudos (activity_id, user_id) VALUES
(1,2),(1,3),
(2,1),(2,3),
(3,1),(3,2),
(4,2),
(5,1),(5,3),
(6,1),(6,2),(6,3);