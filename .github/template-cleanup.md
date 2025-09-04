# Django Project Template

🚀 **Welcome to your new Django project!**

This template provides a modern, well-structured Django project with best practices built-in.

## What's Included

- ✅ Clean project structure with separated concerns
- ✅ Sample app with CRUD operations
- ✅ Bootstrap 5 UI components
- ✅ Pre-configured templates
- ✅ Test suite setup
- ✅ Management commands
- ✅ uv package manager integration

## Quick Start

1. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Set up your environment**:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -r requirements.txt
   ```

3. **Initialize your database**:
   ```bash
   python manage.py migrate
   python manage.py create_sample_people --count 5
   ```

4. **Start developing**:
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/` to see your new Django project!

## Next Steps

- [ ] Update `README.md` with your project details
- [ ] Customize the base template in `web/base/base.html`
- [ ] Remove the sample app if not needed
- [ ] Add your own apps in the `project/` directory
- [ ] Configure your database settings
- [ ] Set up your deployment pipeline

## Need Help?

Check out the [full documentation](README.md) for detailed instructions on customizing and extending this template.

Happy coding! 🎉
