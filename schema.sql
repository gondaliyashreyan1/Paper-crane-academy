-- Cloudflare D1 Database Schema for The Paper Crane Academy

CREATE TABLE IF NOT EXISTS users (
  uid TEXT PRIMARY KEY,
  email TEXT UNIQUE,
  password_hash TEXT,
  display_name TEXT,
  academic_level TEXT,
  interests TEXT DEFAULT '[]',
  goals TEXT DEFAULT '',
  is_admin INTEGER DEFAULT 0,
  created_at TEXT,
  updated_at TEXT
);

CREATE TABLE IF NOT EXISTS articles (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  subtitle TEXT,
  category TEXT,
  kind TEXT,
  author_name TEXT,
  author_id TEXT,
  body TEXT,
  sources TEXT DEFAULT '[]',
  status TEXT DEFAULT 'published',
  editor_note TEXT,
  publish_at TEXT,
  date TEXT,
  featured INTEGER DEFAULT 0,
  correction TEXT,
  created_at TEXT,
  updated_at TEXT
);

CREATE TABLE IF NOT EXISTS events (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  type TEXT,
  date TEXT,
  time TEXT,
  location TEXT,
  capacity INTEGER,
  deadline TEXT,
  description TEXT,
  instructions TEXT,
  registration_open INTEGER DEFAULT 1,
  featured INTEGER DEFAULT 0,
  created_at TEXT,
  updated_at TEXT
);

CREATE TABLE IF NOT EXISTS registrations (
  id TEXT PRIMARY KEY,
  event_id TEXT NOT NULL,
  user_id TEXT NOT NULL,
  user_name TEXT,
  status TEXT DEFAULT 'requested',
  created_at TEXT,
  UNIQUE(event_id, user_id)
);

CREATE TABLE IF NOT EXISTS certificates (
  id TEXT PRIMARY KEY,
  user_id TEXT NOT NULL,
  student_name TEXT NOT NULL,
  course_id TEXT NOT NULL,
  course_title TEXT NOT NULL,
  score INTEGER,
  issued_at TEXT,
  issuer TEXT,
  status TEXT DEFAULT 'valid',
  revoked_at TEXT
);

CREATE TABLE IF NOT EXISTS cert_requests (
  id TEXT PRIMARY KEY,
  user_id TEXT NOT NULL,
  course_id TEXT NOT NULL,
  course_title TEXT NOT NULL,
  student_name TEXT NOT NULL,
  score INTEGER,
  completed_at TEXT,
  status TEXT DEFAULT 'pending',
  note TEXT,
  cert_id TEXT,
  updated_at TEXT,
  UNIQUE(user_id, course_id)
);

CREATE TABLE IF NOT EXISTS user_progress (
  user_id TEXT NOT NULL,
  course_id TEXT NOT NULL,
  done_lessons TEXT DEFAULT '{}',
  scores TEXT DEFAULT '{}',
  started_at TEXT,
  last_lesson TEXT,
  updated_at TEXT,
  PRIMARY KEY (user_id, course_id)
);

CREATE TABLE IF NOT EXISTS user_saved (
  user_id TEXT NOT NULL,
  kind TEXT NOT NULL,
  target_id TEXT NOT NULL,
  saved_at TEXT,
  PRIMARY KEY (user_id, kind, target_id)
);

CREATE TABLE IF NOT EXISTS portfolios (
  user_id TEXT PRIMARY KEY,
  handle TEXT UNIQUE,
  name TEXT,
  bio TEXT,
  career TEXT,
  show_scores INTEGER DEFAULT 0,
  is_public INTEGER DEFAULT 0,
  entries TEXT DEFAULT '[]',
  updated_at TEXT
);
