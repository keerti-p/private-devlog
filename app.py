from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_mysqldb import MySQL
import bcrypt
from functools import wraps
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'devlog-secret-2024'

# ── MySQL config ──
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql1234'
app.config['MYSQL_DB'] = 'devlog_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# ──────────────────────────────────────────────
# Auth decorator
# ──────────────────────────────────────────────
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

# ──────────────────────────────────────────────
# Home
# ──────────────────────────────────────────────
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

# ──────────────────────────────────────────────
# Login
# ──────────────────────────────────────────────
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()

        if user:
            try:
                if bcrypt.checkpw(
                    password.encode('utf-8'),
                    user['password_hash'].encode('utf-8')
                ):
                    session['user_id'] = user['id']
                    session['username'] = user['username']
                    session['avatar'] = user['avatar_initials']
                    return redirect(url_for('dashboard'))
            except Exception:
                pass

        flash('Invalid username or password', 'error')

    return render_template('login.html')

# ──────────────────────────────────────────────
# Register
# ──────────────────────────────────────────────
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']

        initials = ''.join([w[0].upper() for w in username.split()[:2]]) or username[:2].upper()

        pw_hash = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        ).decode('utf-8')

        cur = mysql.connection.cursor()

        try:
            cur.execute(
                "INSERT INTO users (username, password_hash, avatar_initials) VALUES (%s, %s, %s)",
                (username, pw_hash, initials)
            )
            mysql.connection.commit()
            flash('Account created! Please log in.', 'success')
            return redirect(url_for('login'))

        except Exception:
            mysql.connection.rollback()
            flash('Username already exists.', 'error')

        finally:
            cur.close()

    return render_template('register.html')

# ──────────────────────────────────────────────
# Logout
# ──────────────────────────────────────────────
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ──────────────────────────────────────────────
# Dashboard
# ──────────────────────────────────────────────
@app.route('/dashboard')
@login_required
def dashboard():
    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT a.*, u.username, u.avatar_initials,
               COUNT(k.id) AS kudos_count,
               MAX(CASE WHEN k.user_id = %s THEN 1 ELSE 0 END) AS user_gave_kudos
        FROM activities a
        JOIN users u ON a.user_id = u.id
        LEFT JOIN kudos k ON a.id = k.activity_id
        GROUP BY a.id, u.username, u.avatar_initials
        ORDER BY a.created_at DESC
        LIMIT 30
    """, (session['user_id'],))

    activities = cur.fetchall()

    cur.execute("SELECT COUNT(*) AS total FROM activities")
    total = cur.fetchone()['total']

    cur.execute("SELECT COUNT(*) AS cnt FROM users")
    members = cur.fetchone()['cnt']

    cur.execute("""
        SELECT DAYNAME(created_at) AS day, COUNT(*) AS cnt
        FROM activities GROUP BY day ORDER BY cnt DESC LIMIT 1
    """)
    most_active = cur.fetchone()

    cur.execute("""
        SELECT a.title, a.tag, a.created_at
        FROM activities a ORDER BY a.created_at DESC LIMIT 5
    """)
    recent = cur.fetchall()

    cur.close()

    return render_template(
        'dashboard.html',
        activities=activities,
        total=total,
        members=members,
        most_active=most_active,
        recent=recent
    )

# ──────────────────────────────────────────────
# Post Activity
# ──────────────────────────────────────────────
@app.route('/post', methods=['GET', 'POST'])
@login_required
def post_activity():
    if request.method == 'POST':
        title = request.form['title'].strip()
        description = request.form['description'].strip()
        tag = request.form['tag']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO activities (user_id, title, description, tag) VALUES (%s, %s, %s, %s)",
            (session['user_id'], title, description, tag)
        )
        mysql.connection.commit()
        cur.close()

        flash('Activity logged!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('post.html')

# ──────────────────────────────────────────────
# Kudos AJAX
# ──────────────────────────────────────────────
@app.route('/kudos/<int:activity_id>', methods=['POST'])
@login_required
def toggle_kudos(activity_id):
    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT id FROM kudos WHERE activity_id=%s AND user_id=%s",
        (activity_id, session['user_id'])
    )

    existing = cur.fetchone()

    if existing:
        cur.execute(
            "DELETE FROM kudos WHERE activity_id=%s AND user_id=%s",
            (activity_id, session['user_id'])
        )
        given = False
    else:
        cur.execute(
            "INSERT INTO kudos (activity_id, user_id) VALUES (%s, %s)",
            (activity_id, session['user_id'])
        )
        given = True

    mysql.connection.commit()

    cur.execute(
        "SELECT COUNT(*) AS cnt FROM kudos WHERE activity_id=%s",
        (activity_id,)
    )

    count = cur.fetchone()['cnt']
    cur.close()

    return jsonify({'kudos': count, 'given': given})

# ──────────────────────────────────────────────
# Timeline
# ──────────────────────────────────────────────
@app.route('/timeline')
@login_required
def timeline():
    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT a.*, u.username, u.avatar_initials,
               COUNT(k.id) AS kudos_count,
               DATE(a.created_at) AS activity_date
        FROM activities a
        JOIN users u ON a.user_id = u.id
        LEFT JOIN kudos k ON a.id = k.activity_id
        GROUP BY a.id, u.username, u.avatar_initials
        ORDER BY a.created_at DESC
    """)

    rows = cur.fetchall()
    cur.close()

    from collections import OrderedDict

    grouped = OrderedDict()

    for r in rows:
        d = r['activity_date'].strftime('%B %d, %Y')
        grouped.setdefault(d, []).append(r)

    return render_template('timeline.html', grouped=grouped)

# ──────────────────────────────────────────────
# Stats
# ──────────────────────────────────────────────
@app.route('/stats')
@login_required
def stats():
    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT u.username, u.avatar_initials, COUNT(a.id) AS activity_count
        FROM users u
        LEFT JOIN activities a ON u.id = a.user_id
        GROUP BY u.id
        ORDER BY activity_count DESC
    """)
    leaderboard = cur.fetchall()

    cur.execute("""
        SELECT tag, COUNT(*) AS cnt
        FROM activities
        GROUP BY tag
        ORDER BY cnt DESC
    """)
    tag_stats = cur.fetchall()

    cur.execute("""
        SELECT DAYNAME(created_at) AS day, COUNT(*) AS cnt
        FROM activities
        GROUP BY day
        ORDER BY cnt DESC
    """)
    day_stats = cur.fetchall()

    cur.execute("""
        SELECT DATE(created_at) AS d, COUNT(*) AS cnt
        FROM activities
        GROUP BY d
        ORDER BY d DESC
        LIMIT 14
    """)
    daily = cur.fetchall()

    cur.close()

    return render_template(
        'stats.html',
        leaderboard=leaderboard,
        tag_stats=tag_stats,
        day_stats=day_stats,
        daily=daily
    )

# ──────────────────────────────────────────────
# Run App
# ──────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)