import collections as co
import string
alpha_lower = list(string.ascii_lowercase)

email_input = list(input())
email_letter = "".join(email_input)

a = co.Counter(email_input)
if a['@'] > 2:
    print("INVALID")
    exit()
else:
    local = email_letter.split('@')[0].lower()
    domain = email_letter.split('@')[1].lower()

    domain_period = co.Counter(domain)['.']
    if domain_period < 1:
        print("INVALID")
        exit()
    if ".." in domain:
        print("INVALID")
        exit()

    if not local or not domain:
        print("INVALID")
        exit()
    print("VALID")




