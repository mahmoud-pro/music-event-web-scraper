# Music Event Web Scraper

## Overview

The Music Event Web Scraper is a Python script designed to gather information about music events from various websites and store the data in a SQL database. This README file provides an overview of the project, instructions for setting up and running the scraper, and details on the data it collects and how it's stored.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Data Structure](#data-structure)
4. [SQL Database](#sql-database)
5. [Contributing](#contributing)

## Prerequisites

Before using the Music Event Web Scraper, make sure you have the following prerequisites installed:

- Python 3.6+
- pip (Python package manager)
- Selectolax
- Requests
- SQLite3 (for SQL database storage)

You can install the required Python libraries using pip:

```bash
pip install selectolax requests
```

## Installation

1. Clone or download the repository to your local machine:

```bash
git clone https://github.com/mahmoud-pro/music-event-web-scraper.git
```

## Data Structure

The scraper collects the following data for each music event:

- Band Name
- City
- Date

The data is stored in a structured format within the SQL database.

## SQL Database

The scraper uses SQLite as the default database system. The database file is named `data.db` by default. 

The database schema includes a table called `events`, with the following columns:

- `id` (Auto-incremented unique identifier)
- `band` (String)
- `city` (String)
- `date` (Date)

## Contributing

Contributions to this project are welcome. If you'd like to add support for additional websites, improve the scraper's functionality, or fix bugs, please fork the repository, make your changes, and submit a pull request.

