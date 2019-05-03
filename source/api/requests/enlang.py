"""
Contains standardized success and error messages
for use throughout the entire application.

The logic for putting all the errors into a generlized file and form
is as follows: centralization of error messages makes handeling
clearer now and eases future scaling.

@author: Elias Gabriel
@revision: v1.1
"""
##
## MESSAGES
##

# Create calendar
CAL_CREATE_FAILURE = "Something went wrong while creating a new calendar."
CAL_CREATE_SUCCESS = "A calendar was successfully created!"

# Get calendar
CAL_GET_FAILURE = "No calendar exists with the given identifier."
CAL_GET_SUCCESS = "Successfully fetched a calendar with the given UUID!"

# Sync calendar
CAL_SYNC_FAILURE = "Unable to sync calendar events. Did you send data correctly?"
CAL_SYNC_SUCCESS = "Successfully synced the provided events to the calendar!"
