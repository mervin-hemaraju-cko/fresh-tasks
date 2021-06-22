from . import constants as Const

# Checks the format of a ticket and reformat if necessary
def reformat_ticket_number(ticket):

    # Checks if hashtag found in string
    if("#" not in ticket):

        # If not, add it
        return f"#{ticket}"
    
    # else return initial
    return ticket

# Extract the ticket type and ticket number
def ticket_extract(ticket):

        # Reformat the ticket number
        ticket = reformat_ticket_number(ticket)

        # Split to get ticket type and number
        ticket_params = ticket.split(Const.FLAG_TICKET_SEPARATOR)

        # Check if split was successful
        if(len(ticket_params) != 2):
            raise IndexError(Const.EXCEPTION_FORMAT_TICKET)

        # Fetch params    
        ticket_type = ticket_params[0]
        ticket_number = ticket_params[1]

        return ticket_type, ticket_number