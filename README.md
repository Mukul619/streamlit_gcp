# **Deploying a Streamlit App on Google Cloud Run**

This guide explains how to deploy a **Streamlit app** to **Google Cloud Run**, a fully managed platform for running containerized applications. The repository already includes `app.py`, `Dockerfile`, and `requirements.txt`.

---

## **Table of Contents**
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Steps to Deploy](#steps-to-deploy)
4. [Logging and Debugging](#logging-and-debugging)
5. [References](#references)

---

## **Overview**
[Streamlit](https://streamlit.io/) is an open-source Python library for building interactive web apps for data visualization and machine learning. **Google Cloud Run** allows you to host and scale containerized applications seamlessly.

---

## **Prerequisites**
1. A **Google Cloud Platform (GCP) account** with a project set up and billing enabled.
2. The following tools installed:
   - [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
   - [Docker](https://docs.docker.com/get-docker/)
   - [Git](https://git-scm.com/)
3. Python 3.7+ installed locally.

---

## **Steps to Deploy**

### 1. **Clone the Repository**
Clone the repository containing the `app.py`, `Dockerfile`, and `requirements.txt` to your local machine.

### 2. **Authenticate with Google Cloud**
Log in to your Google Cloud account and set the active project using the Google Cloud SDK:
- Authenticate with `gcloud auth login`.
- Set the project using `gcloud config set project [PROJECT_ID]`.

### 3. **Enable Necessary APIs**
Enable the required APIs for deployment:
- **Artifact Registry API** for storing Docker images.
- **Cloud Run API** for deploying the app.

### 4. **Build and Push the Docker Image**
- Use Docker to build the container image for the Streamlit app.
- Tag the image and push it to **Google Artifact Registry**.

### 5. **Deploy to Google Cloud Run**
Deploy the containerized app to Google Cloud Run. Ensure the following:
- The app listens on the `PORT` environment variable (Cloud Run defaults to `8080`).
- Deploy the app with options like region, platform (managed), and allowing unauthenticated access.

---

## **Logging and Debugging**
1. Use Google Cloud Logs to troubleshoot issues:
   - Access the Logs Explorer in the Google Cloud Console.
   - Alternatively, use `gcloud logs read` to view logs from the terminal.

2. Common troubleshooting tips:
   - Verify the `PORT` variable is correctly configured in the app.
   - Ensure all dependencies are listed in `requirements.txt`.

---

## **References**
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Cloud Run Documentation](https://cloud.google.com/run/docs)
- [Docker Documentation](https://docs.docker.com/)

---

This guide provides a step-by-step process for deploying a Streamlit app to Google Cloud Run. If you encounter any issues, feel free to raise them in the repository or refer to the official documentation linked above.
