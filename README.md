# SauceDemo UI Automation Tests (Selenium)

This repository contains a **training UI automation project** built with **Python and Selenium**.  
I use this project to practice and improve my test automation skills in my free time.

The tests are written against the **SauceDemo** demo web application, which is widely used for learning end-to-end UI automation.

## Purpose of the Project

The main goals of this project are:
- Practice UI test automation using **Selenium WebDriver**
- Apply the **Page Object Model (POM)** design pattern
- Write clean, readable, and maintainable test code *(mostly by our beloved ChatGPT* :) *)*

This is a **non-commercial training project** that evolves over time as I learn and refine my skills.

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)

## Application Under Test

- Website: https://www.saucedemo.com/
- Type: Demo e-commerce application for automation practice

## Project Structure

```text
.
├── pages/           # Page Object classes
├── tests/           # UI tests
├── conftest.py      # Pytest fixtures and browser setup
├── pytest.ini       # Pytest configuration
├── requirements.txt # Install before run tests
├── README.md        # You are reading right now (:
└── run_test.ps1     # Script that run tests by path and creates beatiful Allure report
