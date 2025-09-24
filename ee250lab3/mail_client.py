import requests
import argparse
import pprint # For pretty printing

SERVER = 'http://localhost:5000'

def send_mail(recipient: str, sender: str, subject: str, body: str) -> bool:
    """
    Sends a mail entry to the server by making a POST request to the /mail endpoint.
    The JSON body of the request contains the following keys:
    - recipient
    - sender
    - subject
    - body
    
    Args:
        recipient (str): The recipient of the mail
        sender (str): The sender of the mail
        subject (str): The subject of the mail
        body (str): The body of the mail

    Returns:
        bool: True if the mail was sent successfully, False otherwise
    """
    mail_entry = {
        'recipient': recipient,
        'sender': sender,
        'subject': subject,
        'body': body,
    }
    response = requests.post(f'{SERVER}/mail', json=mail_entry)
    pprint.pprint(response.json())

def get_inbox(recipient: str) -> None:
    """
    Gets inbox for specific recipient by making GET request to the endpoint. 
    Response contains list of all emails in the recipient's inbox. 
    
    Args: 
        recipient (str) : email address of recipient whose inbox has get function applied to. 

    Returns: None- this function prints out the list of emails in recipient's inbox. 
    """
    response = requests.get(f'{SERVER}/mail/inbox/{recipient}')
    pprint.pprint(response.json())

def get_sent(sender: str) -> None:
    """
    Gets list of emails sent by sender by making GET request to endpoint.
    Response contains list of all emails sent by sender specified in argument. 

    Args: 
        sender (str) : email address of sender whose sent emails are listed. 

    Returns: None- this function prints out the list of emails sent by the specified sender. 
    """
    response = requests.get(f'{SERVER}/mail/sent/{sender}')
    pprint.pprint(response.json())

def get_mail(mail_id: str) -> None:
    """
    Gets mail specific to the mail ID given in the argument. 
    Response contains the mail corresponding with the mail ID. 

    Args: 
        mail id (str) : identification string of the email that is specified

    Returns: None - this function prints out the email associated with the ID
    """
    response = requests.get(f'{SERVER}/mail/{mail_id}')
    pprint.pprint(response.json())

def delete_mail(mail_id: str) -> None:
    """
    Deletes email specific to the mail ID given in the argument by sending DELETE request
    Response contains the message given by server after deleting email. 

    Args: 
        mail id (str) : identification string of email to be deleted

    Returns: None - this function prints out the response given by the server for deleting the email specific by the ID
    """
    response = requests.delete(f'{SERVER}/mail/{mail_id}')
    pprint.pprint(response.json())

# Command Line Interface
# making CLIs with argparse may be helpful for you in the future
# see if you can understand what each line is doing
def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Mail Client')
    
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    send_parser = subparsers.add_parser('send', help='Send a mail')
    send_parser.add_argument('body', help='The body of the mail')
    send_parser.add_argument(
        '-t', "--to", 
        dest="recipient",
        help='The recipient of the mail'
    )
    send_parser.add_argument(
        '-f', "--from",
        dest="sender",
        help='The sender of the mail'
    )
    send_parser.add_argument(
        '-s', "--subject", 
        help='The subject of the mail', 
        default="No Subject"
    )

    inbox_parser = subparsers.add_parser('inbox', help='Get your inbox')
    inbox_parser.add_argument('-u', "--user", help='The recipient of the mail')

    sent_parser = subparsers.add_parser('sent', help='Get your sent mail')
    sent_parser.add_argument('-u', "--user", help='The sender of the mail')

    get_parser = subparsers.add_parser('get', help='Get a mail')
    get_parser.add_argument('mail_id', help='The id of the mail')

    delete_parser = subparsers.add_parser('delete', help='Delete a mail')
    delete_parser.add_argument('mail_id', help='The id of the mail')

    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()

    if args.command == 'send':
        send_mail(args.recipient, args.sender, args.subject, args.body)
    elif args.command == 'inbox':
        get_inbox(args.user)
    elif args.command == 'sent':
        get_sent(args.user)
    elif args.command == 'get':
        get_mail(args.mail_id)
    elif args.command == 'delete':
        delete_mail(args.mail_id)

# TODO: run the code!
# to run the code, open a terminal and type:
#   python mail_client.py --help
# For example, to send a mail, type:
#   python mail_client.py send -t "recipient" -f "sender" -s "subject" "body"
# you'll need to demo sending, receiving, and deleting mail for checkoff.
if __name__ == '__main__':
    main()

