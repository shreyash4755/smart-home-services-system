\# Smart Home Services Management System with GenAI



\## Overview

This project is a Python-based Smart Home Services Management System designed to manage customer service requests, technician assignments, and issue resolution workflows.  

The system is enhanced with a \*\*GenAI-based intelligence layer\*\* that automatically classifies issues and predicts priority, simulating real-world enterprise automation.



This project demonstrates \*\*application development, system design, database management, and GenAI integration\*\* in an enterprise-style architecture.



---



\## Key Features

\- Create and track smart home service requests

\- Assign technicians and update request status

\- Persistent data storage using SQLite

\- Modular service-based architecture

\- \*\*GenAI-powered issue classification\*\*

\- \*\*GenAI-based priority prediction\*\*

\- Clean CLI-based interaction flow



---



\## GenAI Functionality

When a service request is created, the system uses a GenAI module to:

\- Analyze the issue description

\- Automatically classify the issue category:

&nbsp; - Electrical

&nbsp; - Network

&nbsp; - Device

&nbsp; - Software

&nbsp; - Other

\- Predict priority:

&nbsp; - Low

&nbsp; - Medium

&nbsp; - High



The GenAI logic is abstracted into a dedicated service layer, making it easy to replace the current rule-based logic with a real Large Language Model (LLM) API in production.



---



\## Architecture Overview





