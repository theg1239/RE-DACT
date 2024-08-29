Welcome to RE-DACT's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   contributing
   installation
   usage
   api_reference

Overview
========

RE-DACT is a tool designed to help you with automated redaction of sensitive information from text. It leverages the power of `Presidio <https://microsoft.github.io/presidio/>`_ for entity recognition and anonymization.

Key Features:
-------------
- **Entity Recognition:** Automatically detect sensitive entities like PERSON, LOCATION, EMAIL_ADDRESS, etc.
- **Anonymization:** Replace detected entities with synthetic data or redact them as needed.
- **Flexible Sensitivity Levels:** Configure sensitivity levels to control which entities are redacted based on your requirements.

Getting Started
===============

To start using RE-DACT, follow these steps:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/SIH-VIT-24/RE-DACT.git

2. Create a virtual environment and activate it:

   .. code-block:: bash

      python -m venv env
      source env/bin/activate  # On Windows use `env\Scripts\activate`

3. Install the required dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

4. Run the application:

   .. code-block:: bash

      flask run

Contributing
============

We welcome contributions! Please refer to the :doc:`contributing` guide for more information on how to get started.

Project Board
=============

You can view the project board here: `RE-DACT Project Board <https://github.com/orgs/SIH-VIT-24/projects/2/views/3>`_

Use this board to assign yourself tasks and to track the progress of ongoing work.

Useful Links
============

- `GitHub Repository <https://github.com/SIH-VIT-24/RE-DACT>`_
- `Project Board <https://github.com/orgs/SIH-VIT-24/projects/2/views/3>`_
- `Presidio Documentation <https://microsoft.github.io/presidio/>`_

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
