# LinkedInConnectBot

## Description
LinkedInConnectBot is a Python bot that automates the process of sending connection requests on LinkedIn. It helps streamline the networking process by automatically sending connection requests to targeted individuals on LinkedIn.

## Files

| Filename      | Description                                                                   |
|---------------|-------------------------------------------------------------------------------|
| main.py       | Main file that handles the login and sending connection request functionality.|
| mouseclick.py | Utility script used to record the coordinates of specific points on the screen.|

## Why mouseclick.py?
The `mouseclick.py` script is included to address potential issues that may arise due to different screen sizes. By running `mouseclick.py`, you can obtain the coordinates of specific points on your screen. These coordinates can be used to accurately interact with elements on the LinkedIn page, such as buttons and sliders. The script records the coordinates when the right mouse button is clicked.

## Usage
1. Run `pip install -r requirements.txt` in terminal.
2. Run the `main.py` file to initiate the LinkedInConnectBot.
3. The bot will automate the process of sending connection requests on LinkedIn.
4. If the bot doesn't click the correct "Connect" buttons, follow these steps:
- Run the `mouseclick.py` script and record the following coordinates in the given order:
  - Coordinate of the reload button of the browser.
  - Coordinate of the downward arrow on the message box.
  - Coordinates of the four "Connect" buttons in the first row.
  - Coordinate of the slider that allows visibility of the second row of "Connect" buttons.
  - Coordinates of the four "Connect" buttons in the second row.
- Replace the corresponding coordinates in the `main.py` file with the recorded values.
- Please ensure to record the coordinates in the specified order for accurate functionality. 

## Future Features (Upcoming Enhancements)
LinkedInConnectBot has the potential to incorporate several features to further improve the user experience. Some possible features include:

- Personalized Message Templates: Allow users to create customized connection request messages for better engagement.
- Intelligent Targeting: Implement advanced algorithms to identify and connect with relevant professionals based on specific criteria.
- Connection Status Tracking: Track the status of sent connection requests to provide insights into accepted, pending, or rejected requests.
- Anti-Spam Measures: Implement measures to prevent the bot from triggering spam filters on LinkedIn.
- Error Handling and Logging: Enhance the error handling mechanism and implement a logging system for better debugging.

These features aim to enhance the functionality and user experience of LinkedInConnectBot. 

##T
## Contributions
Contributions are welcome! If you have any ideas for new features or improvements to enhance the user experience, please feel free to develop and contribute them. You can submit your contributions by opening a pull request. I appreciate your valuable input!
