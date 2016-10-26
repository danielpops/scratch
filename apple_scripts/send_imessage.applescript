# Sends an arbitrary iMessage to an arbitrary phone number
# Helpful for sending text messages in a scripted fashion
on run {targetPhoneNumber, targetMessage}
    tell application "Messages"
        # If you have more than one iMessage account, this might not work
        set targetService to 1st service whose service type = iMessage

        # Resolve the phone number to a contact that already exists in your contacts list
        set targetBuddy to buddy targetPhoneNumber of targetService

        # Hit [Send]
        send targetMessage to targetBuddy
    end tell
end run
