
# OrangeHRM UI Login Page Automation Testing

This project demonstrates automated UI testing of the OrangeHRM login page using modern tools and best practices.

## Tools

- Python
- Playwright
- Pytest
- GitHub Actions (CI/CD)

## Description

This project uses the **Playwright** Python library to automate end-to-end testing of the OrangeHRM login page.  
Tests are triggered automatically on every push to the main branch using **GitHub Actions**, ensuring continuous validation.

Key features:
- Parametrized test cases using `@pytest.mark.parametrize`
- Page Object Model (POM) design pattern
- Full test coverage using a **Decision Table** approach
- Automatic HTML report generation
- CI/CD integration with artifact upload

## Report

A **Decision Table** was used to design test cases covering all combinations of:
- Blank inputs
- Invalid credentials
- Valid credentials
- Case sensitivity

During testing, a bug was identified:  
🔐 **Username field is not case-sensitive** — both `Admin` and `admin` allow login with the correct password.
<img width="1838" height="887" alt="image" src="https://github.com/user-attachments/assets/2ecd04e9-b832-4d98-ada4-6ecd2a57c676" />

> ✅ This behavior may be intentional for usability, but should be documented and verified with product requirements.

## How to Run

1. Clone the repo:
`git clone https://github.com/biocodeit/playwright-python-orangehrm-tests.git`

text
2. Install dependencies:
`pip install -r requirements.txt
playwright install`

text
3. Run tests:
`pytest tests/ --html=report.html --self-contained-html`

