#!/usr/bin/env python3
"""
Django Template Customization Script

This script customizes the Django template by:
1. Renaming the 'project' folder to your custom name
2. Updating all references in Python files
3. Updating import statements
4. Updating documentation

Usage:
    python customize_template.py your_project_name

Example:
    python customize_template.py my_blog
    python customize_template.py ecommerce_site
"""

import os
import sys
import re
import shutil
from pathlib import Path


def validate_project_name(name):
    """Validate that the project name is a valid Python module name"""
    if not name:
        return False, "Project name cannot be empty"
    
    if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name):
        return False, "Project name must be a valid Python identifier (letters, numbers, underscores only, cannot start with number)"
    
    if name in ['django', 'config', 'web', 'admin', 'auth', 'contenttypes', 'sessions', 'messages', 'staticfiles']:
        return False, f"'{name}' conflicts with Django built-in modules"
    
    return True, ""


def update_file_content(file_path, old_name, new_name):
    """Update content in a file, replacing old project name with new name"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace import statements
        content = re.sub(rf'\bproject\.{old_name}\b', f'{new_name}.{old_name}', content)
        content = re.sub(rf'\bproject\.', f'{new_name}.', content)
        content = re.sub(rf"'project\.", f"'{new_name}.", content)
        content = re.sub(rf'"project\.', f'"{new_name}.', content)
        
        # Replace in documentation strings
        content = content.replace('project/', f'{new_name}/')
        content = content.replace('project folder', f'{new_name} folder')
        content = content.replace('Project apps', f'{new_name.title()} apps')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False


def update_readme(new_name):
    """Update README.md with the new project name"""
    readme_path = Path('README.md')
    if not readme_path.exists():
        return False
    
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update project structure diagram
        content = content.replace('├── project/', f'├── {new_name}/')
        content = content.replace('│   └── project/', f'│   └── {new_name}/')
        content = content.replace('project/', f'{new_name}/')
        content = content.replace('Project apps container', f'{new_name.title()} apps container')
        content = content.replace('project.', f'{new_name}.')
        content = content.replace("'project.", f"'{new_name}.")
        content = content.replace('"project.', f'"{new_name}.')
        content = content.replace('project/sample', f'{new_name}/sample')
        content = content.replace('`project/', f'`{new_name}/')
        content = content.replace('**`project/', f'**`{new_name}/')
        
        # Update usage instructions
        content = content.replace('cd project', f'cd {new_name}')
        content = content.replace('in the `project/` directory', f'in the `{new_name}/` directory')
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error updating README.md: {e}")
        return False


def main():
    if len(sys.argv) != 2:
        print("Usage: python customize_template.py <your_project_name>")
        print("\nExample:")
        print("  python customize_template.py my_blog")
        print("  python customize_template.py ecommerce_site")
        sys.exit(1)
    
    new_project_name = sys.argv[1].lower()
    
    # Validate project name
    is_valid, error_msg = validate_project_name(new_project_name)
    if not is_valid:
        print(f"Error: {error_msg}")
        sys.exit(1)
    
    # Check if project folder exists
    project_path = Path('project')
    if not project_path.exists():
        print("Error: 'project' folder not found. Make sure you're running this script from the Django template root directory.")
        sys.exit(1)
    
    new_project_path = Path(new_project_name)
    if new_project_path.exists():
        print(f"Error: '{new_project_name}' folder already exists.")
        sys.exit(1)
    
    print(f"🚀 Customizing Django template...")
    print(f"📁 Renaming 'project' folder to '{new_project_name}'")
    
    try:
        # Step 1: Rename the project folder
        shutil.move(str(project_path), str(new_project_path))
        print(f"✅ Renamed folder: project → {new_project_name}")
        
        # Step 2: Update all Python files
        python_files = []
        for ext in ['*.py']:
            python_files.extend(Path('.').rglob(ext))
        
        updated_files = []
        for py_file in python_files:
            if '.venv' in str(py_file) or '__pycache__' in str(py_file):
                continue
                
            if update_file_content(py_file, 'sample', 'sample'):
                updated_files.append(str(py_file))
        
        # Update specific references
        for py_file in python_files:
            if '.venv' in str(py_file) or '__pycache__' in str(py_file):
                continue
                
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                content = content.replace('project.', f'{new_project_name}.')
                content = content.replace("'project.", f"'{new_project_name}.")
                content = content.replace('"project.', f'"{new_project_name}.')
                
                if content != original_content:
                    with open(py_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    if str(py_file) not in updated_files:
                        updated_files.append(str(py_file))
            except Exception as e:
                print(f"Warning: Could not update {py_file}: {e}")
        
        print(f"✅ Updated {len(updated_files)} Python files")
        
        # Step 3: Update README.md
        if update_readme(new_project_name):
            print("✅ Updated README.md")
        else:
            print("⚠️  Could not update README.md")
        
        # Step 4: Update pyproject.toml if it exists
        pyproject_path = Path('pyproject.toml')
        if pyproject_path.exists():
            try:
                with open(pyproject_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                content = content.replace('name = "django-template"', f'name = "{new_project_name}"')
                content = content.replace('known_first_party = ["config", "project", "web"]', 
                                        f'known_first_party = ["config", "{new_project_name}", "web"]')
                
                with open(pyproject_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print("✅ Updated pyproject.toml")
            except Exception as e:
                print(f"⚠️  Could not update pyproject.toml: {e}")
        
        print(f"\n🎉 Template customization complete!")
        print(f"📦 Your project structure now uses '{new_project_name}' instead of 'project'")
        print(f"\n📋 Next steps:")
        print(f"1. Run: python manage.py migrate")
        print(f"2. Run: python manage.py create_sample_people --count 5")
        print(f"3. Run: python manage.py runserver")
        print(f"4. Consider removing this script: rm customize_template.py")
        
    except Exception as e:
        print(f"❌ Error during customization: {e}")
        # Try to rollback if project was renamed but process failed
        if new_project_path.exists() and not project_path.exists():
            try:
                shutil.move(str(new_project_path), str(project_path))
                print("🔄 Rolled back folder rename")
            except:
                pass
        sys.exit(1)


if __name__ == '__main__':
    main()
