#!/usr/bin/env python3
"""
SocialHunter - Advanced Username Search Tool
Main Application Entry Point

Developed by: Swaraj Fugare
Instagram: @swaraj.fugare_23
Description: Hunt down social media accounts by username across 400+ social networks
"""

from app import app
import os

if __name__ == '__main__':
    print("🔍 Starting SocialHunter - Advanced Username Search Tool")
    print("💻 Developed by: Swaraj Fugare (@swaraj.fugare_23)")
    print("🌐 Searching across 400+ social networks...")
    print("=" * 50)
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)