# -*- coding: utf-8 -*-

# Script Name: boilerplate.py
# Description: A Python script that generates a basic boilerplate for new Python projects.
# Version: 1.0
# Author: Trevor Roberts
# Author URI: https://github.com/TrevorRoberts/basic-python-boilerplate
# Copyright: Copyright (c) 2025 Trevor Roberts. All rights reserved.

import sys
import json
import os
from datetime import datetime

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input(prompt, allow_null=False):
    """Prompts the user for input and handles empty responses."""
    while True:
        value = input(prompt).strip()
        if value or allow_null:
            return value

def load_config(file_path="config.json"):
    """Load the configuration file."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return {
            "company_name": None,
            "company_url": None,
            "author_name": None,
            "author_url": None,
            "github_url": None
        }

def save_config(config, file_path="config.json"):
    """Save the configuration file."""
    with open(file_path, 'w') as file:
        json.dump(config, file, indent=4)
    print(f"Configuration saved to {file_path}")

def display_config(config):
    """Display the current configuration."""
    print("Current Configuration:")
    print(f"Company Name: {config.get('company_name', 'Not Set')}")
    print(f"Company URL: {config.get('company_url', 'Not Set')}")
    print(f"Author Name: {config.get('author_name', 'Not Set')}")
    print(f"Author URL: {config.get('author_url', 'Not Set')}")
    print(f"GitHub URL: {config.get('github_url', 'Not Set')}")

def update_config(config):
    """Prompt user to update configuration values."""
    print("\nUpdate Configuration (press Enter to keep current value):")
    
    # Define the order of fields to ensure related fields stay together
    field_order = ["company_name", "company_url", "author_name", "author_url", "github_url"]
    
    for key in field_order:
        current_value = config[key]
        display_value = current_value if current_value is not None else "Not Set"        
        user_input = input(f"{key.replace('_', ' ').title()} [{display_value}]: ")
        
        if user_input.strip():
            config[key] = user_input
        # If user just presses Enter, keep the current value (even if it's None)
    
    return config

def edit_config_file(config_file):
    """Edits an existing config.json file."""
    config = load_config(config_file)
    display_config(config)
    
    updated_config = update_config(config)
    
    save_choice = input("\nSave changes? (y/n): ").lower()
    if save_choice == 'y':
        save_config(updated_config, config_file)
        print("Changes saved successfully!")
    else:
        print("Exiting without saving changes.")

def load_or_create_config():
    """Loads or creates the config.json file."""
    config = load_config()
    return config

def update_config_for_boilerplate(config):
    """Updates the config with missing details for the boilerplate."""
    return config

def create_boilerplate(filename, config):
    """Creates a Python boilerplate with specified filename."""
    current_year = datetime.now().year
    company_name = config.get('company_name', '')
    company_url = config.get('company_url', '')
    author_name = config.get('author_name', '')
    author_url = config.get('author_url', '')
    github_url = config.get('github_url', '')

    # Determine the copyright holder
    copyright_holder = company_name if company_name else author_name if author_name else ''

    # Construct the copyright line
    if copyright_holder:
        copyright_line = f'Copyright (c) {current_year} {copyright_holder}. All rights reserved.'
    else:
        copyright_line = f'Copyright (c) {current_year}. All rights reserved.'

    description = get_user_input("Enter a brief description of your script: ")

    # Ask user about additional libraries
    imports = [
        "import sys",
        "import json",
        "import os",
        "from datetime import datetime"
    ]

    libraries = {
        "numpy": "Numerical computations",
        "pandas": "Data manipulation and analysis",
        "matplotlib": "Data visualization",
        "requests": "HTTP requests",
        "scikit-learn": "Machine learning",
        "flask": "Web development (Flask)",
        "scipy": "Scientific computing",
        "tkinter": "GUI development",
        "sqlite3": "Database operations",
        "beautifulsoup4": "Web scraping"
    }

    for lib, desc in libraries.items():
        choice = input(f"Do you want to include {lib} ({desc})? (y/n): ")
        if choice.lower() == 'y':
            if lib == "matplotlib":
                imports.append("import matplotlib.pyplot as plt")
            elif lib == "tkinter":
                imports.append("import tkinter as tk")
            elif lib == "sqlite3":
                imports.append("import sqlite3")
            elif lib == "beautifulsoup4":
                imports.append("from bs4 import BeautifulSoup")
            elif lib == "scikit-learn":
                imports.append("from sklearn import datasets, svm")
            else:
                imports.append(f"import {lib}")

    link_github = input("Would you like to link this script to a GitHub Repository? (y/n): ").lower()
    if link_github == 'y':
        if config.get('github_url'):
            github_url = config['github_url']
            print(f"Using GitHub URL from config.json: {github_url}")
        else:
            github_url = get_user_input("Enter GitHub URL: ")
            save_github = input("Save this GitHub URL to config.json for future use? (y/n): ").lower()
            if save_github == 'y':
                config['github_url'] = github_url
                save_config(config)
    else:
        github_url = ''
    
    boilerplate = f"""# -*- coding: utf-8 -*-

# Script Name: {filename}.py
# Description: {description}
# Version: 1.0
"""

    headers = []
    if company_name:
        headers.append(f"# Company Name: {company_name}")
    if company_url:
        headers.append(f"# Company URL: {company_url}")
    if author_name:
        headers.append(f"# Author: {author_name}")
    if author_url:
        headers.append(f"# Author URI: {author_url}")
    if github_url:
        headers.append(f"# GitHub URL: {github_url}")

    boilerplate += "\n".join(headers) + "\n"
    boilerplate += f"# Copyright: {copyright_line}\n\n"

    boilerplate += "\n".join(imports) + "\n\n"

    boilerplate += """
def clear_screen():
    \"\"\"Clears the terminal screen.\"\"\"
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    # Your code here

if __name__ == "__main__":
    main()
"""

    with open(f'{filename}.py', 'w') as file:
        file.write(boilerplate)

    print(f"Boilerplate created successfully as {filename}.py")


if __name__ == "__main__":
    clear_screen()
    print("boilerplate.py v2.4 by Trevor Roberts")
    print("Usage:")
    print("  python boilerplate.py <filename>  # Generate a boilerplate script")
    print("  python boilerplate.py --edit-config  # Edit the 'config.json' file")
    print("\n")

    if len(sys.argv) == 1:
        print("Error: No parameters provided. Please use one of the above commands.")
        sys.exit(1)

    if len(sys.argv) > 1 and sys.argv[1] == '--edit-config':
        edit_config_file('config.json')
    elif len(sys.argv) > 1:
        config = load_or_create_config()
        filename = sys.argv[1]
        create_boilerplate(filename, config)
