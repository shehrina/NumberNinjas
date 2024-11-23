import csv
import os
import pandas as pd
import Student
import Teacher
import Admin
class savedata:
    """
    Manages the saving, loading, and modifying of user data in a CSV file.
    
    Attributes:
        df (DataFrame): A pandas DataFrame holding the current state of the user data.
    """
    def __init__(self):
<<<<<<< HEAD
        file_path = os.path.join(os.path.dirname(__file__), 'save_data.csv')
        try:
            self.df = pd.read_csv(file_path)
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=['Username', 'Password', 'Email', 'User_Type', 'Score'])
            self.df.to_csv(file_path, index=False)

=======
        """Initializes the savedata object by loading user data from a CSV file."""
        self.df = pd.read_csv('save_data.csv')
>>>>>>> 9f6a4692e24546c976ea42c19e63d02dbe89be66

    def addNewUser(self, username, password, email, usertype):
        """
        Adds a new user to the DataFrame and updates the CSV file.
        
        Parameters:
            username (str): The username of the new user.
            password (str): The password of the new user.
            email (str): The email address of the new user.
            usertype (str): The type of user being added (e.g., 'Student', 'Teacher', 'Admin').
        
        Returns:
            bool: True if the user was successfully added, False if the username already exists.
        """
        if (self.df['Username'] == username).any():
            return False
        else:
            score = 0

            if usertype == "Teacher":
                score = -1
            elif usertype == "Admin":
                score = 99
            newUser = {'Username': username, 'Password': password, 'Email': email, 'User_Type': usertype,'Score': score}
            newUser_df = pd.DataFrame([newUser])
            self.df = pd.concat([self.df, newUser_df], ignore_index=True)
            file_path = os.path.join(os.path.dirname(__file__), 'save_data.csv')
            self.df.to_csv(file_path, index = False)

            return True
    #load data from csv file with appropriate columns
    # def _load_data(self):
    #     #Check if file exists in directory. If not, create dataframe with columns
    #     if os.path.exists(self.filepath):
    #         return pd.read_csv(self.filepath)
    #     else:
    #         return pd.DataFrame(columns=['userName','password','email','currentScore','highScore'])
    #
    # def _load_data(self):
    #     #Check for valid file path
    #     if os.path.exists(self.filepath):
    #         return pd.read_csv(self.filepath)
    #     else:
    #         return pd.DataFrame(columns=['userName','password', 'email', 'currentScore', 'highScore', 'playTime'])
        
    def saveGame(self, student: Student):
        """
        Updates a student's score in the DataFrame and the CSV file.
        
        Parameters:
            student (Student): The student object whose score is to be updated.
        """
        # Update new player score
        self.df.loc[self.df['Username'] == student.getUserName(), 'Score'] = student.getScore()

        #save df to csv, without index
        file_path = os.path.join(os.path.dirname(__file__), 'save_data.csv')
        self.df.to_csv(file_path, index=False)

    # I dont think we need this because I dont know where we would even need this
    # def setUserData(self, userName, **kwargs):
    #     #Check for user in df
    #     if userName in self.df['userName'].values:
    #         #Update user data if they exist
    #         for key, value in kwargs.items():
    #             if key in self.df.columns:
    #                 self.df.loc[self.df['userName'] == userName, key] = value
    #
    #             else: # if user doesnt exist
    #                 new_data = {k: v for k, v in kwargs.items() if k in self.df.columns}
    #                 new_data['userName'] = userName
    #                 self.df = self.df.append(new_data, ignore_index = True)
    #             self._save_data()

            
    def getUserData(self, username, password):
        """
        Retrieves user data for a given username and password.
        
        Parameters:
            username (str): The username of the user.
            password (str): The password of the user.
        
        Returns:
            A dictionary containing user data if credentials match, None otherwise.
        """
        if (self.df['Username'] == username).any():
            userData = self.df[self.df['Username'] == username].to_dict(orient = 'records')[0]
            if userData['Password'] == password:
                return userData
            else:
                return None
        else:
            return None
        # # Retrieve user data row by userName
        # user_data = self.df.loc[self.df['userName'] == userName]
        # if not user_data.empty:
        #     return user_data.to_dict('records')[0]
        # return None

    # I dont think we need this either
    # def setUserScore(self, userName, newScore):
    #     # Set user score
    #     if userName in self.df['userName'].values:
    #         self.df.loc[self.df['userName'] == userName, 'currentScore'] = newScore
    #         # Update score by comparing to highScore to newScore if needed
    #         self.df.loc[(self.df['userName'] == userName) & (self.df['highScore'] < newScore), 'highScore'] = newScore
    #         self._save_data()
    def getDataframe(self):
        """
        Returns the DataFrame containing all user data.
        
        Returns:
            DataFrame: The DataFrame storing all user data.
        """
        return self.df
    def getHighScores(self):
        """
        Retrieves the top 5 high scores among students.
        
        Returns:
            DataFrame: A DataFrame containing the top 5 student usernames and their scores.
        """
        # Return the top 5 high scores from students

        return self.df[self.df['User_Type'] == 'Student'].nlargest(5, 'Score')[['Username', 'Score']]
    
    def deleteUserData(self, userName):
        """
        Deletes a user's data from the DataFrame and updates the CSV file.
        
        Parameters:
            userName (str): The username of the user to be deleted.
        
        Returns:
            bool: True if the user was successfully deleted, False otherwise.
        """
        #delete user data and profile based on userName if they exist in df
        if userName in self.df['Username'].values:
            self.df = self.df[self.df['Username'] != userName] #matches all rows that do not match userName, effectively removing those rows
            file_path = os.path.join(os.path.dirname(__file__), 'save_data.csv')
            self.df.to_csv(file_path, index=False)
            return True #deletion done
        else:
            return False #deletion not done/failed

#Reminder to mention this in documentation as a CRUD(Create,Read, Update, Delete) operation for user data management


                

