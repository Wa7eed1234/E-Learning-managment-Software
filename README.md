# E-learning portal

Django portal containing registration, profiles, cohorts, courses, projects, materials and email-related modules.

## Run locally

Setup is currently blocked by malformed dependency entries and environment-specific settings. First rename `requrements.txt` to `requirements.txt`, remove the literal `pip install` prefixes, and verify compatible versions. Configure a local MySQL database in `portal/settings.py`, use development-only secrets, and switch email to Django’s console backend. Then the intended local workflow is:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py check
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:8000
```

Open http://127.0.0.1:8000. MySQL client build dependencies may be required. These are conditional instructions, not a tested installation recipe.

## Current status and known limitations

Rename requrements.txt to requirements.txt and remove embedded 'pip install' text. Reconcile Django==4.0 with the settings header mentioning 4.1.7. Configure local MySQL and console email. Review tracked .env, settings credentials and uploaded media before deployment.

## Review status

Documentation drafted from repository source on 13 September 2026. This review did not run the application or certify it for production.

## Cleanup applied

- Renamed and normalized requirements.txt. Historical version pins are preserved and still need compatibility/security review.

The items above supersede the corresponding original review findings. Other listed limitations remain open.
