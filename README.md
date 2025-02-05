# **CS50W Overflow Application**
##### *Find answers to your technical questions regarding CS50w and help others answer theirs.*

## **Distinctiveness and Complexity**

This project is unique compared to other CS50W projects because it is a **technical Q&A platform** specifically designed for **CS50W related discussions**. While other projects like auctions, messaging, and social networking. This project **includes elements of structured Q&A forums, user-driven votings, problem solving**. The complexity of the project increases from the combination of **interactive user engagement, dynamic updates, and structured issue resolution**. and this project is fully mobile-responsive.

### **Key Features That Make It Distinctive:**  

1. **Structured Q&A Workflow**  
   - This platform is not focused on typical posts or comments, compared to the **Network project**. Rather than open-ended conversations, it follows a **Stack Overflow-style format** where each issue has **clear discussion**.  
   - Its **workflow-based problem-solving approach**, which didn't exist in earlier CS50W projects, allows users to **mark questions as solved**.  

2. **Advanced Voting System for Replies**  
   - This project highlights the most helpful replies using a **voting system on replies** rather than just **likes (as in Network)**.  
   - Votes directly impact the visibility of replies, ensuring **quality control**—a feature missing in other CS50W projects.  

3. **Real-Time Interaction with JavaScript & AJAX (More Dynamic Than Network or Commerce)**  
   - Many previous CS50W projects relied heavily on full-page reloads for updates.  
   - Here, **JavaScript (AJAX) dynamically updates** the vote counts and solved status, ensuring a **seamless user experience** without reloading the page.  

4. **Issue Categorization & Search Features (More Structured Than Other Projects)**  
   - Unlike **Commerce (which primarily focuses on item listings and bids)**, this project allows **filtering and categorization** of issues based on **CS50W project tags**, making it easier to find relevant technical discussions.  
   - A **search bar with keyword-based search** is implemented to improve accessibility.  

5. **Role-Based Interactions for Issue Resolution (More Interactive Than a Simple Forum)**  
   - In contrast to a **basic comment-based system**, this platform structures user actions around **solving issues**.  
   - Users can **vote on replies, submit solutions, and close issues**, giving a **workflow-based approach** to problem-solving rather than just posting content.  


## **Project structure:**

The project consists of the following files and directories:

- **`/core/`**: This directory contains the core Django app where models, views, and templates for issues and replies are defined.
  - `models.py`: Defines the database models, including `Issue`, `Reply` and `Vote`.
  - `views.py`: Handles the logic for register, login, logout, check profile, displaying issues, posting new issues, replying to issues, voting on replies, and closing issues.
  - `urls.py`: Contains URL routing for core functionalities such as issue posting, reply submission, and voting.
  - `templates/`: Contains HTML templates for displaying the web pages, such as the homepage, issue detail pages, reister page, login page, and profile page.

- **`/static/`**: Houses all static files, including Bootstrap styles and custom JavaScript files.
  - `scripts.js`: Manages dynamic functionality like updating vote counts and closing issues without reloading the page.

## How to Run the Application

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/me50/FaiqueMZM.git
   cd stackoverflow-clone
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Django**: Install Django by running:
   ```bash
   pip install django
   ```

4. **Run Migrations**: Set up the database by running the migrations:
   ```bash
   python manage,py makeigrations
   python manage.py migrate
   ```

5. **Start the Development Server**: Run the application:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**: Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the application.
```
