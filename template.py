import os


# 15 projects in total

PROJECTS = {
    "Classification": [
        "Credict Card Fraud - Imbalanced data",
        "Loan Prediction - Pyspark",
    ],
    "Regression": [
        "Bike Sharing Demand Analysis",
        "Sales Prediction and Analysis",
        "Housing Price Prediction",
    ],
    "NLP": [
        "Twitter Sentiment extraction",
        "SMS spam Detection",
        "Disaster Tweets Analysis",
    ],
    "Time-Series": [
        "Stock Market Analysis",
        "Time Series Forecasting",
        "Trafic Forecasting",
    ],
    "Clustering": [
        "Customer Segmentation",
        "Student Evaluation",
    ],
    "Recommendation-System": [
        "Movie Recommendation System",
        "Song Recommendation System",
    ],
}


def create_project_folders():
    """
    Create all folders and main files for the repository
    """
    for category, projects in PROJECTS.items():
        folder = os.path.join(os.getcwd(), category)
        for project in projects:
            project_folder = os.path.join(folder, project)
            os.makedirs(project_folder, exist_ok=True)

            # create the readme
            with open(os.path.join(project_folder, "README.md"), "w") as f:
                print(f"Created the readme.md file in {project_folder}")

            # create the data.csv
            with open(os.path.join(project_folder, "data.csv"), "w") as f:
                print(f"created the data.csv file in {project_folder}")

            ipynb_filename = "-".join(project.split()) + ".ipynb"
            with open(os.path.join(project_folder, ipynb_filename), "w") as f:
                print(f"created the {ipynb_filename} file in {project_folder}")


if __name__ == "__main__":
    create_project_folders()
