# SocialHunter - Advanced Username Search Tool

## Overview
SocialHunter is a powerful web application that hunts down social media accounts by username across 400+ social networks. Built by Swaraj Fugare (@swaraj.fugare_23), this modern tool provides a beautiful interface for comprehensive username searches.

## Project Setup
- **Language**: Python 3.11
- **Dependencies**: Managed via pyproject.toml (Poetry format)
- **Installation**: Successfully installed via pip in editable mode
- **Version**: 0.15.0

## Key Features
- Search for usernames across 400+ social networks
- Export results to CSV, XLSX, or text files
- Support for Tor proxy connections
- Customizable site filtering
- Verbose debugging options
- NSFW site inclusion option

## Usage Examples
```bash
# Search for a single username
sherlock username123

# Search multiple usernames
sherlock user1 user2 user3

# Search on specific sites only
sherlock --site GitHub --site Twitter username

# Export to CSV
sherlock --csv username

# Use Tor for anonymity
sherlock --tor username

# Get help
sherlock --help
```

## Project Structure
- `sherlock_project/` - Main package directory
  - `sherlock.py` - Core search logic
  - `sites.py` - Site configuration management
  - `notify.py` - Output notification handling
  - `result.py` - Result processing
  - `resources/data.json` - Social network site definitions
- `tests/` - Test suite
- `docs/` - Documentation and images
- `pyproject.toml` - Project configuration and dependencies

## Configuration
The project is ready to use with all dependencies installed. The workflow displays usage instructions when started.

## Web Interface
The project now includes a modern web interface built with Flask:
- **Frontend**: Beautiful Bootstrap-based UI with search form and results display
- **Backend**: Flask web application that integrates with Sherlock CLI
- **Port**: Runs on port 5000 (configured for Replit environment)
- **Features**: 
  - Real-time username search across popular social networks
  - Formatted results display with direct links to found accounts
  - Mobile-responsive design
  - Error handling and timeout management

## File Structure
```
/
├── app.py                 # Flask web application
├── templates/
│   ├── index.html        # Main search page
│   └── results.html      # Results display page
├── static/               # Static files (CSS, JS, images)
├── sherlock_project/     # Original Sherlock package
└── requirements files
```

## Current State
✅ Python 3.11 installed
✅ All dependencies installed via pip
✅ Flask web interface created and running
✅ Project tested and working
✅ Workflow configured for web application on port 5000
✅ Deployment configuration set up
✅ .gitignore properly configured for Python projects

## Developer Information
- **Created by:** Swaraj Fugare
- **Instagram:** [@swaraj.fugare_23](https://instagram.com/swaraj.fugare_23)
- **Project Name:** SocialHunter
- **Main File:** `main.py` (entry point), `app.py` (Flask application)

## Recent Changes
- 2025-09-07: Rebranded to SocialHunter with modern design
- 2025-09-07: Added profile image display instead of favicons
- 2025-09-07: Created organized project structure
- 2025-09-07: Added developer branding throughout application
- All dependencies successfully installed and configured for production