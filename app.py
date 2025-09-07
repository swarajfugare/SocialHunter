#!/usr/bin/env python3
"""
SocialHunter - Advanced Username Search Tool
Developed by: Swaraj Fugare (@swaraj.fugare_23)
Description: Hunt down social media accounts by username across 400+ social networks
"""

from flask import Flask, render_template, request, jsonify, redirect
import subprocess
import json
import os
import tempfile
from datetime import datetime
import re
from urllib.parse import urlparse

app = Flask(__name__, template_folder='templates', static_folder='static')

def get_profile_image_url(site_name, username, site_url):
    """Get profile image URL for a given site and username, fallback to website logo"""
    # Primary: Try to get user profile picture
    profile_patterns = {
        'GitHub': f'https://github.com/{username}.png?size=64',
        'Instagram': f'https://unavatar.io/instagram/{username}',
        'Twitter': f'https://unavatar.io/twitter/{username}',
        'YouTube': f'https://unavatar.io/youtube/@{username}',
        'Reddit': f'https://unavatar.io/reddit/{username}',
        'Facebook': f'https://unavatar.io/facebook/{username}',
        'LinkedIn': f'https://unavatar.io/linkedin/{username}',
        'TikTok': f'https://unavatar.io/tiktok/{username}',
        'Twitch': f'https://unavatar.io/twitch/{username}',
        'Steam': f'https://unavatar.io/steam/{username}',
        'Telegram': f'https://unavatar.io/telegram/{username}',
        'Discord': f'https://unavatar.io/discord/{username}',
    }
    
    # Return user profile image if available for this site
    if site_name in profile_patterns:
        return {
            'primary': profile_patterns[site_name],
            'fallback': get_website_favicon(site_url)
        }
    else:
        # For unknown sites, use website favicon as primary
        return {
            'primary': get_website_favicon(site_url),
            'fallback': f'https://ui-avatars.com/api/?name={username}&background=667eea&color=fff&size=64&bold=true'
        }

def get_website_favicon(url):
    """Get website favicon URL"""
    try:
        parsed = urlparse(url)
        domain = parsed.netloc
        return f'https://www.google.com/s2/favicons?sz=64&domain={domain}'
    except:
        return 'https://www.google.com/s2/favicons?sz=64&domain=example.com'

def run_sherlock_search(username, sites=None):
    """Run Sherlock search and return results"""
    try:
        # Build command - search ALL sites for comprehensive results
        cmd = ['sherlock', username, '--print-found', '--no-txt', '--timeout', '30']
        
        # Add specific sites if provided, otherwise search ALL available sites
        if sites:
            for site in sites:
                cmd.extend(['--site', site])
        # No else clause - this will search ALL 400+ sites by default
        
        # Run sherlock command
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        
        # Parse the output to get found sites
        found_sites = []
        if result.stdout:
            lines = result.stdout.strip().split('\n')
            for line in lines:
                # Look for lines with [+] indicating found accounts
                if '[+]' in line:
                    # Extract site name and URL using improved regex
                    match = re.search(r'\[\+\]\s+([^:]+):\s+(https?://[^\s]+)', line)
                    if match:
                        site_name = match.group(1).strip()
                        url = match.group(2).strip()
                        
                        # Get profile image URLs (primary and fallback)
                        image_urls = get_profile_image_url(site_name, username, url)
                        
                        found_sites.append({
                            'site': site_name,
                            'url': url,
                            'profile_image': image_urls['primary'],
                            'fallback_image': image_urls['fallback'],
                            'status': 'found'
                        })
        
        # Define priority order for top websites (they appear first)
        priority_sites = [
            'Instagram', 'Twitter', 'Facebook', 'GitHub', 'LinkedIn', 'YouTube', 
            'TikTok', 'Reddit', 'Snapchat', 'Pinterest', 'Twitch', 'Discord',
            'Steam', 'Spotify', 'SoundCloud', 'Telegram', 'WhatsApp', 'Tumblr',
            'DeviantArt', 'Flickr', 'Vimeo', 'Behance', 'Medium', 'Quora'
        ]
        
        # Sort found sites: priority sites first, then alphabetical
        def get_sort_key(site):
            site_name = site['site']
            if site_name in priority_sites:
                return (0, priority_sites.index(site_name))  # Priority sites come first
            else:
                return (1, site_name.lower())  # Other sites alphabetically
        
        found_sites.sort(key=get_sort_key)
        
        return {
            'username': username,
            'found_sites': found_sites,
            'total_found': len(found_sites),
            'search_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'status': 'success'
        }
    
    except subprocess.TimeoutExpired:
        return {
            'username': username,
            'error': 'Search timed out after 60 seconds',
            'status': 'timeout'
        }
    except Exception as e:
        return {
            'username': username,
            'error': str(e),
            'status': 'error'
        }

@app.route('/')
def index():
    """Main page with search form"""
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    """Handle search request"""
    if request.method == 'GET':
        # Redirect GET requests to home page
        return redirect('/')
    
    username = request.form.get('username', '').strip()
    
    if not username:
        return render_template('index.html', error='Please enter a username')
    
    # Basic validation
    if len(username) < 2 or len(username) > 50:
        return render_template('index.html', error='Username must be between 2 and 50 characters')
    
    # Run the search
    results = run_sherlock_search(username)
    
    return render_template('results.html', results=results)

@app.route('/api/search', methods=['POST'])
def api_search():
    """API endpoint for search"""
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({'error': 'Username is required'}), 400
    
    username = data['username'].strip()
    sites = data.get('sites', [])
    
    if not username:
        return jsonify({'error': 'Username cannot be empty'}), 400
    
    results = run_sherlock_search(username, sites)
    return jsonify(results)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)