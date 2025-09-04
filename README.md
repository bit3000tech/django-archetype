# Django Project Template

A modern Django project template with a clean structure and best practices, built with uv for fast dependency management.

## Project Structure

```
django-template/
├── .venv/                  # Virtual environment (created by uv)
├── config/                 # Django configuration (renamed from project_name)
│   ├── __init__.py
│   ├── settings.py         # Main settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py            # WSGI application
│   └── asgi.py            # ASGI application
├── project/               # Project apps container
│   ├── __init__.py
│   └── sample/            # Sample app demonstrating structure
│       ├── migrations/
│       ├── __init__.py
│       ├── admin.py       # Admin configuration
│       ├── apps.py        # App configuration
│       ├── models.py      # Database models
│       └── tests.py       # Tests
├── web/                   # Templates and web-related files
│   ├── __init__.py
│   ├── base/              # Reusable template components
│   │   └── base.html      # Base template
│   ├── public/            # Public pages
│   │   ├── __init__.py
│   │   ├── forms.py       # Public forms
│   │   ├── views.py       # Public views
│   │   ├── urls.py        # Public URLs
│   │   ├── home.html      # Home page template
│   │   └── contact.html   # Contact page template
│   └── sample/            # Sample app templates
│       ├── __init__.py
│       ├── forms.py       # Sample forms
│       ├── views.py       # Sample views
│       ├── urls.py        # Sample URLs
│       ├── person_list.html
│       ├── person_detail.html
│       ├── person_form.html
│       └── person_confirm_delete.html
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## Features

- 🏗️ **Clean Structure**: Organized with separate folders for apps, templates, and configuration
- 🚀 **Modern Setup**: Uses uv for fast package management
- 📦 **Sample App**: Complete CRUD example with Person model
- 🎨 **Bootstrap UI**: Modern, responsive interface with Bootstrap 5
- 🔧 **Ready to Use**: Pre-configured settings and URL routing
- 📝 **Best Practices**: Follows Django conventions and best practices
- 🛠️ **Customization Script**: Easy project folder renaming with `customize_template.py`

## Quick Start

### Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. **Use this template** to create a new repository on GitHub
2. **Clone your new repository**:
   ```bash
   git clone https://github.com/yourusername/your-project-name.git
   cd your-project-name
   ```

3. **Customize the project structure** (optional but recommended):
   ```bash
   python customize_template.py your_project_name
   ```
   This will rename the `project/` folder to your custom name and update all references.
   
   Example:
   ```bash
   python customize_template.py blog      # Creates blog/ folder
   python customize_template.py shop      # Creates shop/ folder  
   python customize_template.py my_app    # Creates my_app/ folder
   ```

4. **Create and activate virtual environment**:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

5. **Install dependencies**:
   ```bash
   uv pip install -r requirements.txt
   ```

6. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Create sample data** (optional):
   ```bash
   python manage.py create_sample_people --count 5
   ```

8. **Create a superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

9. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

10. **Visit your site** at `http://127.0.0.1:8000/`

## Usage

### Customizing Project Structure

After cloning the template, you can customize the project folder name using the included script:

```bash
python customize_template.py your_project_name
```

**What the script does:**
- Renames `project/` folder to `your_project_name/`
- Updates all import statements in Python files
- Updates references in README.md and pyproject.toml
- Validates the project name for Python compatibility

**Examples:**
```bash
python customize_template.py blog        # Creates blog/ folder for a blog project
python customize_template.py ecommerce   # Creates ecommerce/ folder for online store
python customize_template.py portfolio   # Creates portfolio/ folder for portfolio site
```

### Creating New Apps

1. Create your app in your apps directory (default is `project/`, or your custom name):
   ```bash
   cd project  # or cd your_custom_name
   python ../manage.py startapp your_app_name
   ```

2. Update the app's `apps.py` to include the full path:
   ```python
   class YourAppConfig(AppConfig):
       default_auto_field = 'django.db.models.BigAutoField'
       name = 'project.your_app_name'  # or 'your_custom_name.your_app_name'
   ```

3. Add your app to `INSTALLED_APPS` in `config/settings.py`:
   ```python
   INSTALLED_APPS = [
       # ... other apps
       'project.your_app_name',  # or 'your_custom_name.your_app_name'
   ]
   ```

4. Create templates in `web/your_app_name/` directory
5. Create forms, views, and URLs in `web/your_app_name/` as needed

### Template Structure

- **Base templates**: Place reusable components in `web/base/`
- **App templates**: Create app-specific templates in `web/app_name/`
- **Static files**: Django will collect static files as usual
- **Forms & Views**: Keep business logic in `web/app_name/` for better organization

### Architecture Notes

This template uses a **separated concerns** approach:

- **`project/app_name/`**: Contains Django app essentials (models, admin, apps config, tests)
- **`web/app_name/`**: Contains presentation layer (views, forms, URLs, templates)

This separation keeps models and business logic separate from presentation logic, making the codebase more maintainable and easier to navigate.

## Sample App

The included `sample` app demonstrates:

- **Person Model**: Basic model with CRUD operations
- **Forms**: Django forms with Bootstrap styling
- **Views**: Function-based views for all CRUD operations
- **Templates**: Complete set of templates with Bootstrap UI
- **Admin**: Pre-configured admin interface

### Sample URLs

- `/` - Home page
- `/contact/` - Contact form
- `/sample/people/` - List all people
- `/sample/people/create/` - Create new person
- `/sample/people/<id>/` - View person details
- `/sample/people/<id>/edit/` - Edit person
- `/sample/people/<id>/delete/` - Delete person
- `/admin/` - Django admin interface

## Customization

### Settings

Main settings are in `config/settings.py`. Common customizations:

- **Database**: Update `DATABASES` setting
- **Static files**: Configure `STATIC_URL` and `STATIC_ROOT`
- **Media files**: Configure `MEDIA_URL` and `MEDIA_ROOT`
- **Time zone**: Set `TIME_ZONE`
- **Debug**: Set `DEBUG = False` for production

### Templates

- Modify `web/base/base.html` for site-wide changes
- Add new template directories to `TEMPLATES['DIRS']` if needed
- Customize Bootstrap theme by updating CDN links

### Apps

- Remove the `sample` app if not needed
- Create new apps following the structure shown above
- Update URLs in `config/urls.py` to include your app URLs

## Production Deployment

1. **Set environment variables**:
   ```bash
   export DEBUG=False
   export SECRET_KEY=your-secret-key
   export DATABASE_URL=your-database-url
   ```

2. **Install production dependencies**:
   ```bash
   uv pip install gunicorn psycopg2-binary
   ```

3. **Collect static files**:
   ```bash
   python manage.py collectstatic --noinput
   ```

4. **Run with Gunicorn**:
   ```bash
   gunicorn config.wsgi:application
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
