# Mr. Know All - Information Retrieval Desktop Application

The Mr. Know All project is a versatile information retrieval desktop application that allows users to quickly access relevant information in both English and Hebrew languages. The goal is to empower users with real-time knowledge and provide instant answers to their queries. By implementing a user-friendly Tkinter-based GUI, the application ensures a seamless and intuitive user experience.


## Features
### User-Friendly Interface: 
The GUI provides a simple and intuitive user experience. Users can enter their queries in a text box and obtain instant answers.

### Multilingual Support:
Mr. Know All supports both English and Hebrew languages, empowering users to search for information in their preferred language.

### Information from Wikipedia: 
The application leverages natural language processing (NLP) to extract relevant data from Wikipedia based on user queries.

### Performance Optimization: 
Mr. Know All implements caching to reduce response time and avoid redundant API calls, improving overall performance.

## Architecture
The application follows the Model-View-Controller (MVC) pattern to ensure clear separation of concerns and maintainable code:

### Model:
The Model component is responsible for managing data and handling the application's business logic. It represents the core data structures and algorithms required to process user queries and retrieve information from external APIs. In this project, the Model includes:
Interaction with Wikipedia and Google APIs to fetch information based on user queries.
Implementation of caching functionality to store previous search results for improved performance.
Definition of the main data model used by the application to organize and manage the retrieved information.
### View: 
The View component deals with the graphical user interface (GUI) and is responsible for presenting information to the user. It captures user inputs and displays the application's output in a user-friendly manner. The View provides a platform for users to interact with the application. In this project, the View includes:
The Tkinter-based GUI (Graphical User Interface) responsible for creating windows, buttons, and text inputs.
Display of the application logo to enhance visual appeal and branding.
### Controller: 
The Controller component acts as an intermediary between the Model and the View. It handles user inputs from the GUI, updates the Model based on these inputs, and ensures that the View displays the relevant information obtained from the Model. The Controller orchestrates the flow of information and interactions between the Model and the View. In this project, the Controller includes:

The main controller (Main.py) responsible for managing user inputs, coordinating Model actions, and updating the View accordingly.

## Installation
To install and run the Mr. Know All application, please follow these steps:

1. Clone the repository: git clone https://github.com/your-username/mr-know-all.git
2. Install the required dependencies: pip install -r requirements.txt
3. Run the application: python main.py
   
## Usage
1. Access the application by running main.py.
2. Enter your query in the text box and click the "send" button (or press Enter) to see the Wikipedia summary.
3. To swich the language search, click the "English"/"Hebrew" button.
   
The application will also utilize caching to optimize response time for repeated queries.

## Contributing
Contributions to enhance the Mr. Know All application are welcome. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: git checkout -b feature/your-feature
3. Make your changes and commit them: git commit -m 'Add your feature'
4. Push to the branch: git push origin feature/your-feature
5. Submit a pull request explaining your changes.
I hope that Mr. Know All provides users with a valuable tool for quickly gathering knowledge on various topics, enhancing their information retrieval experience.

![image](https://github.com/ohad1s/Mr.-Know-All/assets/92723105/ea5bf6aa-8796-44dd-9607-3c0bf729b93c)

