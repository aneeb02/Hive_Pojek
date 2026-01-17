# Hive 🐝

A feature-rich, real-time chat application built with Django that allows users to create and join topic-based chat rooms called "Hives". Connect with others, share ideas, and collaborate in real-time with video/audio calling, polls, and more.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.1.3-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 🎯 Core Features
- **Real-time Chat** - WebSocket-powered instant messaging
- **Topic-based Hives** - Create or join rooms organized by topics
- **Public & Private Hives** - Password-protected private rooms
- **File Sharing** - Share images, PDFs, and documents (up to 5MB)
- **Voice Messages** - Send audio recordings
- **Search** - Find hives by topic, name, or description

### 👥 User Management
- **User Profiles** - Customizable profiles with avatars and bios
- **Activity Feed** - See recent messages and user activity
- **Top Users Leaderboard** - Discover most active community members

### 🎭 Role-Based Permissions
- **Queen** (Creator) - Full control over the hive
- **Moderator** - Can kick members and create polls
- **Bee** (Member) - Regular participant

### 💬 Advanced Messaging
- **Pin Messages** - Highlight important messages
- **Vanishing Messages** - Auto-delete messages after 30 seconds
- **Spam Filtering** - Automatic offensive content detection
- **Message History** - Full chat history per hive

### 📞 Communication
- **Video Calls** - Powered by Agora RTC
- **Audio Calls** - Voice-only communication
- **Lobby System** - Pre-call waiting room

### 📊 Engagement
- **Polls** - Create and vote on polls within hives
- **Reactions** - Interactive engagement features
- **Spotify Integration** - Background music playlists

### 🎨 Customization
- **Theme Switching** - Light/Dark mode per hive
- **Custom Avatars** - Personalize your profile

---

## 🛠️ Tech Stack

**Backend:**
- Django 5.1.3
- Django REST Framework 3.15.2
- Django Channels 4.2.0 (WebSockets)
- Daphne 4.1.2 (ASGI server)

**Database:**
- SQLite3 (development)
- PostgreSQL recommended for production

**Real-time:**
- Redis 5.2.0 (Channel layer)
- channels-redis 4.2.1

**Video/Audio:**
- Agora RTC SDK
- agora-token-builder 1.0.0

**Frontend:**
- Django Templates
- Vanilla JavaScript
- CSS3

---

## 📋 Prerequisites

- Python 3.8 or higher
- Redis server
- Agora account (for video/audio features)

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Hive_Pojek.git
cd Hive_Pojek
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables Setup

Create a `.env` file in the project root (copy from `.env.example`):

```bash
# Copy the example file
cp .env.example .env
```

Edit `.env` and add your configuration:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Redis Configuration
REDIS_HOST=127.0.0.1
REDIS_PORT=6380

# Agora Video/Audio Settings
AGORA_APP_ID=your-agora-app-id
AGORA_APP_CERTIFICATE=your-agora-certificate
```

**How to get Agora credentials:**
1. Sign up at [Agora.io](https://www.agora.io/)
2. Create a new project
3. Copy your App ID and App Certificate

**Generate a new SECRET_KEY:**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Install and Start Redis

**Windows:**
```bash
# Download Redis from https://github.com/microsoftarchive/redis/releases
# Or use WSL/Docker
docker run -d -p 6380:6379 redis
```

**macOS:**
```bash
brew install redis
redis-server --port 6380
```

**Linux:**
```bash
sudo apt-get install redis-server
redis-server --port 6380
```

### 6. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 8. Run Development Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

---

## 📁 Project Structure

```
Hive_Pojek/
├── home/                   # Main application
│   ├── api/               # REST API endpoints
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
│   ├── consumers.py       # WebSocket consumers
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   └── forms.py           # Django forms
├── pojek/                 # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL config
│   ├── asgi.py            # ASGI configuration
│   └── wsgi.py            # WSGI configuration
├── static/                # Static files (CSS, JS, images)
├── templates/             # Base templates
├── utilities/             # Helper utilities
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # This file
```

---

## 🔒 Security Features

- **Password Hashing** - Private hive passwords are hashed using Django's PBKDF2
- **Spam Filtering** - Automatic detection of offensive content
- **File Validation** - Type and size restrictions on uploads
- **CSRF Protection** - Built-in Django CSRF middleware
- **Environment Variables** - Sensitive credentials stored securely
- **User Authentication** - Session-based authentication

---

## 🎮 Usage

### Creating a Hive
1. Click "Create Hive" button
2. Enter hive name (buzz), topic, and description
3. Choose public or private
4. If private, set a password
5. Click create

### Joining a Hive
1. Browse available hives on homepage
2. Click on a hive to join
3. For private hives, enter the password
4. Start chatting!

### Starting a Video Call
1. Inside a hive, click "Video Call"
2. Wait in the lobby
3. Other members can join
4. Enjoy your call!

### Creating a Poll
1. Inside a hive, click "Create Poll" (Queen/Moderator only)
2. Enter question and options
3. Members can vote
4. View results in real-time

---

## 🔧 API Endpoints

### Available Endpoints
```
GET  /api/                    # List all routes
GET  /api/hives/              # Get all hives
GET  /api/hives/:id/          # Get specific hive
POST /api/signup/             # User registration
```

**Note:** API is currently read-only. Full CRUD operations coming soon.

---

## 🧪 Testing

Run tests (when available):
```bash
python manage.py test
```

---

## 🚀 Deployment

### Production Checklist

1. **Environment Variables**
   ```env
   DEBUG=False
   SECRET_KEY=<strong-random-key>
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   ```

2. **Database**
   - Switch from SQLite to PostgreSQL
   - Update `DATABASES` in settings.py

3. **Static Files**
   ```bash
   python manage.py collectstatic
   ```

4. **Security Settings**
   - Enable HTTPS
   - Set `SECURE_SSL_REDIRECT = True`
   - Set `SESSION_COOKIE_SECURE = True`
   - Set `CSRF_COOKIE_SECURE = True`

5. **Redis**
   - Use production Redis instance
   - Update `REDIS_HOST` and `REDIS_PORT`

6. **Web Server**
   - Use Gunicorn + Nginx
   - Configure Daphne for WebSockets

---

## 🐛 Troubleshooting

### Redis Connection Error
```
Error: Connection refused (Redis)
```
**Solution:** Make sure Redis is running on port 6380:
```bash
redis-server --port 6380
```

### WebSocket Connection Failed
```
WebSocket connection failed
```
**Solution:** 
- Ensure Daphne is running (not runserver)
- Check `CHANNEL_LAYERS` configuration in settings.py
- Verify Redis is accessible

### Agora Token Error
```
Error: Invalid Agora credentials
```
**Solution:**
- Verify `AGORA_APP_ID` and `AGORA_APP_CERTIFICATE` in `.env`
- Check credentials in Agora console
- Ensure `.env` file is loaded

### Import Error: decouple
```
ModuleNotFoundError: No module named 'decouple'
```
**Solution:**
```bash
pip install python-decouple
```

### Database Migration Issues
```bash
# Reset migrations (development only!)
python manage.py migrate --fake home zero
python manage.py migrate home
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- Django framework and community
- Agora for video/audio SDK
- Redis for real-time capabilities
- All contributors and users

---

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

## 🗺️ Roadmap

- [ ] Complete REST API with full CRUD
- [ ] JWT authentication for API
- [ ] Direct messaging between users
- [ ] Message reactions and emojis
- [ ] Message editing and deletion
- [ ] Thread replies
- [ ] Push notifications
- [ ] Mobile app (React Native)
- [ ] Admin dashboard
- [ ] Analytics and insights
- [ ] Email verification
- [ ] OAuth integration (Google, GitHub)

---

**Built with ❤️ using Django**