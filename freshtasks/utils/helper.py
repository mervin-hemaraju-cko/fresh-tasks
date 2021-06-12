
# Checks the format of a ticket and reformat if necessary
def reformat_ticket_number(ticket):

    # Checks if hashtag found in string
    if("#" not in ticket):

        # If not, add it
        return f"#{ticket}"
    
    # else return initial
    return ticket